// Interruttore di stile della barra di prova: Legatoria o Studio.
(function () {
  var html = document.documentElement;
  var bottoni = document.querySelectorAll("[data-tema]");
  function segna() {
    bottoni.forEach(function (b) {
      b.setAttribute("aria-pressed", b.dataset.tema === html.dataset.theme ? "true" : "false");
    });
  }
  bottoni.forEach(function (b) {
    b.addEventListener("click", function () {
      html.dataset.theme = b.dataset.tema;
      try { localStorage.setItem("rt-tema", b.dataset.tema); } catch (e) {}
      segna();
    });
  });
  segna();
})();
