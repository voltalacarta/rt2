---
titolo: Sito statico in HTML generato con Python
stato: proposto
creato: 2026-10-24
aggiornato: 2026-10-24
tag: [decisioni, tecnologia, staging]
sintesi: "Pagine HTML generate da un piccolo script Python (Jinja), catalogo in JSON copiato dal Registro VLC; pubblicazione automatica su GitHub Pages."
collegati: [0001]
sostituisce: 0002
---

# 0003 · Sito statico in HTML generato con Python

## Contesto

La proposta [0002](0002-sito-statico-con-astro-e-catalogo-dal-registro-vlc.md) prevedeva Astro. Nell'ambiente di lavoro di Claude il registro dei pacchetti npm non è raggiungibile, quindi Astro non si può né installare né provare prima della pubblicazione. Serve una soluzione equivalente che si possa costruire e controllare subito.

## Decisione

Proposta, da confermare:

- Pagine in HTML, CSS e JavaScript senza framework, con modelli Jinja in `src/` e generate da `strumenti/build.py` in `dist/`.
- Catalogo, finiture, listino ed extra in `src/data/catalogo.json`, copia del Registro VLC. Più avanti uno script lo aggiornerà dal foglio.
- I font sono ospitati nel sito (scaricati da Fontsource durante la pubblicazione), non caricati da Google Fonts.
- Pubblicazione automatica su GitHub Pages a ogni push su `main` (workflow `pages.yml`); lo staging ha `noindex` e `robots.txt` che blocca tutto.
- Due stili a confronto, *Legatoria* e *Studio*, scelti con un interruttore nella barra di prova.

## Alternative considerate

| Alternativa | Perché scartata |
| --- | --- |
| Astro (proposta 0002) | Non installabile nell'ambiente di lavoro di Claude; il vantaggio per un sito di poche pagine è piccolo |
| Google Fonts collegato | Invia gli indirizzi IP dei visitatori a Google: problema di privacy (GDPR) |

## Conseguenze

- ✅ Nessuna dipendenza da installare: il sito si genera con Python e una sola libreria.
- ✅ Pagine leggerissime, quindi veloci anche da smartphone.
- ⚠️ Pagamento e caricamento del PDF richiederanno comunque un servizio esterno.
