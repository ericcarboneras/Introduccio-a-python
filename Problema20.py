parells = []
senars = []

while True:
    entrada = input("Introdueix un número sencer (o 'final' per acabar): ")
    
    if entrada.lower() == 'final':
        break
    
    try:
        numero = int(entrada)
        (parells if numero % 2 == 0 else senars).append(numero)
    except ValueError:
        print("Si us plau, introdueix només números sencers o 'final'.")

if parells:
    print("Els números parells són:", parells, "Màxim:", max(parells), "Mínim:", min(parells))
else:
    print("No s'han introduït números parells.")

if senars:
    print("Els números senars són:", senars, "Màxim:", max(senars), "Mínim:", min(senars))
else:
    print("No s'han introduït números senars.")
