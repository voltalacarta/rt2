---
titolo: "Migliorie per il nuovo sito (solo traffico organico)"
stato: proposto
creato: 2026-10-24
aggiornato: 2026-10-24
tag: [sito, migliorie, seo]
sintesi: "Elenco prioritizzato: SEO tecnica, contenuti, conversione, fiducia, recensioni, gestione, conformità 2026, integrazione con Registro VLC e Konga."
---

# Migliorie per il nuovo rilegaretesi.it

Versione pubblica senza le parti commerciali riservate. Versione completa nel second brain (privato): `10-progetti/info-pubbliche/07-nuovo-sito/migliorie.md`.

**Il vincolo:** niente pubblicità, solo traffico organico. Il sito deve quindi **farsi trovare**, **convincere** chi arriva e **generare recensioni e passaparola**.

Priorità: **P1** al lancio · **P2** nei 2–3 mesi successivi · **P3** quando c'è tempo

---

## A. Farsi trovare (SEO tecnica)

| # | Miglioria | P | Perché |
|---|---|---|---|
| A1 | Tutte le pagine in **HTML statico indicizzabile**, senza `noindex` sulle pagine commerciali | P1 | Oggi la pagina dove si compra è esclusa da Google |
| A2 | `<title>` e meta description **unici e veritieri** per ogni pagina, con brand e città | P1 | Oggi sono vuoti («Tesi rigide -») o fuorvianti («spedizione gratuita, 24 ore») |
| A3 | **Redirect 301** dai vecchi URL WordPress (`/prodotto/tesi/`, `/faq/`, `/spedizioni/`…) e dalle vecchie pagine tesi di voltalacarta.it | P1 | Si recupera il poco valore accumulato ed evita contenuti in concorrenza tra loro |
| A4 | `sitemap.xml`, `robots.txt`, canonical, invio a **Google Search Console** e Bing Webmaster | P1 | Indicizzazione rapida e monitoraggio gratuito delle ricerche |
| A5 | Dati strutturati: **LocalBusiness** (Volta la carta, indirizzo, orari), **Organization**, **Product + Offer** per ogni linea, **BreadcrumbList** | P1 | Prezzi e scheda azienda leggibili da Google |
| A6 | **Velocità**: obiettivo LCP sotto 1,5 s su mobile, immagini AVIF/WebP, nessuna libreria pesante | P1 | La velocità è un fattore di ranking, e un sito statico ha un vantaggio su WordPress con Elementor |
| A7 | Nomi file e **testi alternativi delle foto** descrittivi («tesi-copertina-rigida-effetto-pelle-blu.avif») | P1 | Traffico da Google Immagini, molto usato per scegliere il colore |
| A8 | URL parlanti in italiano (`/copertine/effetto-pelle/`, `/guide/impaginazione-fronte-retro/`) | P1 | Chiarezza e SEO |
| A9 | **Link interni** tra guide, copertine e configuratore. Link da voltalacarta.it e viceversa | P1 | Distribuisce l'autorità tra le pagine |

## B. Contenuti che portano traffico (SEO di contenuto)

Le pagine elencate sono quelle con domanda di ricerca reale e poca concorrenza locale. Ognuna deve essere **utile davvero**, non un doppione della home.

| # | Pagina | P | Parola chiave obiettivo |
|---|---|---|---|
| B1 | **Rilegatura tesi a Ferrara**: ritiro in negozio, orari, mappa, foto della bottega | P1 | «rilegatura tesi Ferrara», «stampa tesi Ferrara», «tesi Unife» |
| B2 | **Tesi a colori allo stesso prezzo del bianco e nero**, con un calcolatore che confronta le due opzioni | P1 | «stampa tesi a colori prezzo». |
| B3 | **Perché artigianale**: colla a freddo, scanalatura, rifilo, capitello, incisione, con foto macro | P1 | «tesi rilegata a mano», «tesi artigianale». È il vostro vantaggio unico |
| B4 | **Galleria copertine**: una pagina per ognuna delle 10 finiture con tutte le varianti fotografate | P1 | «tesi copertina bordeaux», «tesi effetto pelle blu»… (long tail) |
| B5 | **Tesi floreali**, con foto e storia del decoro esclusivo | P1 | «tesi copertina floreale» |
| B6 | **Prezzi**: listino completo e trasparente, con esempi concreti | P1 | «quanto costa rilegare una tesi» |
| B7 | **Chi siamo**: storia dal 1999, oltre 50.000 tesi, la bottega, referenze (messale papale, libro firme) | P1 | fiducia e ricerche sul brand |
| B8 | **Guide pratiche**: impaginazione fronte/retro, margini, pagine bianche, esportare il PDF da Word, Google Docs e LaTeX, frontespizio, quante copie servono, quando ordinare rispetto alla data di laurea | P2 | domande ricorrenti degli studenti. Il contenuto esiste già nelle FAQ, va espanso |
| B9 | **Frontespizio per ateneo** (Unife prima di tutto, poi Bologna, Padova, Modena e altri), con link ai modelli ufficiali e un esempio di come appare in copertina | P2 | «frontespizio tesi Unife». Va fatto solo per gli atenei dove c'è un contenuto vero da offrire |
| B10 | **Materiali speciali** (legno, sughero, plexiglass, carbonio) con modulo di preventivo | P2 | «tesi in legno», nicchia ad alto margine |
| B11 | **Tesi leggere** con prezzo visibile, come fascia d'ingresso | P1 | chi cerca il prezzo più basso |
| B12 | Pagina **Recensioni**, solo recensioni vere e raccolte con consenso | P2 | prova sociale |

## C. Convincere chi arriva (conversione)

| # | Miglioria | P | Perché |
|---|---|---|---|
| C1 | **Conteggio automatico delle facciate** dal PDF caricato | P1 | Meno errori e meno passaggi. Nessun concorrente esaminato lo comunica |
| C2 | **Prezzo totale sempre visibile**, spedizione compresa, fin dal primo passaggio | P1 | Il cliente confronta i totali, non i prezzi «a partire da» |
| C3 | **Data di consegna stimata** calcolata sul momento («ordina entro le 12:00 → consegna prevista giovedì 29»), con festivi e cut-off | P1 | Per chi si laurea a breve il dubbio principale è la data |
| C4 | **Ritiro gratuito in negozio** a Ferrara come opzione di consegna | P1 | Costo zero, vantaggio unico sugli studenti Unife, porta clienti in bottega |
| C5 | **Anteprima della copertina** con colore, scritta e frontespizio estratto dal PDF | P2 | Rassicura e riduce gli errori. MisterTesi ha già un'anteprima |
| C6 | **Controlli automatici sul PDF** prima del pagamento: formato A4, pagine orizzontali, facciate dispari con fronte/retro, frontespizio presente | P2 | Recupera il servizio «controlliamo il tuo file», oggi perso |
| C7 | Opzione **«Controllate il mio file prima di stampare»**, gratuita o simbolica, con qualche ora in più | P2 | È il vantaggio di una bottega vera rispetto a una stampa automatica |
| C8 | **Apple Pay, Google Pay, PayPal** tramite Stripe Checkout | P1 | Più metodi, meno carrelli abbandonati. Oggi accettate solo carte |
| C9 | **WhatsApp** (link click-to-chat al numero aziendale) e **telefono** visibili | P1 | I concorrenti li hanno. Oggi c'è solo l'email |
| C10 | **Pagina stato ordine** raggiungibile dal link nell'email, senza account | P1 | Meno email «a che punto è la mia tesi?» |
| C11 | Sconto automatico sulle **copie aggiuntive** (la seconda copia costa meno) | P2 | Alza lo scontrino medio. La lavorazione delle copie in serie costa meno |
| C12 | **Garanzia esplicita**: «Se c'è un difetto di lavorazione la rifacciamo gratis» | P1 | Fiducia. Va scritta in accordo con la revisione dei Termini |
| C13 | Configuratore **pensato per lo smartphone** | P1 | Molti studenti hanno il PDF sul telefono |
| C14 | **Riprendi l'ordine più tardi**: salvataggio della configurazione con link via email | P3 | Per chi aspetta la versione finale della tesi |

## D. Fiducia

| # | Miglioria | P |
|---|---|---|
| D1 | Indirizzo, telefono, P.IVA, orari in **ogni pagina** (footer) | P1 |
| D2 | **Foto reali**: bottega, mani al lavoro, dettagli di capitello e scanalatura. Niente immagini di stock | P1 |
| D3 | **Video breve** (30–60 secondi) della lavorazione, ospitato su YouTube e inserito nel sito: è anche contenuto social | P2 |
| D4 | Referenze (messale papale, libro firme Mattarella, dal 1999, oltre 50.000 tesi) in home e in Chi siamo, con formulazione verificata | P1 |
| D5 | Numeri coerenti su tutti i canali | P1 |

## E. Generare recensioni e passaparola (organico fuori dal sito)

| # | Miglioria | P | Perché |
|---|---|---|---|
| E1 | **Google Business Profile** completo: categoria «Legatoria» e «Servizio di stampa», link a rilegaretesi.it, foto, orari, prodotti | P1 | Gratuito. Porta le ricerche locali e Maps |
| E2 | **Email automatica di richiesta recensione** 3 giorni dopo la consegna o il ritiro, con link diretto alle recensioni Google | P1 | I leader del settore raccolgono migliaia di recensioni chiedendole in automatico. Google è gratuito e aiuta anche la SEO locale |
| E3 | Biglietto nel pacco con QR per la recensione e invito a taggarvi su Instagram il giorno della laurea | P1 | Costa pochi centesimi |
| E4 | **Instagram o TikTok**: copertine abbinate all'abito, prima/dopo, lavorazione, repost degli studenti | P2 | Il canale da cui oggi parte la domanda (articolo del 2024) |
| E5 | **Codice amico**: sconto a chi porta un compagno di corso | P2 | I laureandi della stessa sessione si conoscono tra loro |
| E6 | Correggere le **directory** (Coobiz con il vecchio indirizzo, Yelp) e aggiungere ovunque il sito | P1 | Coerenza dei dati per la SEO locale |
| E7 | Contatti con **associazioni studentesche Unife** e rappresentanti, per convenzioni o volantini nei periodi di laurea | P2 | Link e passaparola locali |
| E8 | Link da **voltalacarta.it** (home e footer) | P1 | Backlink immediato dal vostro dominio più vecchio |

## G. Gestione e conformità

| # | Miglioria | P |
|---|---|---|
| G1 | **Pannello ordini** con stati, tracking, download PDF ed export CSV | P1 |
| G2 | Email automatiche per ogni cambio di stato | P1 |
| G3 | Cancellazione automatica dei PDF dopo 30 giorni, come previsto dai Termini | P1 |
| G4 | Backup notturno del database | P1 |
| G5 | **Revisione legale dei Termini** (rischio di trasporto, termine reclami) e privacy aggiornata con i nuovi fornitori (Cloudflare, Stripe, Resend) | P1 |
| G6 | Nessun cookie di profilazione, quindi nessun banner | P1 |
| G7 | Verifica degli obblighi fiscali con il commercialista (corrispettivi e fattura su richiesta) | P1 |
| G8 | **Accessibilità** (contrasto, tastiera, etichette): l'EAA esenta le microimprese, ma migliora la SEO e l'usabilità e costa poco se fatta dall'inizio | P2 |

## H. Conformità normativa 2026 (aggiunta del 24/10/2026)

Fonte: [guida-ecommerce](https://github.com/voltalacarta/second-brain/blob/main/10-progetti/guida-ecommerce/01-normativa/00-calendario-scadenze.md) del second brain. Sono **obblighi già in vigore**: valgono anche per il sito WordPress attuale finché resta online.

| # | Miglioria | P | Norma e riferimento |
|---|---|---|---|
| H1 | **Nessun tracker senza consenso.** Nel nuovo sito non si usano proprio (Cloudflare Web Analytics è senza cookie), quindi niente banner | P1 | GDPR e cookie → [03-privacy](https://github.com/voltalacarta/second-brain/blob/main/10-progetti/guida-ecommerce/01-normativa/03-privacy-gdpr-cookie.md) |
| H2 | **Claim ambientali.** «Materiali sostenibili» e «totalmente plastic free» vanno resi **specifici e documentati** (quale materiale, quale certificazione, quale parte del prodotto), oppure tolti | P1 | D.Lgs. 30/2026, in vigore dal **27/09/2026** → [06-green-claims](https://github.com/voltalacarta/second-brain/blob/main/10-progetti/guida-ecommerce/01-normativa/06-green-claims-greenwashing.md) |
| H3 | **Togliere il link alla piattaforma ODR** da Termini, pagine ed email | P1 | Reg. (UE) 2024/3228, piattaforma chiusa dal 20/07/2025 → [10-controversie](https://github.com/voltalacarta/second-brain/blob/main/10-progetti/guida-ecommerce/01-normativa/10-controversie-adr.md) |
| H4 | **Recesso:** dire chiaramente che è escluso per le tesi personalizzate (art. 59). Valutare con il legale se serve comunque la **funzione di recesso digitale** (art. 54-bis) per ciò che non è su misura, come copie non personalizzate o libri. Se serve, si fa in due passaggi con ricevuta email | P1 | D.Lgs. 209/2025, dal 19/06/2026 → [01-recesso](https://github.com/voltalacarta/second-brain/blob/main/10-progetti/guida-ecommerce/01-normativa/01-codice-consumo-recesso.md) |
| H5 | **Recensioni:** spiegare come vengono verificate (solo clienti con ordine reale); nessun filtro delle negative. **Sconti** (codice amico, seconda copia) senza prezzi barrati falsi: vale la regola del prezzo più basso a 30 giorni | P1 | Omnibus → [02-prezzi](https://github.com/voltalacarta/second-brain/blob/main/10-progetti/guida-ecommerce/01-normativa/02-prezzi-promozioni-recensioni.md) |
| H6 | **Dati del fabbricante** (Volta la carta, indirizzo, email) in ogni scheda prodotto | P1 | GPSR → [05-gpsr](https://github.com/voltalacarta/second-brain/blob/main/10-progetti/guida-ecommerce/01-normativa/05-sicurezza-prodotti-gpsr.md) |
| H7 | **Pagine legali complete** (identità, prezzi totali, consegna, garanzia legale, reclami) | P1 | → [06-pagine-legali](https://github.com/voltalacarta/second-brain/blob/main/10-progetti/guida-ecommerce/02-sito-web/06-pagine-legali-obbligatorie.md) e [checklist conformità](https://github.com/voltalacarta/second-brain/blob/main/10-progetti/guida-ecommerce/05-checklist/checklist-conformita-legale.md) |
| H8 | **Email dal dominio** (`ordini@rilegaretesi.it`) invece di Gmail, con SPF, DKIM e DMARC | P1 | Consegna delle email e protezione dalle imitazioni → [quadro e piano](https://github.com/voltalacarta/second-brain/blob/main/10-progetti/guida-ecommerce/00-profilo-azienda/quadro-e-piano.md), punto 8 |

## I. Integrazione con il resto di Volta la carta (aggiunta del 24/10/2026)

| # | Miglioria | P | Collegamento |
|---|---|---|---|
| I1 | **Catalogo e listino dal Registro VLC** (Google Sheets): uno script li esporta in JSON prima di ogni build. Chi non programma cambia un prezzo nel foglio e il sito si aggiorna | P1 | Decisione rt2 [0002](https://github.com/voltalacarta/rt2/blob/main/docs/decisioni/0002-sito-statico-con-astro-e-catalogo-dal-registro-vlc.md) |
| I2 | **Ordini nel database del sito (D1), non nel foglio «Ordini» del Registro.** Il foglio contiene nome, email e telefono dei clienti: più rischi privacy e nessun controllo sugli accessi. Al massimo si sincronizza un riepilogo senza dati personali | P1 | [25-sicurezza-web · dati e segreti](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/05-crittografia/dati-e-segreti.md) |
| I3 | **Riepilogo mensile per Konga:** export CSV degli ordini pagati, diviso per aliquota (tesi = servizi 22%) e per strumento di pagamento, da copiare nei corrispettivi. Richieste di fattura con CF/P.IVA e SDI/PEC | P1 | [Flusso 01 ordine → Konga](https://github.com/voltalacarta/second-brain/blob/main/10-progetti/info-economiche/04-automazione/flussi/01-ordine-online-a-konga.md) |
| I4 | **Metadati Stripe** (`order_id`, tipologia, aliquota) su ogni pagamento, così la riconciliazione notturna funziona senza abbinamenti a mano | P1 | [Stripe webhook](https://github.com/voltalacarta/second-brain/blob/main/10-progetti/info-economiche/04-automazione/codice/stripe-webhook.md) |
| I5 | **Upload dei PDF secondo la scheda di sicurezza:** solo PDF veri (controllo dei magic bytes, non dell'estensione), dimensione massima, nomi file generati dal server, bucket privato, link di download a scadenza | P1 | [Upload e gestione dei file](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/03-input-e-output/upload-file.md) |
| I6 | **Header di sicurezza e CSP**, `security.txt`, Turnstile e rate limiting sulle API | P1 | [Header di sicurezza](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/04-browser/header-di-sicurezza.md) · [modello security.txt](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/15-modelli/security.txt) |
| I7 | **Due checklist prima del lancio:** quella di sicurezza e quella di lancio e-commerce | P1 | [Pre-lancio sicurezza](https://github.com/voltalacarta/documentazione/blob/main/25-sicurezza-web/checklist/pre-lancio.md) · [Checklist lancio sito](https://github.com/voltalacarta/second-brain/blob/main/10-progetti/guida-ecommerce/05-checklist/checklist-lancio-sito.md) |
| I8 | **Rispondere alle domande aperte del Registro** (foglio «Da verificare»): seconda copia, prezzi delle tesi leggere e floreali, costo del fronte/retro, decoro su tutte le copertine, ritiro in negozio, promessa delle 24 ore, metodi di pagamento | P1 | Registro VLC |
| I9 | **Satispay e PayPal:** già indicati nel piano e-commerce come primi metodi da aggiungere se il sito cresce. Da attivare tramite Stripe (Satispay su Stripe è in anteprima privata) o con un conto diretto | P2 | [Pagamenti](https://github.com/voltalacarta/second-brain/blob/main/10-progetti/guida-ecommerce/03-commerce/03-pagamenti.md) |

---

## Le 10 voci che contano di più

1. A1–A3: indicizzazione e redirect
2. B1: Rilegatura tesi Ferrara + C4: ritiro gratuito
3. E1 + E2: Google Business Profile e richiesta automatica di recensioni
4. B3 + D2: pagina «Perché artigianale» con foto vere
5. B2: tesi a colori allo stesso prezzo
6. C1 + C2 + C3: facciate automatiche, totale visibile, data di consegna
7. C8 + C9: più metodi di pagamento, WhatsApp e telefono
8. B4: galleria copertine per finitura
9. G5: revisione dei Termini

**Obblighi già in vigore** (da rispettare dal primo giorno): H1–H3.
