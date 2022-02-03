from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Dice Game")
root.resizable(False,False)


my_frame = LabelFrame(root, padx=10,pady=10)
my_frame.pack(pady=10, padx=10)

username_label = Label(my_frame, text="Username:")#Label
username_label.grid(row=0,column=0)

username_input = Entry(my_frame)#Entry
username_input.grid(row=0,column=1)
##########################################
password_label = Label(my_frame, text="Password:")#Label
password_label.grid(row=1, column=0)

password_input = Entry(my_frame, show="*")#Entry
password_input.grid(row=1,column=1)
###########################################
def click():
    my_text = Label(my_frame, text="Incorrect")
    my_text.grid(row=3,column=0)
    

sign_up = Button(my_frame,text="Sign In", command=click)
sign_up.grid(row=2, column=1, columnspan=2, pady=5)

mainloop()