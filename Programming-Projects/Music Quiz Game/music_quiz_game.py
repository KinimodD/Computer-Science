from userdetails import users

answerreg = input("Login or Register?\n")
if answerreg == "login" or answerreg == "Login" or answerreg =="l":
    username = input("Username:\n")
    password = input("Password:\n")
    try:
        users[username]
        print("Username Correct")
    except KeyError:
        print("Enter a valid username")

elif answerreg == "register" or answerreg == "Register" or answerreg =="r":
    username = input("Username:\n")
    password = input("Password:\n")