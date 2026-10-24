---
titolo: "rilegaretesi.it (nuovo sito)"
stato: attivo
creato: 2026-10-24
aggiornato: 2026-10-24
tag: [progetto]
sintesi: "Nuovo sito di vendita online delle tesi rilegate di Volta la carta."
---

# rilegaretesi.it (nuovo sito)

Nuovo sito di vendita online delle tesi rilegate di Volta la carta.

## Dove trovare cosa

| Cosa | Dove |
| --- | --- |
| Documentazione del progetto | [`docs/`](docs/README.md) |
| Decisioni del progetto | [`docs/decisioni/`](docs/decisioni/README.md) |
| Mappa compatta di tutti i file (anche per Claude) | `INDICE.md`, generato da solo |
| Regole generali di Volta la carta | [documentazione](https://github.com/voltalacarta/documentazione) |

## Come si lavora

- Apri la repo in un Codespace: *Code* → *Codespaces* → *Create codespace on main*.
- Una decisione nuova: `python3 strumenti/nuova-decisione.py "Titolo"`, poi compila il file.
- Indici e mappa si aggiornano da soli dopo il push; il progetto compare nel grafo del second brain entro qualche ora.

## Fonti dati

- **[Registro VLC](https://docs.google.com/spreadsheets/d/1oP_wjw2Vgfo60ZbXU06rWZ1XMu9-ltrZVTFVsf9RKjg/edit)** (Google Sheets, in `ProduzioneVLC` su Drive): catalogo copertine, finiture, listino stampa, extra.
- **MaterialeVLC** (Drive): materiale grezzo (foto, loghi, recensioni).

## Staging

Il sito in lavorazione è pubblicato su GitHub Pages: <https://voltalacarta.github.io/rt2/>. Il sito attuale rilegaretesi.it non viene toccato.
