# This file contains the welcome screen


# Imports
from tkinter import *
from game import Game
from PIL import Image,ImageTk

class Welcome(Toplevel):
    def __init__(self,playername):
        super().__init__()
        self.title("Welcome")
        self.geometry("400x400")
        self.playername = playername

        #Welcome Message
        self.w_message1 = Label(self, text=f"Welcome to Dice Roller, {self.playername}")
        self.w_message1.pack()


        #Image
        self.dice = Image.open("Dice-Game\welcome.jpg")
        #self.dice = self.dice.resize((100,100), Image.ANTIALIAS)
        self.diceimg = ImageTk.PhotoImage(self.dice)
        self.imagelbl = Label(self,image=self.diceimg)
        self.imagelbl.config(image=self.diceimg)
        self.imagelbl.pack()

        def play():
            self.destroy()
            Game(self.playername)

        self.playbtn = Button(self, text="Play", command=play, padx=50)
        self.playbtn.pack()
        