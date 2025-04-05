import pygame
def loadbackground(image):
    return pygame.image.load(f"Pygame_project/assets/images/{image}.png").convert_alpha()