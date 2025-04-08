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

def load_King():
	KING_SIZE=155.01
	KING_SCALE=3
	KING_OFFSET=[75,55]
	KING_DATA=[KING_SIZE,KING_SCALE,KING_OFFSET]
	KING_animation_steps=[6,8,2,6,6,4,11]
	KING_sheet=pygame.image.load("Pygame_project/assets/kingc/king.png").convert_alpha()
	return(KING_DATA,KING_sheet,KING_animation_steps)

def load_Samurai():
	SAMURAI_SIZE=200
	SAMURAI_SCALE=4.5
	SAMURAI_OFFSET=[90,80]
	SAMURAI_DATA=[SAMURAI_SIZE,SAMURAI_SCALE,SAMURAI_OFFSET]
	SAMURAI_animation_steps=[8,8,2,6,6,4,6]
	SAMURAI_sheet=pygame.image.load("Pygame_project/assets/Samurai/Sprites/samurai.png").convert_alpha()
	return(SAMURAI_DATA,SAMURAI_sheet,SAMURAI_animation_steps)


def load_Evilwizard():
	WIZARD_SIZE=150
	WIZARD_SCALE=4
	WIZARD_OFFSET=[63,56]
	WIZARD_DATA=[WIZARD_SIZE,WIZARD_SCALE,WIZARD_OFFSET]
	WIZARD_animation_steps=[8,8,8,8,8,4,5]
	WIZARD_sheet=pygame.image.load("Pygame_project/assets/Evilwizard/Sprites/evilwizard.png").convert_alpha()
	return(WIZARD_DATA,WIZARD_sheet,WIZARD_animation_steps)

def load_Huntress():
	HUNTRESS_SIZE=150
	HUNTRESS_SCALE=5.5
	HUNTRESS_OFFSET=[65,65]
	HUNTRESS_DATA=[HUNTRESS_SIZE,HUNTRESS_SCALE,HUNTRESS_OFFSET]
	HUNTRESS_animation_steps=[8,8,2,5,5,3,8]
	HUNTRESS_sheet=pygame.image.load("Pygame_project/assets/Huntress/Sprites/huntress.png").convert_alpha()
	return(HUNTRESS_DATA,HUNTRESS_sheet,HUNTRESS_animation_steps)

def load_spaceknight():
	SPACE_SIZE=180
	SPACE_SCALE=4
	SPACE_OFFSET=[80,68]
	SPACE_DATA=[SPACE_SIZE,SPACE_SCALE,SPACE_OFFSET]
	SPACE_animation_steps=[11,8,3,7,7,4,11]
	SPACE_sheet=pygame.image.load("Pygame_project/assets/knight/Sprites/knight.png").convert_alpha()
	return(SPACE_DATA,SPACE_sheet,SPACE_animation_steps)



def load_Tarzan():
	TARZAN_SIZE=126
	TARZAN_SCALE=4
	TARZAN_OFFSET=[50,40]
	TARZAN_DATA=[TARZAN_SIZE,TARZAN_SCALE,TARZAN_OFFSET]
	TARZAN_animation_steps=[10,8,3,7,9,3,11]
	TARZAN_sheet=pygame.image.load("Pygame_project/assets/Tarzan/Sprite/tarzan.png").convert_alpha()
	return(TARZAN_DATA,TARZAN_sheet,TARZAN_animation_steps)

