from tkinter import *
from logins import root
import random
from PIL import Image, ImageTk
root.destroy()


root = Tk()
root.title("Dice Game")
root.geometry("500x500")

player = 1
turn = Label(root, text=("Player", str(player) + "'s", "turn"))
turn.grid(row=0,columnspan=3,column=0)

def rollDice():
    return

roll = Button(root, text="Roll dice", command=rollDice)
roll.grid(row=1,column=1)













mainloop()