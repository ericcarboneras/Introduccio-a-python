while True:
    try:
        num1 = float(input("Introdueix el primer nombre: "))
        num2 = float(input("Introdueix el segon nombre: "))
        
        result = num1 / num2
        print("El resultat de la divisió és:", result)
        break  
    except:
        print("Error: No es pot dividir per zero")




while True:
    try:
        entrada = input("Introdueix un número: ")
        numero = int(entrada)
        print("Has introduït el número:", numero)
        break  
    except:
        print("Error: La entrada no és un número vàlid, introdueix un número enter")




while True:
    try:
        valor1 = float(input("Introdueix el primer valor: "))
        valor2 = float(input("Introdueix el segon valor: "))
        
        suma = valor1 + valor2
        print("La suma dels dos valors és:", suma)
        break  
    except:
        print("Error: Un o tots dos dels valors no són números vàlids,introdueix dos valors numèrics.")




llista = [1,2,3,4,5]
try:
    index = int(input("Introdueix un índex: "))
    print("L'element corresponent a l'índex", index, "és:", llista[index])
except:
    print("L'índex no existeix a la llista")

    



