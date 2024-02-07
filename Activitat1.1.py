numero_dni = int(input("Introdueix el número del DNI: "))
lletra_dni = input("Introdueix la lletra del DNI: ").upper()

lletres_dni = 'TRWAGMYFPDXBNJZSQVHLCKE'
index = numero_dni % 23
lletra_dni_calculada = lletres_dni[index]

if lletra_dni == lletra_dni_calculada:
    print("El teu DNI és {}{}".format(numero_dni, lletra_dni))
else:
    print("La lletra del DNI introduïda no coincideix amb el càlcul.")
