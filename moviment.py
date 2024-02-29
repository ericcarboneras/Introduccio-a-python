posicio_asterisc = 0
AMPLADA = 20
while True:
    
    cadena_asterisc = ""
    for i in range(AMPLADA+1):
        if posicio_asterisc == i:
            cadena_asterisc += "*"
        else:
            cadena_asterisc += " "
    print(cadena_asterisc)
    moviment = input("")
    if moviment == 'a' and posicio_asterisc > 0:
            posicio_asterisc -= 1
    elif moviment == 'd' and posicio_asterisc < AMPLADA:
            posicio_asterisc += 1
