paraules = []
while True:
    paraula = input("Introdueix una paraula (o 'final' per acabar): ")
    if paraula.lower() == 'final':
        break
    paraules.append(paraula)
concatenacio = ' '.join(paraules)
print("La concatenació de les paraules és:", concatenacio)
