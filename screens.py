import pygame
import sys

def show_homescreen(window):
    """Zeigt den Homescreen mit Auswahl über Pfeiltasten."""
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 50)
    clock = pygame.time.Clock()

    # Farben
    white = (255, 255, 255)
    black = (0, 0, 0)
    yellow = (255, 255, 0)  # Hervorhebung

    # Menüoptionen
    options = ["Spiel starten", "Highscore", "Beenden"]
    selected_index = 0  # Index des aktuell ausgewählten Buttons

    while True:
        window.fill(black)

        # Titeltext
        title_text = font.render("The Duck is Fucked!", True, white)
        window.blit(title_text, (100, 100))

        # Buttons zeichnen
        for i, option in enumerate(options):
            color = yellow if i == selected_index else white
            button_text = small_font.render(option, True, color)
            window.blit(button_text, (250, 250 + i * 100))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Pfeil hoch
                    selected_index = (selected_index - 1) % len(options)
                elif event.key == pygame.K_DOWN:  # Pfeil runter
                    selected_index = (selected_index + 1) % len(options)
                elif event.key == pygame.K_RETURN:  # Enter-Taste
                    return options[selected_index].lower().replace(" ", "_")

        clock.tick(30)


def show_gameover_screen(window, score):
    """Zeigt den Game-Over-Bildschirm mit Navigation über Pfeiltasten."""
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 50)
    clock = pygame.time.Clock()

    # Farben
    white = (255, 255, 255)
    black = (0, 0, 0)
    yellow = (255, 255, 0)  # Hervorhebung
    red = (255, 0, 0)

    # Menüoptionen
    options = ["Noch einmal", "Highscore", "Hauptmenü"]
    selected_index = 0  # Index des aktuell ausgewählten Menüpunkts

    while True:
        window.fill(black)

        # Game-Over-Titel
        gameover_text = font.render("Game Over", True, red)
        score_text = font.render(f"Score: {score}", True, white)
        window.blit(gameover_text, (200, 100))
        window.blit(score_text, (250, 200))

        # Menüoptionen zeichnen
        for i, option in enumerate(options):
            color = yellow if i == selected_index else white
            option_text = small_font.render(option, True, color)
            window.blit(option_text, (200, 300 + i * 80))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Pfeil hoch
                    selected_index = (selected_index - 1) % len(options)
                elif event.key == pygame.K_DOWN:  # Pfeil runter
                    selected_index = (selected_index + 1) % len(options)
                elif event.key == pygame.K_RETURN:  # Enter-Taste
                    return options[selected_index].lower().replace(" ", "_")

        clock.tick(30)


# Simples Hauptprogramm
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("The Duck is Fucked")

    while True:
        # Homescreen
        result = show_homescreen(screen)

        if result == "spiel_starten":
            print("Spiel wird gestartet...")
            # Hier könnte dein Spiel starten, z. B. eine Spielfunktion
            # Wenn das Spiel vorbei ist, zeige den Game-Over-Bildschirm
            gameover_result = show_gameover_screen(screen, score=42)
            if gameover_result == "noch_einmal":
                print("Spiel wird erneut gestartet...")
                continue
            elif gameover_result == "hauptmenü":
                print("Zurück zum Hauptmenü...")
                continue
            elif gameover_result == "beenden":
                print("Spiel wird beendet...")
                pygame.quit()
                sys.exit()
        elif result == "highscore":
            print("Highscore-Bildschirm wird angezeigt... (noch nicht implementiert)")
            continue
        elif result == "beenden":
            print("Spiel wird beendet...")
            pygame.quit()
            sys.exit()
