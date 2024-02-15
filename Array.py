comunitat = ["Gandalf", "Legolas", "Gimli", "Aragorn", "Merry", "Pippin", "Frodo", "Sam", "Boromir"]
print(comunitat[0])

print(comunitat[-1])

posicion_media = len(comunitat) // 2
print(comunitat[posicion_media])

primer_alfabeticamente = min(comunitat, key=len)
print(primer_alfabeticamente)

darrer_alfabeticament = max(comunitat)
print(darrer_alfabeticament)

comunitat.remove("Aragorn")
primer_alfabeticament = min(comunitat)
print(primer_alfabeticament)

comunitat.append("Arwen")
comunitat.sort()
print(comunitat)









