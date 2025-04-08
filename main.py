import pygame
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from character import Character
from loadcharacters import *
from loadmap import loadbackground
class Menu:
	def __init__(self,master):
		self.master=master  
		self.master.geometry('1000x960')   
		self.master.maxsize(1000,960)
		self.frame1=tk.Frame(self.master, width=1000, height=960,bg='#222831',borderwidth=2, relief="solid")
		self.frame1.place(x=0,y=0)
		self.play_button=tk.Button(self.frame1,text="PLAY",font=('Arial',15,"bold"),bg='#FFD369',borderwidth=2, relief="solid",command=lambda:self.start_game())
		self.play_button.place(x=240,y=155,height=80,width=480)
		self.player1name_label=tk.Label(self.frame1, text="Pick a name for player 1:",font=('Arial',13,"bold"),bg='#EEEEEE')
		self.player1name_label.place(x=120,y=300,height=25,width=240)
		self.Player1_name=tk.Entry(self.frame1,width=50,bg="#FFF")
		self.Player1_name.place(x=100,y=350)
		style= ttk.Style()
		style.theme_use('clam')
		style.configure("TCombobox", fieldbackground= "#FFF", background= "#048A81")
		self.player2name_label=tk.Label(self.frame1, text="Pick a name for player 2:",font=('Arial',13,"bold"),bg='#EEEEEE')
		self.player2name_label.place(x=670,y=300,height=25,width=240)
		self.Player2_name=tk.Entry(self.frame1,width=50,bg="#FFF")
		self.Player2_name.place(x=650,y=350)
		self.player1_label=tk.Label(self.frame1, text="Choose your fighter Player 1:",font=('Arial',13,"bold"),bg='#EEEEEE')
		self.player1_label.place(x=120,y=500,height=25,width=240)
		
		self.player1=ttk.Combobox(self.frame1,height = 10,width=50, values=('warrior', 'Female wizard', 'oni','king','samurai','evil wizard','Huntress','knight','Tarzan'))
		self.player1.place(x=80,y=550)
		self.player2_label=tk.Label(self.frame1, text="Choose your fighter Player 2:",font=('Arial',13,"bold"),bg='#EEEEEE')
		self.player2_label.place(x=670,y=500,height=25,width=240)
		self.player2=ttk.Combobox(self.frame1,height = 10,width=50, values=('warrior', 'Female wizard', 'oni','king','samurai','evil wizard','Huntress','knight','Tarzan'))
		self.player2.place(x=650,y=550)
		self.map_label=tk.Label(self.frame1,text="Select a map:",font=('Arial',13,"bold"),bg='#EEEEEE')
		self.map_label.place(x=450,y=650)
		self.map=ttk.Combobox(self.frame1,height = 10,width=50, values=('Japanese Bath', 'Ruined castle', 'Harley bike club','Foggy swamp','Chinese pavillion','Temple',
																  'Lady in the lake','Harbor','Failed heist','Waterfall'))
		self.map.place(x=350,y=700)
		self.exit_button=tk.Button(self.frame1,text="EXIT",font=('Arial',15,"bold"),bg='#FFD369',borderwidth=2, relief="solid",command=lambda:self.master.destroy())
		self.exit_button.place(x=240,y=850,height=80,width=480)
		'''self.imageWS = ImageTk.PhotoImage(Image.open("./Pygame_project/assets/wizard/wiza.gif"), format="gif -index 2")
		self.image1=tk.Label(self.frame1, image=self.imageWS,bg='black')
		self.image1.place(x=80,y=500,height=350,width=150)
		self.photo_list=[] 
		self.photo_list.append(self.imageWS)'''
	def closeWindow(self):
		self.master.destroy()
        
	def start_game(self):
			name1=self.Player1_name.get()
			name2=self.Player2_name.get()
			char1=self.player1.get()
			char2=self.player2.get()
			map=self.map.get()
			self.closeWindow()
			main2(name1,name2,char1,char2,map)
	
def main2(name1,name2,char1="warrior",char2="warrior",image="background1"):
	pygame.init()
	SCREEN_WIDTH=1600
	SCREEN_HEIGHT=900
	screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
	pygame.display.set_caption("Pygame Project")

	clock=pygame.time.Clock()
	FPS=60
	YELLOW=(255,211,105)
	RED=(165,36,34)
	WHITE=(235,242,250)
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
	GAME_OVER_COOLDOWN=6000
	round_number=1
	PLAYER1_XPOSITON=200
	PLAYER1_YPOSITION=630
	PLAYER2_XPOSITON=1200
	PLAYER2_YPOSITION=630
	victory_image=pygame.image.load("Pygame_Project/assets/images/victory.png").convert_alpha()
	background_image=loadbackground(image)
	def load_image():
		scaled_image=pygame.transform.scale(background_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
		screen.blit(scaled_image,(0,0))

	def draw_health_bar(health,x,y):
		bar_ratio=health/100
		pygame.draw.rect(screen,BLACK,(x-5,y-5,410,40))
		pygame.draw.rect(screen,RED,(x,y,400,30))
		pygame.draw.rect(screen,YELLOW,(x,y,400*bar_ratio,30))
	def load_player(player,x,y,flip,name,char):
		if char=="warrior":
			character=Character(player,x,y,flip,name,load_warrior())
		elif char=='Female wizard':
			character=Character(player,x,y,flip,name,load_wizardF())
		elif char=='oni':
			character=Character(player,x,y,flip,name,load_ONI())
		elif char=="king":
			character=Character(player,x,y,flip,name,load_King())
		elif char=="samurai":
			character=Character(player,x,y,flip,name,load_Samurai())
		elif char=="evil wizard":
			character=Character(player,x,y,flip,name,load_Evilwizard())
		elif char=="Huntress":
			character=Character(player,x,y,flip,name,load_Huntress())
		elif char=="knight":
			character=Character(player,x,y,flip,name,load_spaceknight())
		elif char=="Tarzan":
			character=Character(player,x,y,flip,name,load_Tarzan())	
		return character
	
	character1=load_player(1,PLAYER1_XPOSITON,PLAYER1_YPOSITION,False,name1,char1)

	#character2=Character(2,1200,510,True,WIZARD_DATA,WIZARD_sheet,WIZARD_animation_steps)
	character2=load_player(2,PLAYER2_XPOSITON,PLAYER2_YPOSITION,True,name2,char2)

	game_running=True
	while game_running:
		clock.tick(FPS)
		load_image()
		draw_text("Round number:"+str(round_number),round_font,WHITE,SCREEN_WIDTH/2-175, 10)
		draw_health_bar(character1.health,20,20)
		draw_health_bar(character2.health,SCREEN_WIDTH-400-30,20)
		draw_text(f"{name1}: "+str(score[0]),score_font,WHITE,40,60)
		draw_text(f"{name2}: "+str(score[1]),score_font,WHITE,SCREEN_WIDTH-(len(name2)*50),60)
		if intro_count<0:
			character1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,character2,round_over)
			character2.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,character1,round_over)
		else:
			draw_text(str(intro_list[intro_count]),count_font,RED,SCREEN_WIDTH / 2-75,SCREEN_HEIGHT / 3)		
			if (pygame.time.get_ticks()-last_count_update)>=1000:
				intro_count-=1
				last_count_update= pygame.time.get_ticks()
				
		character1.update_character()
		character2.update_character()
		
		character1.draw(screen)
		character2.draw(screen)
		if round_over==False:
			if character1.alive==False and character2.alive==False:
				score[0]+=1
				score[1]+=1
				round_number+=1
				round_over=True
				round_over_time=pygame.time.get_ticks()
			elif character1.alive==False:
				score[1]+=1
				round_number+=1
				round_over=True
				round_over_time=pygame.time.get_ticks()
				
			elif character2.alive==False:
				score[0]+=1
				round_number+=1
				round_over=True
				round_over_time=pygame.time.get_ticks()

				
		else:
			if round_number>3:
				
				if score[0]>score[1]:
						draw_text(f"Game over! {name1} wins! ",score_font,RED,SCREEN_WIDTH/2-180,SCREEN_HEIGHT/2)
				elif score[0]<score[1]:
						draw_text(f"Game over! {name2} wins! ",score_font,RED,SCREEN_WIDTH/2-180,SCREEN_HEIGHT/2)
				elif score[0]==score[1]:
					draw_text(f"Game over! Draw! ",score_font,RED,SCREEN_WIDTH/2-180,SCREEN_HEIGHT/2)
				if pygame.time.get_ticks()-round_over_time>ROUND_OVER_COOLDOWN:
					
					game_running=False
			else:	
				if character1.alive==False and character2.alive==False:
					
					draw_text("Draw!",score_font,RED,SCREEN_WIDTH/2-125,SCREEN_HEIGHT/2)
				elif character1.alive==False:
					
					draw_text(f"{name2} wins! ",score_font,RED,SCREEN_WIDTH/2-150,SCREEN_HEIGHT/2)
					screen.blit(victory_image,(600,350))
				elif character2.alive==False:
					
					draw_text(f"{name1} wins! ",score_font,RED,SCREEN_WIDTH/2-150,SCREEN_HEIGHT/2)
					
					screen.blit(victory_image,(600,350))
				'''if round_number>3:
					round_over_time=pygame.time.get_ticks()
					if score[0]>score[1]:
							draw_text(f"Game over! {name1}  wins! ",score_font,RED,SCREEN_WIDTH/2-150,SCREEN_HEIGHT/2)
					elif score[0]<score[1]:
							draw_text(f"Game over! {name2} wins! ",score_font,RED,SCREEN_WIDTH/2-150,SCREEN_HEIGHT/2)
					if pygame.time.get_ticks()-round_over_time>ROUND_OVER_COOLDOWN:
						
						game_running=False
						pygame.quit()'''
				if pygame.time.get_ticks()-round_over_time>ROUND_OVER_COOLDOWN:
					round_over=False
					intro_count=3
					character1=load_player(1,PLAYER1_XPOSITON,PLAYER1_YPOSITION,False,name1,char1)
					character2=load_player(2,PLAYER2_XPOSITON,PLAYER2_YPOSITION,True,name2,char2)

		for event in pygame.event.get():
			if event.type==pygame.QUIT: 
				game_running=False
				pygame.quit()
			
		pygame.display.update()
	main()
	

def main():
	pygame.quit()
	root = tk.Tk()
	root.title("Choose your warrior")
	switchWindow(root,Menu)
	

def switchWindow(root,newWindow):
    newWindow(root)
    root.mainloop()
def closeWindow(self):
        self.master.destroy()
        
if __name__ == '__main__':
	#main()
	main2("Mohamed","HSAN","king","king","Temple")
