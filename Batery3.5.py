def es_primer(num):
    """Funció per comprovar si un número és primer."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

limit_superior = int(input("introdueix el límit superior per als números primers: "))
print("Números primers fins a", limit_superior, ":")
for numero in range(2, limit_superior + 1):
    if es_primer(numero):
        print(numero, end=" ")
