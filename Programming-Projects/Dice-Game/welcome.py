from tkinter import *
#from login import player1name
from game import Game
from PIL import Image,ImageTk

class Welcome(Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome")
        self.geometry("400x400")
        
        #self.playerswelcome = player1name

        #Welcome Message
        #self.message = Label(self, text=f"Welcome to Dice Roller, {self.playerswelcome}")
        #self.message.pack()


        #Image
        self.dice = Image.open("GitHub\Computer-Science\Programming-Projects\Dice-Game\dice.jpg")
        #self.dice = self.dice.resize((100,100), Image.ANTIALIAS)
        self.diceimg = ImageTk.PhotoImage(self.dice)
        self.imagelbl = Label(self, image=self.diceimg)
        self.imagelbl.config(image=self.diceimg)
        self.imagelbl.pack()

        def play():
            self.destroy()
            gameWindow = Game()
            gameWindow.mainloop()

        self.playbtn = Button(self, text="Play", command=play, padx=50)
        self.playbtn.pack()
        