import pygame
import random
from sound import initialize_sounds
from screens import show_gameover_screen
from screens import show_homescreen
from gameLogic import run_game
from gameLogic import generate_target
from gameLogic import get_direction_vector
from style import draw_snake
from style import draw_target

initialize_sounds() 

def main(): 
    pygame.init()

    # Fenstergröße
    width, height = 1200, 900
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("The Duck is Fucked!")

    # Sounds initialisieren
    initialize_sounds()

    # Hauptschleife
    running = True
    while running:
        # Homescreen anzeigen
        start_game = show_homescreen(window)  # Übergabe des 'window'-Parameters
        if start_game:
            # Spiel ausführen
            score = run_game(window, width, height)
            # Gameover-Bildschirm anzeigen
            running = show_gameover_screen(window, score)
        else:
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()


show_homescreen()

show_gameover_screen()

get_direction_vector()

generate_target()

draw_target()

draw_snake()

run_game()


if __name__ == "__main__":
    main()
