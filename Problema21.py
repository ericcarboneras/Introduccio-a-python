parells = []
senars = []

while (entrada := input("Introdueix un número sencer (o 'final' per acabar): ")) != 'final':
    try:
        (parells if int(entrada) % 2 == 0 else senars).append(int(entrada))
    except ValueError:
        print("Si us plau, introdueix només números sencers o 'final'.")

print("Els números parells són:", parells)
print("Els números senars són:", senars)
