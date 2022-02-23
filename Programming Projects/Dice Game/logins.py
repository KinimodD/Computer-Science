from tkinter import *
from tkinter import messagebox
from playerdetails import players

root = Tk()
root.title("Player 1 Login")
root.geometry("250x125")
root.resizable(False,False)

player1loggedin = False
player2loggedin = False

my_frame = LabelFrame(root, padx=10,pady=10)
my_frame.pack(pady=10, padx=10)


username_label = Label(my_frame, text="Username:")#Label
username_label.grid(row=0,column=0)

username_input = Entry(my_frame)#Entry
username_input.grid(row=0,column=1)


password_label = Label(my_frame, text="Password:")#Label
password_label.grid(row=1, column=0)

password_input = Entry(my_frame, show="*")#Entry
password_input.grid(row=1,column=1)


def signin():
    try:
        if players[username_input.get()] != password_input.get():
            messagebox.showerror("KeyError", "Incorrect password")
        else:
            global player1loggedin
            player1loggedin = True
            
            
            
            
    except KeyError:
        messagebox.showerror("KeyError", "Incorrect username")
    

def register():
    return
    
signregframe = LabelFrame(my_frame)
signregframe.grid(row=2, column=0, pady=5, columnspan=2)

sign_up = Button(signregframe,text="Sign In", command=signin)
sign_up.grid(row=0, column=0, pady=5,padx=5)

sign_up = Button(signregframe,text="Register", command=register)
sign_up.grid(row=0, column=1, pady=5,padx=5)







mainloop()