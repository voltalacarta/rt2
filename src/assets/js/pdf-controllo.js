// Controllo del PDF nel browser con pdf.js: facciate, formato, pagine bianche, frontespizio.
// Il file non lascia il dispositivo. pdf.js si carica solo quando serve.

const MAX_CONTROLLO_BIANCHE = 600;

async function caricaPdfjs() {
  const pdfjs = await import("../vendor/pdfjs/pdf.mjs");
  pdfjs.GlobalWorkerOptions.workerSrc = new URL("../vendor/pdfjs/pdf.worker.mjs", import.meta.url).href;
  return pdfjs;
}

async function eUnPdf(file) {
  const testa = new Uint8Array(await file.slice(0, 5).arrayBuffer());
  return String.fromCharCode(...testa) === "%PDF-";
}

function eA4(w, h) {
  const [a, b] = w < h ? [w, h] : [h, w];
  return Math.abs(a - 595) < 12 && Math.abs(b - 842) < 12;
}

// Una pagina è bianca se non ha testo e, ridotta a miniatura, quasi tutti i pixel sono chiari.
// Il controllo del testo evita di segnalare pagine quasi vuote ma volute, come una dedica.
async function paginaBianca(pagina, canvas) {
  const testo = await pagina.getTextContent();
  if (testo.items.some((it) => (it.str || "").trim())) return false;
  const vista = pagina.getViewport({ scale: 150 / pagina.getViewport({ scale: 1 }).width });
  canvas.width = Math.ceil(vista.width);
  canvas.height = Math.ceil(vista.height);
  const ctx = canvas.getContext("2d", { willReadFrequently: true });
  ctx.fillStyle = "#fff";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  await pagina.render({ canvasContext: ctx, viewport: vista }).promise;
  const px = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
  let scuri = 0;
  for (let i = 0; i < px.length; i += 4) {
    if (px[i] + px[i + 1] + px[i + 2] < 690) scuri++;
  }
  return scuri / (px.length / 4) < 0.0005;
}

// Il titolo è di solito la riga con il carattere più grande del frontespizio.
async function titoloProbabile(pagina) {
  const testo = await pagina.getTextContent();
  const righe = new Map();
  for (const it of testo.items) {
    const s = (it.str || "").trim();
    if (!s) continue;
    const alt = Math.round(Math.abs(it.transform[3]));
    const y = Math.round(it.transform[5]);
    const chiave = alt + ":" + y;
    righe.set(chiave, ((righe.get(chiave) || "") + " " + s).trim());
  }
  let max = 0;
  for (const k of righe.keys()) max = Math.max(max, Number(k.split(":")[0]));
  const titolo = [...righe.entries()]
    .filter(([k]) => Number(k.split(":")[0]) === max)
    .sort((a, b) => Number(b[0].split(":")[1]) - Number(a[0].split(":")[1]))
    .map(([, v]) => v)
    .join(" ");
  return titolo.length >= 4 && titolo.length <= 160 ? titolo : "";
}

async function analizza(file, avanzamento) {
  if (!(await eUnPdf(file))) return { errore: "non-pdf" };
  const pdfjs = await caricaPdfjs();
  const doc = await pdfjs.getDocument({ data: await file.arrayBuffer(), isEvalSupported: false }).promise;
  const n = doc.numPages;
  const esito = { facciate: n, nonA4: [], orizzontali: [], bianche: [], bianchiControllati: n <= MAX_CONTROLLO_BIANCHE, titolo: "" };

  const prima = await doc.getPage(1);
  const v = prima.getViewport({ scale: 1 });
  const fronte = document.getElementById("frontespizio");
  const scala = fronte.width / v.width;
  fronte.height = Math.round(v.height * scala);
  const ctx = fronte.getContext("2d");
  ctx.fillStyle = "#fff";
  ctx.fillRect(0, 0, fronte.width, fronte.height);
  await prima.render({ canvasContext: ctx, viewport: prima.getViewport({ scale: scala }) }).promise;
  esito.titolo = await titoloProbabile(prima);

  const tela = document.createElement("canvas");
  for (let i = 1; i <= n; i++) {
    const p = i === 1 ? prima : await doc.getPage(i);
    const vp = p.getViewport({ scale: 1 });
    if (!eA4(vp.width, vp.height)) esito.nonA4.push(i);
    if (vp.width > vp.height) esito.orizzontali.push(i);
    if (esito.bianchiControllati && i > 1 && (await paginaBianca(p, tela))) esito.bianche.push(i);
    p.cleanup();
    if (avanzamento && (i % 10 === 0 || i === n)) avanzamento(i, n);
  }
  await doc.destroy();
  return esito;
}

window.ControlloPDF = { analizza };
window.dispatchEvent(new Event("controllo-pdf-pronto"));
