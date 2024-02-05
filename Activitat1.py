<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora Factorial</title>
    <script>
        function calcularFactorial() {
            var num = document.getElementById("numero").value;
            var resultat = 1;

            for (var i = 1; i <= num; i++) {
                resultat *= i;
            }

            document.getElementById("resultat").innerHTML = "El factorial de " + num + " és: " + resultat;
        }
    </script>
</head>
<body>
    <h2>Calculadora Factorial</h2>
    <label for="numero">Introdueix un nombre:</label>
    <input type="number" id="numero">
    <button onclick="calcularFactorial()">Calcular Factorial</button>
    <p id="resultat"></p>
</body>
</html>
