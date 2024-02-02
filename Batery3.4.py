numero = int(input("introdueix un número: "))
tipus_suma = input("Vols sumar números parells (P) o senars (S)? ").upper()
if tipus_suma == "P":
    suma_resultat = sum(range(2, numero + 1, 2))
    tipus_resultat = "parells"
elif tipus_suma == "S":
    suma_resultat = sum(range(1, numero + 1, 2))
    tipus_resultat = "senars"
else:
    suma_resultat = 0
    tipus_resultat = "invalid"

if tipus_resultat != "invalid":
    print(f"La suma dels números {tipus_resultat} fins a {numero} és: {suma_resultat}")
else:
    print("Opció no vàlid, si us plau, selecciona 'P' per parells o 'S' per senars.")
