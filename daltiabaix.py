asterisk_pos = 10

while True:
    print(" " * asterisk_pos + "*")
    key = input("Presiona 'w' per moure l'asterisc amunt, 's' per moure'l avall, o 'q' per sortir: ")
    if key == 'w': asterisk_pos = max(0, asterisk_pos - 1)
    elif key == 's': asterisk_pos = min(20, asterisk_pos + 1)
    elif key == 'q': break
