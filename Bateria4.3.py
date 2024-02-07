def sumar_imparells():
    try:
        num = int(input("Introdueix un nombre: "))
        suma = 0
        
        # Iterar des de 1 fins al nombre introduït, incrementant de 2 en 2 per assegurar que només s'afegeixen nombres imparells
        for i in range(1, num + 1, 2):
            suma += i
        
        print("La suma dels números imparells entre 1 i", num, "és:", suma)
    
    except ValueError:
        print("Si us plau, introdueix un nombre vàlid.")


# Cridar la funció per sumar els números imparells
sumar_imparells()
