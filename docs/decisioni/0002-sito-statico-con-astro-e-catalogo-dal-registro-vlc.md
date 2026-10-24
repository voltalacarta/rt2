---
titolo: Sito statico con Astro e catalogo dal Registro VLC
stato: proposto
creato: 2026-10-24
aggiornato: 2026-10-24
tag: [decisioni, tecnologia, astro]
sintesi: "Proposta: sito statico Astro, catalogo letto dal Registro VLC, pagamenti e caricamento PDF in una fase successiva."
collegati: [0001]
---

# 0002 · Sito statico con Astro e catalogo dal Registro VLC

## Contesto

Lo staging su GitHub Pages richiede un sito statico. Serve una tecnologia veloce, adatta a Google e che non costringa a mantenere un CMS. Prezzi e colori devono restare modificabili da chi non programma.

## Decisione

Proposta, da confermare:

- Sito statico generato con **Astro**.
- Catalogo copertine, finiture, listino e extra letti dal **Registro VLC** (Google Sheets). Per lo staging se ne tiene una copia in `src/data/`; più avanti si aggiorna in automatico.
- Il configuratore calcola il prezzo nel browser con gli stessi dati.
- Pagamento (es. Stripe) e caricamento del PDF in una fase successiva, con un servizio esterno.

## Alternative considerate

| Alternativa | Perché scartata |
| --- | --- |
| WordPress con tema nuovo | Non gira su GitHub Pages; più lento e da mantenere |
| Shopify o simili | Canone mensile e configuratore con PDF difficile da personalizzare |

## Conseguenze

- ✅ Sito molto veloce, quindi buono per Google e per chi arriva da smartphone.
- ✅ Nessun pannello da aggiornare o proteggere.
- ⚠️ Per modificare testi e pagine serve passare dalla repo (o da Claude).
