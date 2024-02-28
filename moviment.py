posicion_asterisco = 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * posicion_asterisco + "*")
    movimiento = input("Presiona 'a' para mover el asterisco a la izquierda, 'd' para moverlo a la derecha, o 'q' para salir: ")
    
    if movimiento == 'a':
        posicion_asterisco = max(0, posicion_asterisco - 1)
    elif movimiento == 'd':
        posicion_asterisco = min(20, posicion_asterisco + 1)
    elif movimiento == 'q':
        break
