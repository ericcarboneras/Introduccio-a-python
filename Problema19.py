def suma_numeros():
    numeros = []
    
    while True:
        entrada = input("Introdueix un número sencer (o 'final' per acabar): ")
        
        if entrada.lower() == 'final':
            break
        
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Si us plau, introdueix només números sencers o 'final'.")
    
    return sum(numeros)

resultat = suma_numeros()
print("La suma dels números introduïts és:", resultat)
