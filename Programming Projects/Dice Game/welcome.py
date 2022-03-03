from tkinter import *
from playerdetails import players
#from main import username_input

class Welcome(Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome")
        self.geometry("400x400")
        wText = str("Welcome to Dice Roller")
        message = Label(self, text=wText)

        message.pack()

if __name__== "__main__":
    myApp = Welcome()
    myApp.mainloop()