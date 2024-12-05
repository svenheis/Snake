import pygame
import random
from style import draw_snake
from style import draw_target


def run_game(window, width, height):

    """Hauptspiel-Logik."""
    block_size = 50
    direction = "RIGHT"
    snake = [(width // 2, height // 2)]
    score = 0
    clock = pygame.time.Clock()

    target = generate_target(width, height, block_size, snake)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return score
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        # Bewegung der Schlange
        head_x, head_y = snake[0]
        dx, dy = get_direction_vector(direction, block_size)
        new_head = (head_x + dx, head_y + dy)

        # Kollision prüfen
        if (
            new_head[0] < 0 or new_head[1] < 0 or
            new_head[0] >= width or new_head[1] >= height or
            new_head in snake
        ):
            return score

        snake.insert(0, new_head)

        if new_head == target:
            score += 1
            target = generate_target(width, height, block_size, snake)
        else:
            snake.pop()

        # Zeichnen
        window.fill((0, 0, 0))
        draw_snake(window, snake, block_size)
        draw_target(window, target, block_size)
        pygame.display.flip()
        clock.tick(10)

def get_direction_vector(direction, block_size):
    """Gibt den Bewegungsvektor basierend auf der Richtung zurück."""
    if direction == "UP":
        return 0, -block_size
    if direction == "DOWN":
        return 0, block_size
    if direction == "LEFT":
        return -block_size, 0
    if direction == "RIGHT":
        return block_size, 0
    return 0, 0

def generate_target(width, height, block_size, snake):
    """Generiert ein neues Ziel, das nicht auf der Schlange liegt."""
    while True:
        target_x = random.randrange(0, width // block_size) * block_size
        target_y = random.randrange(0, height // block_size) * block_size
        target = (target_x, target_y)
        if target not in snake:
            return target