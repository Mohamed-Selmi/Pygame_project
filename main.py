import pygame
from character import Character
from loadcharacters import load_warrior,load_wizardF,load_ONI
def main2(char1="warrior",char2="warrior"):
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
	count_font=pygame.font.Font("Pygame_project/assets/fonts/Turok.ttf",80)
	score_font=pygame.font.Font("Pygame_project/assets/fonts/Turok.ttf",40)
	round_font=pygame.font.Font("Pygame_project/assets/fonts/Turok.ttf",50)																	;  
	def draw_text(text,font,text_color,x,y):
		img=font.render(text,True,text_color)
		screen.blit(img,(x,y)) 
	intro_count=3
	intro_list=["Fight!",1,2,3]
	
	last_count_update=pygame.time.get_ticks()
	score=[0,0]
	round_over=False
	ROUND_OVER_COOLDOWN=3000
	round_number=1
	PLAYER1_XPOSITON=200
	PLAYER1_YPOSITION=510
	PLAYER2_XPOSITON=1200
	PLAYER2_YPOSITION=510
	victory_image=pygame.image.load("Pygame_Project/assets/images/victory.png").convert_alpha()
	background_image=pygame.image.load("Pygame_project/assets/images/background.jpg").convert_alpha()
	


	def load_image():
		scaled_image=pygame.transform.scale(background_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
		screen.blit(scaled_image,(0,0))

	def draw_health_bar(health,x,y):
		bar_ratio=health/100
		pygame.draw.rect(screen,BLACK,(x-5,y-5,410,40))
		pygame.draw.rect(screen,RED,(x,y,400,30))
		pygame.draw.rect(screen,YELLOW,(x,y,400*bar_ratio,30))
		

	
	def load_player(player,x,y,flip,char):
		if char=="warrior":
			character=Character(player,x,y,flip,load_warrior())
		elif char=='wizard':
			character=Character(player,x,y,flip,load_wizardF())
		elif char=='oni':
			character=Character(player,x,y,flip,load_ONI())
		return character
	


	character1=load_player(1,PLAYER1_XPOSITON,PLAYER1_YPOSITION,False,char1)

	#character2=Character(2,1200,510,True,WIZARD_DATA,WIZARD_sheet,WIZARD_animation_steps)
	character2=load_player(2,PLAYER2_XPOSITON,PLAYER2_YPOSITION,True,char2)
	game_running=True
	
	while game_running:
		clock.tick(FPS)
		load_image()
		draw_text("Round numer:"+str(round_number),round_font,RED,SCREEN_WIDTH/2-200, 10)
		draw_health_bar(character1.health,20,20)
		draw_health_bar(character2.health,SCREEN_WIDTH-400-30,20)
		draw_text("P1: "+str(score[0]),score_font,RED,40,60)
		draw_text("P2: "+str(score[1]),score_font,RED,SCREEN_WIDTH-120,60)

		if intro_count<0:
			character1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,character2,round_over)
			character2.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,character1,round_over)
		else:
			draw_text(str(intro_list[intro_count]),count_font,RED,SCREEN_WIDTH / 2,SCREEN_HEIGHT / 3)
					
			if (pygame.time.get_ticks()-last_count_update)>=1000:
				intro_count-=1
				last_count_update= pygame.time.get_ticks()
				
		character1.update_character()
		character2.update_character()
		
		character1.draw(screen)
		character2.draw(screen)
		if round_over==False:
			if character1.alive==False:
				score[1]+=1
				round_number+=1
				round_over=True
				round_over_time=pygame.time.get_ticks()
				print(score)
			elif character2.alive==False:
				score[0]+=1
				round_number+=1
				round_over=True
				round_over_time=pygame.time.get_ticks()
				print(score)
		else:
			if character1.alive==False:
				draw_text("PLayer 2 wins: ",score_font,RED,SCREEN_WIDTH/2-150,SCREEN_HEIGHT/2)
			screen.blit(victory_image,(600,350))
			if pygame.time.get_ticks()-round_over_time>ROUND_OVER_COOLDOWN:
				round_over=False
				intro_count=3

				character1=Character(1,200,510,False,load_warrior())

				character2=Character(2,1200,510,True,load_ONI())

		
		for event in pygame.event.get():
			if event.type==pygame.QUIT or round_number>3:
				game_running=False
				
		pygame.display.update()
	pygame.quit()
	

if __name__ == '__main__':
	main2()
	