llista_paraules = []
while (nova_paraula := input("Introdueix una paraula (o escriu 'final' per acabar): ")) != 'final':
    llista_paraules.append(nova_paraula)
  
paraula_a_buscar = input("Introdueix una paraula per cercar i eliminar de la llista: ")
conteig = llista_paraules.count(paraula_a_buscar)
print(f"La paraula '{paraula_a_buscar}' apareix {conteig} vegades a la llista.")
llista_paraules = [paraula for paraula in llista_paraules if paraula != paraula_a_buscar]

print("Llista actualitzada:", llista_paraules)
