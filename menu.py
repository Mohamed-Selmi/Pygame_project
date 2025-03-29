import pygame
from character import Character
import tkinter as tk
from tkinter import ttk
from main import main2

def main():
	root = tk.Tk()
	root.title("Choose your warrior")
	root.geometry('1000x960')
	root.maxsize(1280,720)
	root.configure(background='#FFEAAE')
	play_button=tk.Button(root,text="play",font=('Arial',15,"bold"),bg='#F0A04B',borderwidth=2, relief="solid",command=start_game)
	play_button.place(x=10,y=25,height=100,width=225)
	root.mainloop()
def start_game():
	print("game starting")
	main2()
	
if __name__ == '__main__':
	main()

	



#game play: choose between 3 fighters for each player, each fighter will have it's values imported and the whole shebang, pass it as argument from the tkitner menu to a start game function
#add round and score first maybe?