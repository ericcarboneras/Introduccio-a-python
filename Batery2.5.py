anys_treballats = int(input("introdueix la quantitat d'anys que portes treballant com a programador: "))
if anys_treballats < 5:
    categoria = "junior"
else:
    categoria = "senior"
print(f"Ets considerat un programador {categoria}.")
