const $formularioCurso = document.getElementById("formularioCurso");
const $txtNombre = document.getElementById("txtNombre");

(function () {
  $formularioCurso.addEventListener("submit", function (e) {
    let nombre = String($txtNombre.value).trim();
    if (nombre.length === 0) {
      alert("El nombre de curso no puede ir vacio");
      e.preventDefault();
    }
  });
})();
