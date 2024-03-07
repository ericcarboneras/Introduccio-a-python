import pygame

def ask_user_details():
    title = input("Introdueix el títol de la finestra: ")
    width = int(input("Introdueix l'amplada de la finestra: "))
    height = int(input("Introdueix l'alçada de la finestra: "))
    red = int(input("Quantitat de vermell al color de fons (0-255): "))
    green = int(input("Quantitat de verd al color de fons (0-255): "))
    blue = int(input("Quantitat de blau al color de fons (0-255): "))
    fullscreen = input("Vols que el programa estigui en pantalla sencera? (sí/no): ").lower() == 'sí'
    return title, width, height, (red, green, blue), fullscreen

def select_background_image():
    print("Selecciona una imatge de fons:")
    print("1. background1.jpg")
    print("2. background2.jpg")
    print("3. background3.jpg")
    choice = input("Introdueix el número de la imatge que vols: ")
    return 'assets/background{}.jpg'.format(choice if choice in ['1', '2', '3'] else 'default')

def main():
    pygame.init()

    title, width, height, background_color, fullscreen = ask_user_details()
    background_image = select_background_image()

    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN if fullscreen else 0)
    pygame.display.set_caption(title)

    screen.fill(background_color)
    background = pygame.image.load(background_image).convert()
    screen.blit(background, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        pygame.display.update()

if __name__ == "__main__":
    main()
