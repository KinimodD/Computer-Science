from msilib.schema import TextStyle
from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.title("Dice Game")

player = 1
turn = Label(root, text=("Player", str(player) + "'s", "turn"))
turn.pack()


roll = Button(root, text="Roll dice")
roll.pack()













mainloop()