// Configuratore: anteprima della copertina e prezzo calcolato dal catalogo.
(function () {
  var form = document.getElementById("configuratore");
  var libro = document.getElementById("libro-conf");
  var $ = function (id) { return document.getElementById(id); };
  var dati = null;
  var perCodice = {};

  fetch("assets/catalogo.json")
    .then(function (r) { return r.json(); })
    .then(function (d) {
      dati = d;
      d.copertine.forEach(function (c) { perCodice[c.codice] = c; });
      preseleziona();
      aggiorna();
    });

  function preseleziona() {
    var codice = new URLSearchParams(location.search).get("copertina");
    var input = codice && form.querySelector('input[name="copertina"][value="' + codice + '"]');
    if (input) {
      input.checked = true;
      input.closest(".tessera").scrollIntoView({ block: "nearest" });
    }
  }

  function scelto(nome) {
    var el = form.querySelector('input[name="' + nome + '"]:checked');
    return el ? el.value : null;
  }

  function prezzoStampa(facciate) {
    for (var i = 0; i < dati.stampa.length; i++) {
      var s = dati.stampa[i];
      if (facciate >= s.da && facciate <= s.a) return s.prezzo;
    }
    return null;
  }

  function aggiorna() {
    if (!dati) return;
    var c = perCodice[scelto("copertina")];
    var decoro = $("decoro").checked;
    var facciate = parseInt($("facciate").value, 10);
    var copie = Math.min(50, Math.max(1, parseInt($("copie").value, 10) || 1));
    var max = dati.stampa[dati.stampa.length - 1].a;

    Libro.copertina(libro, { colore: c.colore, finitura: Libro.classeFinitura(c.finitura), nome: c.nome, prezzo: Libro.euro(c.prezzo) });
    Libro.decoro(libro, decoro);
    $("riga-decoro").hidden = !decoro;
    $("conto-copertina").textContent = Libro.euro(c.prezzo);
    $("conto-copie").textContent = copie;

    var stampa = facciate > 0 ? prezzoStampa(facciate) : null;
    var riepilogo = $("riepilogo");
    if (stampa === null) {
      $("conto-stampa").textContent = "—";
      $("conto-copia").textContent = "—";
      $("conto-totale").textContent = "—";
      $("barra-totale").textContent = "—";
      riepilogo.textContent = facciate > max
        ? "Oltre " + max + " facciate facciamo un preventivo su misura: scrivici a info@rilegaretesi.it."
        : "Indica il numero di facciate per vedere il totale.";
      return;
    }
    var copia = c.prezzo + (decoro ? dati.decoro.prezzo : 0) + stampa;
    var totale = copia * copie + dati.spedizione.prezzo;
    $("conto-stampa").textContent = Libro.euro(stampa);
    $("conto-copia").textContent = Libro.euro(copia);
    $("conto-totale").textContent = Libro.euro(totale);
    $("barra-totale").textContent = Libro.euro(totale);
    riepilogo.textContent = copie + (copie === 1 ? " copia" : " copie") + " in " + c.nome + ", " + facciate + " facciate: " +
      Libro.euro(totale) + " spedizione compresa.";
  }

  // Filtri della griglia
  var filtroFinitura = "";
  function filtra() {
    var famiglia = $("filtro-famiglia").value;
    var visibili = 0;
    form.querySelectorAll(".tessera").forEach(function (t) {
      var ok = (!filtroFinitura || t.dataset.finitura === filtroFinitura) && (!famiglia || t.dataset.famiglia === famiglia);
      t.hidden = !ok;
      if (ok) visibili++;
    });
    $("griglia-vuota").hidden = visibili > 0;
  }
  form.querySelectorAll(".filtro").forEach(function (b) {
    b.addEventListener("click", function () {
      filtroFinitura = b.dataset.valore;
      form.querySelectorAll(".filtro").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      filtra();
    });
  });
  $("filtro-famiglia").addEventListener("change", filtra);
  $("azzera-filtri").addEventListener("click", function () {
    filtroFinitura = "";
    $("filtro-famiglia").value = "";
    form.querySelectorAll(".filtro").forEach(function (x, i) { x.setAttribute("aria-pressed", i === 0 ? "true" : "false"); });
    filtra();
  });

  // Scritta e anteprima dei testi
  form.querySelectorAll('input[name="testo"]').forEach(function (r) {
    r.addEventListener("change", function () { Libro.scritta(libro, r.dataset.colore); });
  });
  form.querySelectorAll("[data-anteprima]").forEach(function (input) {
    input.addEventListener("input", function () {
      Libro.testo(libro, input.dataset.anteprima, input.value, input.placeholder);
    });
  });

  // Copie
  form.querySelectorAll("[data-copie]").forEach(function (b) {
    b.addEventListener("click", function () {
      var n = (parseInt($("copie").value, 10) || 1) + parseInt(b.dataset.copie, 10);
      $("copie").value = Math.min(50, Math.max(1, n));
      aggiorna();
    });
  });

  form.addEventListener("change", aggiorna);
  form.addEventListener("input", aggiorna);

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var facciate = $("facciate");
    if (!(parseInt(facciate.value, 10) > 0)) {
      facciate.setAttribute("aria-invalid", "true");
      facciate.focus();
      $("riepilogo").textContent = "Manca il numero di facciate: lo trovi nel tuo PDF.";
      return;
    }
    facciate.removeAttribute("aria-invalid");
    var avviso = $("avviso-staging");
    if (avviso) avviso.hidden = false;
  });
})();
