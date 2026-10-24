#!/usr/bin/env python3
"""Rigenera gli indici della documentazione dai metadati dei file. Zero token, zero lavoro a mano.

    python3 strumenti/indici.py            # riscrive gli indici e INDICE.md
    python3 strumenti/indici.py --verifica # esce con 1 se qualcosa non è aggiornato (per la CI)

1. In ogni README.md, il testo tra i marcatori
       <!-- indice:inizio -->            (o <!-- indice:inizio decisioni -->)
       <!-- indice:fine -->
   diventa la tabella dei file della cartella (titolo, sintesi, stato) e delle sottocartelle.
2. INDICE.md, nella radice, elenca TUTTI i documenti in una riga ciascuno: è la mappa
   che Claude legge al posto di aprire i file, per spendere pochi token.

Gira da sola in GitHub Actions a ogni push (.github/workflows/indici.yml).
"""

from __future__ import annotations

import re
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from doclib import RADICE, documenti, leggi, sintesi, titolo  # noqa: E402

RE_BLOCCO = re.compile(r"(<!-- indice:inizio(?P<tipo>[^>]*?)-->\n)(.*?)(<!-- indice:fine -->)", re.S)
RE_DECISIONE = re.compile(r"^(\d{4})-.+\.md$")
AVVISO = "<!-- Generato da strumenti/indici.py: le modifiche qui dentro vengono sovrascritte. -->"


def cella(t: object) -> str:
    return str(t or "").replace("|", "\\|").replace("\n", " ").strip()


def link(testo: str, verso: str) -> str:
    return f"[{testo.replace('[', '(').replace(']', ')')}]({urllib.parse.quote(verso)})"


def info(p: Path) -> dict:
    meta, corpo, _ = leggi(p)
    return {"titolo": titolo(meta, corpo, p), "sintesi": sintesi(meta, corpo), "stato": meta.get("stato") or "", "meta": meta}


def tabella_cartella(cartella: Path) -> str:
    righe = ["| Documento | Sintesi | Stato |", "| --- | --- | --- |"]
    valide = set(documenti())
    for sotto in sorted(d for d in cartella.iterdir() if d.is_dir() and (d / "README.md") in valide):
        i = info(sotto / "README.md")
        righe.append(f"| 📁 {link(i['titolo'], sotto.name + '/README.md')} | {cella(i['sintesi'])} | {cella(i['stato'])} |")
    for f in sorted(p for p in cartella.glob("*.md") if p.name != "README.md" and p in valide):
        i = info(f)
        righe.append(f"| {link(i['titolo'], f.name)} | {cella(i['sintesi'])} | {cella(i['stato'])} |")
    if len(righe) == 2:
        righe.append("| — | — | — |")
    return "\n".join(righe)


def tabella_decisioni(cartella: Path) -> str:
    righe = ["| N. | Decisione | Stato | Data |", "| --- | --- | --- | --- |"]
    for f in sorted(cartella.glob("*.md")):
        m = RE_DECISIONE.match(f.name)
        if not m:
            continue
        i = info(f)
        stato = cella(i["stato"])
        if i["meta"].get("sostituito-da"):
            stato += f" → {str(i['meta']['sostituito-da']).zfill(4)}"
        righe.append(f"| {link(m.group(1), f.name)} | {cella(i['titolo'])} | {stato} | {cella(i['meta'].get('creato'))} |")
    return "\n".join(righe)


def aggiorna_readme(p: Path) -> str | None:
    testo = p.read_text(encoding="utf-8")
    if "<!-- indice:inizio" not in testo:
        return None

    def sostituisci(m: re.Match) -> str:
        tipo = m.group("tipo").strip()
        corpo = tabella_decisioni(p.parent) if tipo == "decisioni" else tabella_cartella(p.parent)
        return f"{m.group(1)}{AVVISO}\n\n{corpo}\n\n{m.group(4)}"

    nuovo = RE_BLOCCO.sub(sostituisci, testo)
    return nuovo if nuovo != testo else None


def indice_generale() -> str:
    docs = documenti()
    righe = [
        "# Indice compatto",
        "",
        AVVISO,
        "",
        f"{len(docs)} documenti. Una riga per file: `percorso · titolo · stato · sintesi`.",
        "Per cercare: `grep -i \"parola\" INDICE.md`, poi apri solo i file trovati.",
        "",
    ]
    sezione = None
    for p in docs:
        rel = p.relative_to(RADICE).as_posix()
        testa = rel.split("/", 1)[0] if "/" in rel else "(radice)"
        if testa != sezione:
            sezione = testa
            righe += ["", f"## {testa}", ""]
        i = info(p)
        righe.append(f"- {rel} · {i['titolo']} · {i['stato'] or '-'} · {i['sintesi'][:150] or '-'}".rstrip())
    return "\n".join(righe).replace("\n\n\n", "\n\n") + "\n"


def main() -> int:
    verifica = "--verifica" in sys.argv
    da_scrivere: dict[Path, str] = {}
    for p in documenti():
        if p.name == "README.md":
            nuovo = aggiorna_readme(p)
            if nuovo is not None:
                da_scrivere[p] = nuovo
    indice = RADICE / "INDICE.md"
    testo_indice = indice_generale()
    if not indice.is_file() or indice.read_text(encoding="utf-8") != testo_indice:
        da_scrivere[indice] = testo_indice
    for p, t in da_scrivere.items():
        print(("da aggiornare: " if verifica else "aggiornato: ") + p.relative_to(RADICE).as_posix())
        if not verifica:
            p.write_text(t, encoding="utf-8")
    if not da_scrivere:
        print("Indici già aggiornati.")
    return 1 if (verifica and da_scrivere) else 0


if __name__ == "__main__":
    sys.exit(main())
