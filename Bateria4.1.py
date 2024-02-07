def calcular_divisors():
    try:
        # Demanar a l'usuari que introdueixi un nombre
        num = int(input("Introdueix un nombre: "))
        
        # Inicialitzar una llista per emmagatzemar els divisors
        divisors = []
        
        # Iterar des de 1 fins al nombre introduït
        for i in range(1, num + 1):
            # Comprovar si el nombre és divisible per 'i' sense residu
            if num % i == 0:
                divisors.append(i)
        
        # Mostrar els divisors
        print("Els divisors de", num, "són:", divisors)
    
    except ValueError:
        print("Si us plau, introdueix un nombre vàlid.")


# Cridar la funció per calcular els divisors
calcular_divisors()
