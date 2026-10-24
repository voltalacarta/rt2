#!/usr/bin/env python3
"""Controlla i metadati di tutti i documenti. Esce con 1 se trova errori (per la CI).

Controlli: frontmatter leggibile; campi obbligatori; stato tra quelli ammessi; date AAAA-MM-GG;
tag come elenco; numeri delle decisioni unici e in sequenza; decisioni "collegate" esistenti;
nomi di file in minuscolo senza spazi né accenti.
"""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from doclib import RADICE, STATI, cartella_decisioni, documenti, leggi  # noqa: E402

OBBLIGATORI = ("titolo", "stato", "creato", "aggiornato", "tag")
SENZA_FRONTMATTER = {"README.md"}  # la home della repo può non averlo


def data_valida(v: object) -> bool:
    try:
        dt.date.fromisoformat(str(v))
        return True
    except ValueError:
        return False


def main() -> int:
    errori: list[str] = []
    avvisi: list[str] = []
    decisioni: dict[str, str] = {}
    for p in documenti():
        rel = p.relative_to(RADICE).as_posix()
        meta, _, errore = leggi(p)
        if errore:
            errori.append(f"{rel}: {errore}")
            continue
        if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", p.name.lower()) or p.name != p.name.lower() and p.name != "README.md":
            avvisi.append(f"{rel}: nome del file con maiuscole, spazi o accenti")
        if not meta:
            if rel not in SENZA_FRONTMATTER:
                errori.append(f"{rel}: manca il frontmatter")
            continue
        for campo in OBBLIGATORI:
            if campo not in meta or meta[campo] in (None, ""):
                errori.append(f"{rel}: manca il campo '{campo}'")
        if meta.get("stato") and str(meta["stato"]) not in STATI:
            errori.append(f"{rel}: stato '{meta['stato']}' non ammesso ({', '.join(sorted(STATI))})")
        for campo in ("creato", "aggiornato", "prossima_revisione"):
            if campo in meta and not data_valida(meta[campo]):
                errori.append(f"{rel}: '{campo}' non è una data AAAA-MM-GG")
        if "tag" in meta and not isinstance(meta["tag"], list):
            errori.append(f"{rel}: 'tag' deve essere un elenco, es. [uno, due]")
        if meta.get("sintesi") and len(str(meta["sintesi"])) > 200:
            avvisi.append(f"{rel}: 'sintesi' oltre 200 caratteri")
        m = re.match(r"^(\d{4})-", p.name)
        if p.parent == cartella_decisioni() and m:
            if m.group(1) in decisioni:
                errori.append(f"{rel}: numero {m.group(1)} già usato da {decisioni[m.group(1)]}")
            decisioni[m.group(1)] = rel
    for p in documenti():
        meta, _, _ = leggi(p)
        for c in meta.get("collegati") or []:
            if str(c).isdigit() and str(c).zfill(4) not in decisioni:
                errori.append(f"{p.relative_to(RADICE).as_posix()}: collegati → {str(c).zfill(4)} non esiste")
    numeri = sorted(int(n) for n in decisioni)
    mancanti = sorted(set(range(1, (numeri[-1] if numeri else 0) + 1)) - set(numeri))
    if mancanti:
        avvisi.append(f"{cartella_decisioni().relative_to(RADICE).as_posix()}: numeri mancanti {', '.join(f'{n:04d}' for n in mancanti)} (i numeri non si riusano)")
    for a in avvisi:
        print(f"avviso: {a}")
    for e in errori:
        print(f"ERRORE: {e}")
    print(f"{len(documenti())} documenti controllati · {len(errori)} errori · {len(avvisi)} avvisi")
    return 1 if errori else 0


if __name__ == "__main__":
    sys.exit(main())
