import pygame
from character import Character

pygame.init()

SCREEN_WIDTH=1600
SCREEN_HEIGHT=900

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Project")

clock=pygame.time.Clock()
FPS=60
YELLOW=(255,255,0)
RED=(255,0,0)
WHITE=(255,255,255)
BLACK=(0,0,0)

WARRIOR_SIZE=162
WARRIOR_SCALE=4
WARRIOR_OFFSET=[72,56]
WARRIOR_DATA=[WARRIOR_SIZE,WARRIOR_SCALE,WARRIOR_OFFSET]


background_image=pygame.image.load("Pygame_project/assets/images/background.jpg").convert_alpha()
warrior_sheet=pygame.image.load("Pygame_project/assets/warrior/Sprites/warrior1.png").convert_alpha()
warrior_animation_steps=[10,8,1,7,7,3,7]
king_animation_steps=[8,8,2,2,4,4,4,6]

def load_image():
    scaled_image=pygame.transform.scale(background_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_image,(0,0))

def draw_health_bar(health,x,y):
    bar_ratio=health/100
    pygame.draw.rect(screen,BLACK,(x-5,y-5,410,40))
    pygame.draw.rect(screen,RED,(x,y,400,30))
    pygame.draw.rect(screen,YELLOW,(x,y,400*bar_ratio,30))
    



character1=Character(1,200,510,False,WARRIOR_DATA,warrior_sheet,warrior_animation_steps)

character2=Character(2,1200,510,True,WARRIOR_DATA,warrior_sheet,warrior_animation_steps)

game_running=True

while game_running:
    clock.tick(FPS)
    load_image()
    draw_health_bar(character1.health,20,20)
    draw_health_bar(character2.health,1020,20)
    character1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,character2)
    character2.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,character1)
    character1.update_character()
    character2.update_character()
    
    character1.draw(screen)
    character2.draw(screen)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_running=False

    pygame.display.update()
pygame.quit()