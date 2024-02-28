lives = int(input("Quantes vides tens? "))
position = 0

while lives:
    print("Vides:", lives)
    print(" " * position + "*")
    move = input("'a' (esquerra), 'd' (dreta), 'q' (sortir): ")
    if move == 'a': position = max(0, position - 1)
    if move == 'd': position = min(20, position + 1)
    if move == 'q': break
    if move == 'k':
        lives -= 1
        if lives == 0:
            print("Game Over")
            break
