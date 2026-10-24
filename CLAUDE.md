# Claude · regole di questa repo

Progetto di voltalacarta. Regole generali in `voltalacarta/documentazione` (non serve leggerle se non per dubbi).

## Spendere pochi token

1. Orientati con `INDICE.md` (una riga per file) o `grep -i "parola" INDICE.md`. Apri solo i file che servono.
2. Non aggiornare a mano indici e tabelle tra i marcatori `<!-- indice:… -->`: lo fa l'Action dopo il push.
3. Clone superficiale: `git clone --depth 1`.

## Regole

- Ciò che si decide in chat → `python3 strumenti/nuova-decisione.py "Titolo" --tag … --sintesi "…"`, poi compila il file.
- Documenti in `docs/`, con frontmatter `titolo`, `stato`, `creato`, `aggiornato`, `tag` (e `sintesi` in una riga).
- Prima del commit: `python3 strumenti/controlla.py`. Messaggi di commit `tipo(ambito): descrizione`.
- Mai segreti o dati sensibili nella repo.
