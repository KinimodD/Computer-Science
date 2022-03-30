# The actual game is stored in this file

# Imports
from tkinter import *
from random import randint
from PIL import Image, ImageTk

class Game(Toplevel):
    def __init__(self,playername):
        super().__init__()
        self.title("Dice Game")
        self.geometry("500x500")
        self.turn = Label(self, text=(playername + "'s", "turn"))
        self.turn.grid(row=0,columnspan=3,column=0)
        self.roll = Button(self, text="Roll dice", command=self.rollDice)
        self.roll.grid(row=1,column=2)

    def numToImg(self,dice):
        if dice == 1:
            diceimg = Image.open("Computer-Science\Dice-Game\dice side images\one.jpg")
            self.diceimgtk = ImageTk.PhotoImage(diceimg)
        elif dice == 2:
            diceimg = Image.open("Computer-Science\Dice-Game/dice side images/two.jpg")
            self.diceimgtk = ImageTk.PhotoImage(diceimg)
        elif dice == 3:
            diceimg = Image.open("Computer-Science\Dice-Game\dice side images/three.jpg")
            self.diceimgtk = ImageTk.PhotoImage(diceimg)
        elif dice == 4:
            diceimg = Image.open("Computer-Science\Dice-Game\dice side images/four.jpg")
            self.diceimgtk = ImageTk.PhotoImage(diceimg)
        elif dice == 5:
            diceimg = Image.open("Computer-Science\Dice-Game\dice side images/five.jpg")
            self.diceimgtk = ImageTk.PhotoImage(diceimg)
        elif dice == 6:
            diceimg = Image.open("Computer-Science\Dice-Game\dice side images\six.jpg")
            self.diceimgtk = ImageTk.PhotoImage(diceimg)
        else:
            return "Error"





    def rollDice(self):
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        
        self.numToImg(dice1)
        
        img1 = Label(self, image=self.diceimgtk)
        img1.grid(row=1,column=0)
        img1.image = self.diceimgtk
        
        self.numToImg(dice2)

        img2 = Label(self, image=self.diceimgtk)
        img2.grid(row=1,column=1)


       