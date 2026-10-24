#!/usr/bin/env python3
"""Crea una nuova decisione con il numero successivo libero e stampa il percorso.

    python3 strumenti/nuova-decisione.py "Adottare il metodo PARA" --tag metodo,second-brain --collegati 4
    python3 strumenti/nuova-decisione.py "Titolo" --stato accettato --sintesi "Una riga che la riassume."

Dopo: compila le sezioni del file, commit e push. Indici e registro si aggiornano da soli.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from doclib import RADICE, STATI, cartella_decisioni, oggi  # noqa: E402

CARTELLA = cartella_decisioni()


def slug(testo: str) -> str:
    t = unicodedata.normalize("NFKD", testo)
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60].rstrip("-")


def prossimo_numero() -> int:
    numeri = [int(m.group(1)) for p in CARTELLA.glob("*.md") if (m := re.match(r"^(\d{4})-", p.name))]
    return max(numeri, default=0) + 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("titolo")
    ap.add_argument("--tag", default="", help="separati da virgola (decisioni è aggiunto da solo)")
    ap.add_argument("--collegati", default="", help="numeri di decisioni collegate, separati da virgola")
    ap.add_argument("--stato", default="proposto", choices=sorted(STATI))
    ap.add_argument("--sintesi", default="", help="una riga che riassume la decisione")
    ap.add_argument("--sostituisce", default="", help="numero della decisione che questa sostituisce")
    a = ap.parse_args()

    CARTELLA.mkdir(parents=True, exist_ok=True)
    n = prossimo_numero()
    file = CARTELLA / f"{n:04d}-{slug(a.titolo)}.md"
    tag = ["decisioni"] + [t.strip() for t in a.tag.split(",") if t.strip() and t.strip() != "decisioni"]
    collegati = [c.strip().zfill(4) for c in a.collegati.split(",") if c.strip()]
    righe = [
        "---",
        f"titolo: {a.titolo}",
        f"stato: {a.stato}",
        f"creato: {oggi()}",
        f"aggiornato: {oggi()}",
        f"tag: [{', '.join(tag)}]",
    ]
    if a.sintesi:
        righe.append(f"sintesi: {a.sintesi}")
    if collegati:
        righe.append(f"collegati: [{', '.join(collegati)}]")
    if a.sostituisce:
        righe.append(f"sostituisce: {a.sostituisce.zfill(4)}")
    righe += [
        "---",
        "",
        f"# {n:04d} · {a.titolo}",
        "",
        "## Contesto",
        "",
        "<!-- Qual è il problema? Perché decidere adesso? -->",
        "",
        "## Decisione",
        "",
        "<!-- Cosa si è deciso, in modo chiaro e verificabile. -->",
        "",
        "## Alternative considerate",
        "",
        "| Alternativa | Perché scartata |",
        "| --- | --- |",
        "| — | — |",
        "",
        "## Conseguenze",
        "",
        "- ✅ <!-- vantaggio -->",
        "- ⚠️ <!-- costo, rischio o vincolo -->",
        "",
    ]
    file.write_text("\n".join(righe), encoding="utf-8")
    print(file.relative_to(RADICE).as_posix())
    if a.sostituisce:
        print(f"Ricorda: nella decisione {a.sostituisce.zfill(4)} imposta 'stato: superato' e 'sostituito-da: {n:04d}'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
