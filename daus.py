import random
def tirada_dau():
    return random.randint(1, 6)
def main():
    input("Premi Enter per fer una tirada de dau...")
    resultat = tirada_dado()
    print("El resultat de la tirada és:", resultat)
tirada_dau()




import random
def dau_6():
    return random.randint(1, 6)
resultat_tirada = dau_6()
print("El resultat de la tirada és:", resultat_tirada)
 dau_6()




import random
def daus_6():
    num_daus = int(input("Quants daus vols llençar? "))
    resultats = [random.randint(1, 6) for _ in range(num_daus)]
    print("Resultats de les tirades dels daus:", resultats)
daus_6()



import random
def dau_x():
    num_cares = int(input("De quantes cares és el dau? "))
    resultat = random.randint(1, num_cares)
    print("El resultat de la tirada és:", resultat)
dau_x()




import random
def daus_x():
    num_cares = int(input("De quantes cares són els daus? "))
    num_daus = int(input("Quants daus vols llençar? "))
    resultats = [random.randint(1, num_cares) for _ in range(num_daus)]
    print("Resultats de les tirades dels daus:", resultats)
daus_x()


























