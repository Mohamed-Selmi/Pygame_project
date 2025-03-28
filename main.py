import pygame
from character import Character

pygame.init()

SCREEN_WIDTH=1600
SCREEN_HEIGHT=900

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Project")

clock=pygame.time.Clock()
FPS=60

background_image=pygame.image.load("Pygame_project/assets/images/background.jpg").convert_alpha()

def load_image():
    scaled_image=pygame.transform.scale(background_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_image,(0,0))




character1=Character(200,510)

character2=Character(1200,510)

game_running=True

while game_running:
    clock.tick(FPS)
    load_image()
    character1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen)
   #  character2.move()
    character1.draw(screen)
    character2.draw(screen)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_running=False

    pygame.display.update()
pygame.quit()