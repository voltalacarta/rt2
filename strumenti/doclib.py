"""Funzioni comuni agli strumenti della documentazione: frontmatter, titolo, sintesi.

Nessuna dipendenza oltre a PyYAML. Le stesse regole usa il motore del grafo del second brain,
così la sintesi di un file è la stessa ovunque compaia.
"""

from __future__ import annotations

import datetime as dt
import re
from pathlib import Path
from typing import Any

import yaml

RADICE = Path(__file__).resolve().parent.parent
RE_FRONTMATTER = re.compile(r"\A﻿?---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.S)
RE_H1 = re.compile(r"^#[ \t]+(.+?)[ \t]*#*[ \t]*$", re.M)
RE_FENCE = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})")
RE_LINK = re.compile(r"(?<!!)\[((?:[^\[\]\n]|\[[^\]\n]*\])*)\]\(\s*<?([^)\s>]+)>?(?:\s+[\"'][^\"']*[\"'])?\s*\)")
RE_WIKILINK = re.compile(r"\[\[([^\]\|#\n]+)(?:#[^\]\|\n]*)?(?:\|([^\]\n]*))?\]\]")
RE_CODICE = re.compile(r"`([^`\n]*)`")
RE_ENFASI = re.compile(r"(\*\*|__|\*|_)(?=\S)(.+?)(?<=\S)\1")
RE_SERVIZIO = re.compile(
    r"^(decision[ei] di riferimento|torna (a|al|alla|all)\b|indice della cartella|vedi anche|stato:|"
    r"file generato|questo file è generato|sei qui)",
    re.I,
)

# Cartelle e file che non sono documentazione (modelli, automazioni, file generati).
ESCLUSI = ("_modelli/", ".github/", "node_modules/", ".devcontainer/", "strumenti/")
FILE_ESCLUSI = {"CLAUDE.md", "INDICE.md"}
STATI = {"bozza", "proposto", "attivo", "accettato", "superato", "archiviato"}


def _iso(v: Any) -> Any:
    if isinstance(v, (dt.date, dt.datetime)):
        return v.isoformat()[:10]
    if isinstance(v, list):
        return [_iso(x) for x in v]
    if isinstance(v, dict):
        return {k: _iso(x) for k, x in v.items()}
    return v


def leggi(percorso: Path) -> tuple[dict[str, Any], str, str | None]:
    """(metadati, corpo, errore del frontmatter o None)."""
    testo = percorso.read_text(encoding="utf-8")
    m = RE_FRONTMATTER.match(testo)
    if not m:
        return {}, testo, None
    try:
        dati = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        return {}, testo[m.end():], f"YAML non valido: {str(e).splitlines()[0]}"
    if not isinstance(dati, dict):
        return {}, testo[m.end():], "il frontmatter non è un elenco di campi"
    return _iso(dati), testo[m.end():], None


def senza_codice(testo: str) -> str:
    righe, dentro, recinto = [], False, ""
    for riga in testo.splitlines():
        m = RE_FENCE.match(riga)
        if m:
            segno = m.group(1)
            if not dentro:
                dentro, recinto = True, segno
                righe.append("")
                continue
            if segno[0] == recinto[0] and len(segno) >= len(recinto):
                dentro = False
                righe.append("")
                continue
        righe.append("" if dentro else riga)
    return "\n".join(righe)


def piano(md: str) -> str:
    t = RE_WIKILINK.sub(lambda m: (m.group(2) or m.group(1)).strip(), md)
    t = RE_LINK.sub(lambda m: m.group(1), t)
    t = RE_CODICE.sub(lambda m: m.group(1), t)
    for _ in range(2):
        t = RE_ENFASI.sub(lambda m: m.group(2), t)
    t = re.sub(r"<[^>\n]+>", "", t)
    return re.sub(r"\s+", " ", t).strip()


def titolo(meta: dict[str, Any], corpo: str, percorso: Path) -> str:
    if meta.get("titolo"):
        return piano(str(meta["titolo"]))
    m = RE_H1.search(senza_codice(corpo))
    if m:
        return piano(m.group(1))
    return percorso.parent.name if percorso.name.lower() == "readme.md" else percorso.stem


def sintesi(meta: dict[str, Any], corpo: str, massimo: int = 180) -> str:
    """Il campo `sintesi` se c'è, altrimenti la prima frase dell'apertura del documento."""
    if meta.get("sintesi"):
        return piano(str(meta["sintesi"]))
    pulito = re.sub(r"<!--.*?-->", "", senza_codice(corpo), flags=re.S)
    titoli = 0
    for blocco in re.split(r"\n[ \t]*\n", pulito):
        righe = [r.strip() for r in blocco.strip().splitlines() if r.strip()]
        if not righe:
            continue
        if re.match(r"^#{2,}\s", righe[0]):
            titoli += 1
            if titoli > 1:
                break
            righe = righe[1:]
            if not righe:
                continue
        prima = righe[0]
        if prima.startswith(("#", "|", "---", "<", "![", "- [", "* [", "←", "[←")) or re.match(r"^[-*+]\s|^\d+\.\s", prima):
            continue
        if len(righe) == 1 and re.fullmatch(r"(\*|_)(?!\1).+(\*|_)", prima):
            continue  # riga tutta in corsivo: versione, data, nota di servizio
        testo = piano(" ".join(r.lstrip("> ").strip() for r in righe))
        testo = re.sub(r"^(in sintesi|in breve|sintesi|tl;?dr|riassunto)\s*[.:—-]\s*", "", testo, flags=re.I)
        if len(testo) < 12 or testo.endswith(":") or RE_SERVIZIO.match(testo):
            continue
        frasi = re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý0-9\"«(])", testo)
        out = frasi[0]
        if len(out) < 40 and len(frasi) > 1:
            out = f"{out} {frasi[1]}"
        if len(out) > massimo:
            out = out[: massimo - 1].rsplit(" ", 1)[0].rstrip(",;:") + "…"
        return out
    return ""


def documenti(radice: Path = RADICE) -> list[Path]:
    """Tutti i file .md che sono documentazione, in ordine di percorso."""
    out = []
    for p in sorted(radice.rglob("*.md")):
        rel = p.relative_to(radice).as_posix()
        if rel.startswith(".git/") or any(rel.startswith(e) or f"/{e}" in f"/{rel}" for e in ESCLUSI) or p.name in FILE_ESCLUSI:
            continue
        out.append(p)
    return out


def cartella_decisioni(radice: Path = RADICE) -> Path:
    """10-decisioni/ (documentazione) o docs/decisioni/ (repo di progetto)."""
    for c in ("10-decisioni", "docs/decisioni", "decisioni"):
        if (radice / c).is_dir():
            return radice / c
    return radice / "docs" / "decisioni"


def oggi() -> str:
    return dt.date.today().isoformat()
