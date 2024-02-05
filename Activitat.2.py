<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Taula de Multiplicar</title>
    <script>
        function generarTaula() {
            var num = document.getElementById("numero").value;
            var taula = "<h2>Taula de Multiplicar del " + num + "</h2><ul>";

            for (var i = 1; i <= 10; i++) {
                var resultat = num * i;
                taula += "<li>" + num + " x " + i + " = " + resultat + "</li>";
            }

            taula += "</ul>";
            document.getElementById("resultat").innerHTML = taula;
        }
    </script>
</head>
<body>
    <label for="numero">Introdueix un número:</label>
    <input type="number" id="numero">
    <button onclick="generarTaula()">Generar Taula</button>
    <div id="resultat"></div>
</body>
</html>
