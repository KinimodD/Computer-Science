from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.title("Dice Game")

player = 1
turn = Label(root, text=("Player", str(player) + "'s", "turn"))
turn.grid(row=0,columnspan=3,column=1)

def rollDice():
    return

roll = Button(root, text="Roll dice", command=rollDice)
roll.grid(row=4,column=2)













mainloop()