---
titolo: Nuovo sito separato, staging su GitHub Pages
stato: accettato
creato: 2026-10-24
aggiornato: 2026-10-24
tag: [decisioni, staging, github-pages]
sintesi: "Il sito attuale non si tocca; il nuovo si costruisce a parte e si pubblica in staging su GitHub Pages."
---

# 0001 · Nuovo sito separato, staging su GitHub Pages

## Contesto

Il sito attuale rilegaretesi.it porta ordini ogni giorno: intervenire mentre si costruisce il nuovo rischia di interrompere le vendite. Serve uno spazio dove vedere e provare il nuovo sito senza toccare quello in produzione. Collegata alla decisione [0009 della documentazione](https://github.com/voltalacarta/documentazione/blob/main/10-decisioni/0009-rifare-i-siti-rilegaretesi-it-e-voltalacarta-it-per-vendere.md).

## Decisione

- Il sito attuale (WordPress) **non si modifica**.
- Il nuovo sito si costruisce in questa repo e si pubblica in staging su **GitHub Pages** (`https://voltalacarta.github.io/rt2/`).
- Lo staging è escluso dai motori di ricerca (`noindex`) per non fare concorrenza al sito attuale.
- Il passaggio al dominio rilegaretesi.it si decide più avanti, a sito approvato.

## Alternative considerate

| Alternativa | Perché scartata |
| --- | --- |
| Correggere subito il sito attuale | Scelta dell'utente: non si tocca ciò che funziona |
| Staging su un hosting a pagamento | GitHub Pages basta per ora ed è gratuito |

## Conseguenze

- ✅ Nessun rischio per gli ordini in corso.
- ✅ Ogni modifica è visibile online pochi minuti dopo il push.
- ⚠️ GitHub Pages pubblica solo siti statici: pagamenti e caricamento PDF andranno provati con un servizio esterno.
- ⚠️ I problemi SEO del sito attuale (shop in `noindex`) restano finché il nuovo non va online.
