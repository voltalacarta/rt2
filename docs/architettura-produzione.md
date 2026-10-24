---
titolo: "Architettura di produzione proposta (Cloudflare + Stripe)"
stato: proposto
creato: 2026-10-24
aggiornato: 2026-10-24
tag: [architettura, hosting, cloudflare, stripe]
sintesi: "Proposta: pagine statiche Astro su Cloudflare Workers, PDF su R2, ordini su D1, Stripe Checkout, Resend; costo fisso 0–55 €/anno."
---

# Architettura del nuovo rilegaretesi.it

Proposta per la produzione. Lo staging resta su GitHub Pages (decisione [0001](decisioni/0001-nuovo-sito-separato-staging-su-github-pages.md)); qui si descrive la parte dinamica (pagamenti, PDF, ordini). Va confermata con una decisione.

## Schema

```
            GitHub (repo privato)
                   │ push
                   ▼
          Cloudflare Workers Builds ──► deploy automatico
                   │
   ┌───────────────┴────────────────────────────────────────┐
   │  rilegaretesi.it  (Cloudflare Worker + asset statici)  │
   │                                                        │
   │  Pagine HTML statiche (Astro)  ← SEO, velocità         │
   │  Configuratore (isola JS)      ← prezzo, pdf.js        │
   │                                                        │
   │  /api/preventivo   ricalcola il prezzo lato server     │
   │  /api/upload       crea URL firmato R2 ──► il browser  │
   │                    carica il PDF direttamente su R2    │
   │  /api/checkout     crea la sessione Stripe Checkout    │
   │  /api/stripe-hook  pagamento OK → ordine in D1 → email │
   │  /ordine/:token    stato ordine per il cliente         │
   │  /admin            pannello laboratorio (CF Access)    │
   └───────┬──────────────┬───────────────┬─────────────────┘
           ▼              ▼               ▼
      R2 (PDF)       D1 (ordini)     Stripe / Resend
   regola: cancella  backup notturno
   dopo 30 giorni    su R2 (Cron)
```

## Scelte tecniche

| Livello | Scelta | Motivo |
|---|---|---|
| Generatore del sito | **Astro** in output statico | HTML puro e velocissimo, ideale per la SEO. Contenuti in Markdown, facili da modificare. JavaScript solo dove serve |
| Linguaggio | TypeScript | Stesso linguaggio per front-end e Worker |
| Dati di prodotto | **Registro VLC** (Google Sheets: Catalogo copertine con codici CP-001…CP-088, Finiture, Listino stampa, Extra e spedizione). Uno script lo esporta in `copertine.json`, `listino.json`, `extra.json` prima della build; `festivi.json` resta nel repository | Chi non programma cambia un prezzo nel foglio. Il sito e il server leggono lo stesso JSON, quindi i prezzi non divergono. Decisione rt2 0002 |
| Prezzo | Calcolato nel browser per mostrarlo e **ricalcolato nel Worker** prima del pagamento | Il prezzo inviato dal browser non va mai preso per buono |
| Conteggio facciate | **pdf.js nel browser**: il numero di facciate si compila da solo appena si sceglie il file | Elimina gli errori di chi scrive il numero a mano. Il laboratorio verifica comunque in produzione |
| Upload | **URL firmato** S3-compatibile verso R2, caricamento diretto dal browser | Nessun limite di dimensione del Worker, nessun costo di banda |
| Pagamento | **Stripe Checkout** ospitato | Carte, Apple Pay, Google Pay e altri metodi attivabili dalla Dashboard (es. PayPal). Il sito non tocca mai i dati di pagamento |
| Ordini | Tabelle D1 `ordini`, `righe_ordine`, `eventi` (stati e tracking). **Non** il foglio «Ordini» del Registro | Dati personali in un database con accesso controllato. Export CSV per Konga e commercialista (vedi migliorie I2–I3) |
| Email | Resend, mittente **ordini@rilegaretesi.it** con SPF, DKIM e DMARC (non Gmail), modelli in HTML semplice | Conferma ordine, file ricevuto, spedito con tracking, pronto per il ritiro, richiesta di recensione |
| Pannello | `/admin` protetto da **Cloudflare Access**: login con email e codice monouso, nessuna password da gestire | Lista ordini, download PDF, cambio stato, inserimento tracking, export CSV |
| Anti-spam | Turnstile sul modulo contatti e sull'upload | Gratis e senza cookie di profilazione |
| Statistiche | Cloudflare Web Analytics + Google Search Console | Nessun cookie, quindi **nessun banner cookie** |

## Flusso d'ordine

1. Il cliente configura la copertina, carica il PDF e le facciate vengono contate in automatico. Vede il prezzo totale e la **data di consegna stimata**
2. Sceglie **corriere** oppure **ritiro gratuito in via Voltapaletto**
3. Passa a Stripe e paga
4. Il webhook Stripe registra l'ordine pagato in D1 e invia l'email di conferma con il link allo stato dell'ordine
5. Il laboratorio vede l'ordine nel pannello, scarica il PDF e lavora
6. Imposta «spedito» con il numero di tracking, oppure «pronto per il ritiro»: parte l'email al cliente
7. Dopo 3 giorni dalla consegna parte l'email con il link alla recensione Google
8. Dopo 30 giorni una regola di R2 cancella il PDF

## Dati fiscali

- Al checkout c'è un campo facoltativo «Mi serve la fattura» con CF o P.IVA e SDI o PEC, come prevedono i Termini attuali
- Export mensile CSV degli ordini pagati per il registro dei corrispettivi o per la fattura
- ⚠️ Secondo l'interpello AdE n. 198 del 2019, il commercio elettronico indiretto (vendita a distanza di beni) è esonerato dall'invio telematico dei corrispettivi, ma resta l'annotazione nel registro e la fattura su richiesta. **La normativa va verificata con il commercialista** prima del lancio.

## Sicurezza

Si applicano le schede della [knowledge base di sicurezza web](https://github.com/voltalacarta/documentazione/tree/main/25-sicurezza-web), soprattutto [upload di file](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/03-input-e-output/upload-file.md), [header e CSP](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/04-browser/header-di-sicurezza.md) e la [checklist pre-lancio](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/checklist/pre-lancio.md). Il profilo di progetto si ricava da [profili-di-progetto](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/16-progetti/profili-di-progetto.md): e-commerce con pagamenti esterni e upload di file.

I segreti (chiavi Stripe, Resend, R2) stanno solo nelle variabili cifrate di Cloudflare, **mai nel repository** pubblico `rt2`.

## Repository (struttura indicativa)

```
rilegaretesi/
├── src/content/       pagine e guide in Markdown
├── src/data/          JSON esportati dal Registro VLC + festivi.json
├── scripts/           export-registro.ts (Google Sheets → JSON)
├── src/pages/         template Astro
├── src/components/    Configuratore, AnteprimaCopertina, Calcolatore
├── worker/            API: preventivo, upload, checkout, webhook, admin
├── migrations/        schema D1
├── public/img/        foto copertine (AVIF/WebP)
└── docs/              come si modifica prezzi, testi, foto
```


## Allegato · Valutazione dell'hosting



### Cosa deve fare il sito

Il sito non è una vetrina, ma un **e-commerce con caricamento di file**:

1. Pagine di contenuto veloci e indicizzabili: il traffico sarà **solo organico**
2. Configuratore con prezzo in tempo reale
3. **Caricamento di PDF anche pesanti** (50–200 MB per le tesi con immagini)
4. **Pagamento online** sicuro
5. Registrazione dell'ordine, email automatiche, pannello per il laboratorio
6. Cancellazione dei file dopo 30 giorni, come già promesso nei Termini

Un hosting «solo statico» copre il punto 1, ma non i punti 3–6.

### L'idea di partenza: GitHub Pages + Cloudflare

**GitHub va benissimo per il codice. GitHub Pages invece non si può usare per questo sito.** La documentazione ufficiale di GitHub dice:

> «GitHub Pages is not intended for or allowed to be used as a free web-hosting service to run your online business, e-commerce site […]. GitHub Pages sites shouldn't be used for sensitive transactions like sending passwords or credit card numbers.»

Inoltre GitHub Pages serve **solo file statici**: non gestisce upload, pagamenti, ordini o email. Bisognerebbe comunque appoggiarsi a un altro servizio per la parte dinamica.

**Staging e produzione sono due cose diverse.** La decisione [rt2 0001](https://github.com/voltalacarta/rt2/blob/main/docs/decisioni/0001-nuovo-sito-separato-staging-su-github-pages.md) usa GitHub Pages come **staging** (`voltalacarta.github.io/rt2/`, in `noindex`, senza transazioni). Va bene così, e la stessa decisione prevede già che pagamenti e PDF girino su un servizio esterno. Le **parti dinamiche** si provano sulle anteprime gratuite di Cloudflare. Il **sito in produzione** non può stare su Pages.

**Correzione dell'idea:** il codice sta su GitHub (repository privato, gratuito). **Sito e funzioni girano tutti su Cloudflare**, che si aggiorna da solo a ogni modifica del repository.

### Confronto delle alternative

| Opzione | Uso commerciale | Upload, ordini, backend | Costo tipico | Manutenzione | Giudizio |
|---|---|---|---|---|---|
| **GitHub Pages** | ❌ vietato per e-commerce | ❌ solo statico | 0 € | bassa | **scartata** |
| **Cloudflare** (Workers + R2 + D1) | ✅ ammesso anche sul piano gratuito | ✅ tutto incluso | **0 €**, oppure 5 $/mese con Workers Paid | bassa, nessun server da aggiornare | ⭐ **consigliata** |
| Vercel Hobby | ❌ solo uso personale e non commerciale | ✅ | 0 €, ma il piano Pro costa 20 $/mese | bassa | scartata (Pro troppo caro) |
| Netlify Free | ✅ | parziale (funzioni, storage limitati) | 0 € entro 300 crediti al mese; poi 9–20 $ | bassa | rischiosa: se finiscono i crediti **va in pausa tutto l'account**, magari proprio in sessione di laurea |
| VPS (Hetzner, Aruba, OVH…) | ✅ | ✅ | pochi €/mese | **alta**: aggiornamenti, sicurezza, backup a carico vostro | sconsigliata |
| Shopify o SaaS e-commerce | ✅ | upload PDF e prezzo per facciata solo con app a pagamento | decine di €/mese + app | bassa | troppo caro e rigido per un configuratore così specifico |
| WordPress attuale | ✅ | ✅ | hosting + plugin + licenze | media-alta | da abbandonare (vostra decisione) |

### Perché Cloudflare

| Esigenza | Servizio Cloudflare | Limite gratuito (2026) |
|---|---|---|
| Pagine del sito | **Workers con asset statici** (oggi è la strada consigliata per i nuovi progetti, al posto di Pages) | richieste ai file statici illimitate |
| API (prezzo, ordini, webhook) | **Workers** | 100.000 richieste al giorno, CPU breve per richiesta |
| PDF delle tesi | **R2** (storage di oggetti) | **10 GB**, 1 milione di scritture e 10 milioni di letture al mese, **download gratuiti** |
| Database ordini | **D1** (SQLite) | 5 GB, 5 milioni di righe lette e 100.000 scritte al giorno |
| Pannello del laboratorio protetto | **Cloudflare Access** (Zero Trust) | gratis fino a 50 utenti |
| Anti-spam sui moduli | **Turnstile** | gratis |
| Statistiche senza cookie | **Web Analytics** | gratis |
| Email in arrivo su info@ | **Email Routing** (inoltro alla casella attuale) | gratis |
| Deploy da GitHub | **Workers Builds** collegato al repository | incluso |

**Stima del carico:** in un giorno di punta con 100 visitatori e 30 ordini si arriva a poche migliaia di richieste, cioè circa il 2–5% del limite giornaliero gratuito. I PDF, se cancellati dopo 30 giorni, occupano qualche GB: con 300 ordini al mese da 20 MB sono circa 6 GB. **Si sta comodamente nel piano gratuito.**

**Quando passare a Workers Paid (5 $ al mese):** se un giorno si superano le 100.000 richieste, oppure se si vuole **controllare sul server il numero di facciate del PDF**. Quel controllo richiede più tempo di calcolo di quanto ne conceda il piano gratuito; il piano Paid include 10 milioni di richieste e 30 milioni di ms di CPU al mese.

### Componenti esterni a Cloudflare

| Funzione | Servizio | Costo |
|---|---|---|
| Pagamenti | **Stripe Checkout**: pagina di pagamento ospitata da Stripe, quindi nessun dato di carta passa dal vostro sito | 1,5% + 0,25 € per le carte europee standard (2,8% + 0,25 € per le premium). Nessun canone mensile |
| Email transazionali | **Resend** | gratis fino a 3.000 al mese e **100 al giorno**. Con circa 3 email per ordine sono circa 33 ordini al giorno; oltre si passa al Pro (20 $/mese) o a un'alternativa |
| Codice | **GitHub**, repository `voltalacarta/rt2` (oggi pubblico: niente segreti nel codice) | gratis |
| Dominio | rilegaretesi.it presso il registrar attuale; si spostano **solo i DNS** su Cloudflare | invariato |

### Rischi e contromisure

| Rischio | Contromisura |
|---|---|
| Dipendenza da un solo fornitore | Il codice è standard (TypeScript, SQLite, API compatibile S3) e resta portabile su altri provider |
| Limite di 100 email al giorno nei picchi | Monitoraggio, poi piano a pagamento o secondo provider solo quando serve |
| Sito scritto «in casa», quindi qualcuno deve mantenerlo | Stack piccolo, repository documentato, nessun plugin da aggiornare. Le modifiche di testo si fanno nei file Markdown |
| Upload lenti o interrotti | Caricamento diretto su R2 con URL firmato e barra di avanzamento. Possibile anche l'invio successivo via link |
