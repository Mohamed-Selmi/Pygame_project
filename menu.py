import pygame
from character import Character
import tkinter as tk
from tkinter import ttk
from main import main2
from PIL import Image, ImageTk

class Menu:
	def __init__(self,master):
		self.master=master
		self.master.geometry('1000x960')
		self.master.maxsize(1000,960)
		self.frame1=tk.Frame(self.master, width=1000, height=960,bg='#197278',borderwidth=2, relief="solid")
		self.frame1.place(x=0,y=0)
		self.play_button=tk.Button(self.frame1,text="PLAY",font=('Arial',15,"bold"),bg='#F0A04B',borderwidth=2, relief="solid",command=lambda:self.start_game())
		self.play_button.place(x=240,y=155,height=80,width=480)
		self.player1_label=tk.Label(self.frame1, text="Choose your fighter Player 1:",font=('Arial',13,"bold"),bg='#F0A04B')
		self.player1_label.place(x=120,y=300,height=25,width=240)
		self.player1=ttk.Combobox(self.frame1,height = 10,width=50, values=('warrior', 'wizard', 'oni'))
		self.player1.place(x=80,y=350)
		self.player2_label=tk.Label(self.frame1, text="Choose your fighter Player 2:",font=('Arial',13,"bold"),bg='#F0A04B')
		self.player2_label.place(x=670,y=300,height=25,width=240)
		self.player2=ttk.Combobox(self.frame1,height = 10,width=50, values=('warrior', 'wizard', 'oni'))
		self.player2.place(x=650,y=350)
		self.exit_button=tk.Button(self.frame1,text="EXIT",font=('Arial',15,"bold"),bg='#F0A04B',borderwidth=2, relief="solid",command=lambda:self.master.destroy())
		self.exit_button.place(x=240,y=655,height=80,width=480)
		#imageW.show()
		self.imageWS = ImageTk.PhotoImage(Image.open("./Pygame_project/assets/wizard/wiza.gif"), format="gif -index 2")
		self.image1=tk.Label(self.frame1, image=self.imageWS,bg='black')
		self.image1.place(x=80,y=500,height=350,width=150)
		self.photo_list=[] 
		self.photo_list.append(self.imageWS)

	def start_game(self):
			char1=self.player1.get()
			char2=self.player2.get()
			print("game starting")
			main2(char1,char2)

	

def main():
	root = tk.Tk()
	root.title("Choose your warrior")
	switchWindow(root,Menu)

def switchWindow(root,newWindow):
    newWindow(root)
    root.mainloop()
if __name__ == '__main__':
	main()

	



#game play: choose between 3 fighters for each player, each fighter will have it's values imported and the whole shebang, pass it as argument from the tkitner menu to a start game function
#add round and score first maybe?