// Aggiorna l'anteprima della copertina: colore, finitura, colore della scritta, decoro, testi.
window.Libro = {
  copertina: function (libro, c) {
    libro.style.setProperty("--cop", c.colore);
    libro.dataset.finitura = c.finitura;
    var nome = libro.querySelector('[data-campo="copertina"]');
    var prezzo = libro.querySelector('[data-campo="prezzo"]');
    if (nome) nome.textContent = c.nome;
    if (prezzo) prezzo.textContent = c.prezzo;
  },
  scritta: function (libro, colore) {
    libro.style.setProperty("--foil", colore);
  },
  decoro: function (libro, attivo) {
    libro.querySelector(".libro__decoro").toggleAttribute("hidden", !attivo);
  },
  testo: function (libro, campo, valore, predefinito) {
    var el = libro.querySelector('[data-campo="' + campo + '"]');
    if (el) el.textContent = valore.trim() || predefinito;
  },
  euro: function (n) {
    return Number.isInteger(n) ? n + " €" : n.toFixed(2).replace(".", ",") + " €";
  },
  classeFinitura: function (nome) {
    return nome.toLowerCase().replace(/ /g, "-");
  }
};
