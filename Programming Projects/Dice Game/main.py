from tkinter import *
from tkinter import messagebox
from playerdetails import players


class Window(Tk):
    def __init__(self):
        super().__init__()
        global player1loggedin
        global player2loggedin
        self.geometry("400x400")
        self.title("Dice Roller")
        self.resizable(0,0)

        self.title("Login")
        self.geometry("250x175")
        self.resizable(False,False)

        player1loggedin = False
        player2loggedin = False

        my_frame = LabelFrame(self, padx=10,pady=10)
        my_frame.pack(pady=(5,0), padx=10)


        username_label = Label(my_frame, text="Username:")#Label
        username_label.grid(row=0,column=0)

        username_input = Entry(my_frame)#Entry
        username_input.grid(row=0,column=1)


        password_label = Label(my_frame, text="Password:")#Label
        password_label.grid(row=1, column=0)

        password_input = Entry(my_frame, show="*")#Entry
        password_input.grid(row=1,column=1)


        def signin():
            global player1loggedin
            global player2loggedin

            if player1loggedin == True:
                try:
                    if players[username_input.get()] != password_input.get():
                        messagebox.showerror("KeyError", "Incorrect password")
                    else:
                        
                        player2loggedin = True

                        ready2 = Label(self, text="Player 2 ready")#Label
                        ready2.pack()

                        exec(open("Computer-Science\Programming Projects\Dice Game\welcome.py").read())


                        
                        
                        
                        
                except KeyError:
                    messagebox.showerror("KeyError", "Incorrect username")
            else:

                try:
                    if players[username_input.get()] != password_input.get():
                        messagebox.showerror("KeyError", "Incorrect password")
                    else:
                        
                        player1loggedin = True

                        ready1 = Label(self, text="Player 1 ready")#Label
                        ready1.pack()

                        username_input.delete(0, END)
                        password_input.delete(0, END)


                        
                        
                        
                        
                except KeyError:
                    messagebox.showerror("KeyError", "Incorrect username")
            

        def register(username,password):
            players[username] = password
            
        signregframe = LabelFrame(my_frame)
        signregframe.grid(row=2, column=0, pady=5, columnspan=2)

        sign_up = Button(signregframe,text="Sign In", command=signin)
        sign_up.grid(row=0, column=0, pady=5,padx=5)

        sign_up = Button(signregframe,text="Register", command=lambda: register(username_input.get(), password_input.get()))
        sign_up.grid(row=0, column=1, pady=5,padx=5)











if __name__== "__main__":
    myApp = Window()
    myApp.mainloop()