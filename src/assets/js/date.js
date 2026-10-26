// Date di spedizione e consegna: giorni lavorativi, festivi, chiusure, ora limite.
window.DateRT = (function () {
  function iso(d) {
    var m = String(d.getMonth() + 1).padStart(2, "0");
    var g = String(d.getDate()).padStart(2, "0");
    return d.getFullYear() + "-" + m + "-" + g;
  }
  function giorno(d) { return new Date(d.getFullYear(), d.getMonth(), d.getDate()); }

  function lavorativo(dati, d) {
    var gs = d.getDay() === 0 ? 7 : d.getDay();
    if (dati.ordini.giorni_lavorativi.indexOf(gs) === -1) return false;
    var s = iso(d);
    if (dati.festivi.indexOf(s) !== -1) return false;
    return !dati.chiusure.some(function (c) { return s >= c.dal && s <= c.al; });
  }

  function prossimoLavorativo(dati, d) {
    var x = giorno(d);
    do { x.setDate(x.getDate() + 1); } while (!lavorativo(dati, x));
    return x;
  }

  // Giorno in cui la tesi è pronta e parte: oggi se è lavorativo e prima dell'ora limite.
  function spedizione(dati, adesso) {
    var oggi = giorno(adesso);
    if (lavorativo(dati, oggi) && adesso.getHours() < dati.ordini.ora_limite) return oggi;
    return prossimoLavorativo(dati, oggi);
  }

  function aggiungiLavorativi(dati, d, n) {
    var x = giorno(d);
    for (var i = 0; i < n; i++) x = prossimoLavorativo(dati, x);
    return x;
  }

  function fmt(d) {
    return d.toLocaleDateString("it-IT", { weekday: "long", day: "numeric", month: "long" });
  }

  return { iso: iso, giorno: giorno, lavorativo: lavorativo, spedizione: spedizione, aggiungiLavorativi: aggiungiLavorativi, fmt: fmt };
})();
