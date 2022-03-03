from tkinter import *
from main import Window
import random
from PIL import Image, ImageTk

if __name__== "__main__":
    myApp = Window()
    myApp.mainloop()

myApp.destroy()

class Game(Tk):
    def __init__(self):
        super().__init__()
        self.title("Dice Game")
        self.geometry("500x500")

        player = 1
        turn = Label(self, text=("Player", str(player) + "'s", "turn"))
        turn.grid(row=0,columnspan=3,column=0)

        def rollDice():
            return

        roll = Button(myApp, text="Roll dice", command=rollDice)
        roll.grid(row=1,column=1)


if __name__== "__main__":
    myGame = Game()
    myGame.mainloop()











mainloop()