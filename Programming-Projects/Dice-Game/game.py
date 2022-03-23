from tkinter import *
from random import randint
from PIL import Image, ImageTk

class Game(Tk):
    def __init__(self):
        super().__init__()
        self.title("Dice Game")
        self.geometry("500x500")


        def numToImg(dice):
            if dice == 1:
                self.diceimg = Image.open("Computer-Science\Programming-Projects\Dice-Game\one.jpg")
                self.diceimgtk = ImageTk.PhotoImage(self.diceimg)
            elif dice == 2:
                self.diceimg = Image.open("Computer-Science/Programming-Projects/Dice-Game/two.jpg")
                self.diceimgtk = ImageTk.PhotoImage(self.diceimg)
            elif dice == 3:
                self.diceimg = Image.open("Computer-Science/Programming-Projects/Dice-Game/three.jpg")
                self.diceimgtk = ImageTk.PhotoImage(self.diceimg)
            elif dice == 4:
                self.diceimg = Image.open("Computer-Science/Programming-Projects/Dice-Game/four.jpg")
                self.diceimgtk = ImageTk.PhotoImage(self.diceimg)
            elif dice == 5:
                self.diceimg = Image.open("Computer-Science/Programming-Projects/Dice-Game/five.jpg")
                self.diceimgtk = ImageTk.PhotoImage(self.diceimg)
            elif dice == 6:
                self.diceimg = Image.open("Computer-Science/Programming-Projects/Dice-Game/six.jpg")
                self.diceimgtk = ImageTk.PhotoImage(self.diceimg)



        self.player = 1
        self.turn = Label(self, text=("Player", str(self.player) + "'s", "turn"))
        self.turn.grid(row=0,columnspan=3,column=0)

        def rollDice():
            dice1 = randint(1,6)
            dice2 = randint(1,6)
            numToImg(dice1)
            
            Label(self, image=self.diceimgtk).grid(row=1,column=0)
            numToImg(dice2)

            Label(self, image=self.diceimgtk).grid(row=1,column=1)

            
        self.roll = Button(self, text="Roll dice", command=rollDice)
        self.roll.grid(row=1,column=2)

if __name__== "__main__":
    myApp = Game()
    myApp.mainloop()