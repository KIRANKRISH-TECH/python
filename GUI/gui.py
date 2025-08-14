
from tkinter import *
insta = Tk()
insta.title("Login Page")
insta.geometry("5000x4000")


def login():
    print("Login button clicked")
    

username_entry = Entry(insta, width=30)
username_entry.grid(row=0, column=1, padx=20, pady=10)
username_entry.insert(0, "Enter Username")


password_entry = Entry(insta, width=30,)
password_entry.grid(row=1, column=1, padx=20, pady=10)
password_entry.insert(0, "Enter Password")




login_button = Button(insta, text="Login", command=login)
login_button.grid(row=2, column=1, padx=20, pady=10)



path = PhotoImage(file="C:/Users/Krish/Downloads/insta.png.png")
label_image = Label(insta, image=path)
label_image.grid(row=3, column=1, padx=20, pady=10)




insta.mainloop()






