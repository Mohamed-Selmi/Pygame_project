import pygame

def load_warrior():
	WARRIOR_SIZE=162
	WARRIOR_SCALE=4
	WARRIOR_OFFSET=[72,56]
	WARRIOR_DATA=[WARRIOR_SIZE,WARRIOR_SCALE,WARRIOR_OFFSET]
	warrior_animation_steps=[10,8,1,7,7,3,7]
	warrior_sheet=pygame.image.load("Pygame_project/assets/warrior/Sprites/warrior1.png").convert_alpha()
	return(WARRIOR_DATA,warrior_sheet,warrior_animation_steps)



def load_wizardF():
	WIZARD_SIZE=140
	WIZARD_SCALE=4
	WIZARD_OFFSET=[63,56]
	WIZARD_DATA=[WIZARD_SIZE,WIZARD_SCALE,WIZARD_OFFSET]
	WIZARD_animation_steps=[10,8,3,13,13,3,18]
	WIZARD_sheet=pygame.image.load("Pygame_project/assets/wizard/Sprites/wizzy.png").convert_alpha()
	return(WIZARD_DATA,WIZARD_sheet,WIZARD_animation_steps)


def load_ONI():
	ONI_SIZE=200
	ONI_SCALE=4
	ONI_OFFSET=[90,85]
	ONI_DATA=[ONI_SIZE,ONI_SCALE,ONI_OFFSET]
	ONI_animation_steps=[4,8,2,4,4,3,7]
	ONI_sheet=pygame.image.load("Pygame_project/assets/Oni/Sprites/oni.png").convert_alpha()
	return(ONI_DATA,ONI_sheet,ONI_animation_steps)

		