            num = float(input("Introdueix un nombre (0 per sortir): "))
            
            if num == 0:
                break   
            numeros.append(num)  
            
        except ValueError:
            print("Si us plau, introdueix un nombre vàlid.")

    if len(numeros) == 0:
        print("No s'han introduït cap nombre.")
    else:
        mitjana = sum(numeros) / len(numeros)  
        print("La mitjana dels números introduïts és:", mitjana)

calcular_mitjana()
