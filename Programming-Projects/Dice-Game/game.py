from tkinter import *
import random
from PIL import Image, ImageTk

class Game(Tk):
    def __init__(self):
        super().__init__()
        self.title("Dice Game")
        self.geometry("500x500")

        self.player = 1
        self.turn = Label(self, text=("Player", str(self.player) + "'s", "turn"))
        self.turn.grid(row=0,columnspan=3,column=0)

        def rollDice():
            return

        self.roll = Button(self, text="Roll dice", command=rollDice)
        self.roll.grid(row=1,column=1)