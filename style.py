import pygame

def draw_snake(window, snake, block_size):
    """Zeichnet die Schlange."""
    for segment in snake:
        pygame.draw.rect(window, (0, 255, 0), pygame.Rect(segment[0], segment[1], block_size, block_size))


def draw_target(window, target, block_size):
    """Zeichnet das Ziel."""
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(target[0], target[1], block_size, block_size))
