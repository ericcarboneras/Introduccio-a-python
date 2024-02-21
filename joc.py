import random

def dau_6():
    return random.randint(1, 6)

def dau_x(num_cares):
    return random.randint(1, num_cares)

def daus_6(num_daus):
    return [dau_6() for _ in range(num_daus)]

def daus_x(num_daus, num_cares):
    return [dau_x(num_cares) for _ in range(num_daus)]

def mostrar_menu():
    print("Menú:")
    print("1. Llençar un dau de 6 cares.")
    print("2. Llençar més d'un dau de 6 cares.")
    print("3. Llençar un dau de cares definides per usuari.")
    print("4. Llençar més d'un dau de cares definides per usuari.")
    print("5. Sortir.")

def main():
    while True:
        mostrar_menu()
        opcio = input("Escull una opció (1-5): ")
        
        if opcio == '1':
            print("El resultat de la tirada és:", dau_6())
        elif opcio == '2':
            num_daus = int(input("Quants daus vols llençar? "))
            print("Resultats de les tirades dels daus:", daus_6(num_daus))
        elif opcio == '3':
            num_cares = int(input("De quantes cares és el dau? "))
            print("El resultat de la tirada és:", dau_x(num_cares))
        elif opcio == '4':
            num_cares = int(input("De quantes cares és el dau? "))
            num_daus = int(input("Quants daus vols llençar? "))
            print("Resultats de les tirades dels daus:", daus_x(num_daus, num_cares))
        elif opcio == '5':
            print("Adéu!")
            break
        else:
            print("Opció no vàlida. Si us plau, tria una opció vàlida.")

if __name__ == "__main__":
    main()
