while True:
    print("\nMENÚ PRINCIPAL:\n")
    print("Benvinguts a pycalc, introduiu una de les següents opcions:")
    print("0. Sortir")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcio = input("Introdueix la opció desitjada: ")

    if opcio == "0":
        print("Adéu!")
        break

    if opcio == "1":
        num1 = float(input("Introdueix el primer número: "))
        num2 = float(input("Introdueix el segon número: "))
        resultat = num1 + num2
        print(f"La suma de {num1} + {num2} és: {resultat}")             

    if opcio == "2":
        num1 = float(input("Introdueix el primer número: "))
        num2 = float(input("Introdueix el segon número: "))
        resultat = num1 - num2
        print(f"La resta de {num1} - {num2} és: {resultat}")

    if opcio == "3":
        num1 = float(input("Introdueix el primer número: "))
        num2 = float(input("Introdueix el segon número: "))
        resultat = num1 * num2
        print(f"La multiplicació de {num1} * {num2} és: {resultat}")

    if opcio == "4":
        num1 = float(input("Introdueix el primer número: "))
        num2 = float(input("Introdueix el segon número: "))
        if num2 != 0:
            resultat = num1 / num2
            print(f"La divisió de {num1} / {num2} és: {resultat}")
        
    
