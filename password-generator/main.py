from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

WHITE = "#fff"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def pwd_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letr = [choice(letters) for char in range(randint(8, 10))]
    sym = [choice(symbols) for char in range(randint(2, 4))]
    nmb = [choice(numbers) for char in range(randint(2, 4))]

    password_list = letr + sym + nmb
    shuffle(password_list)

    pwd = ''.join(password_list)

    pwd_input.insert(0, pwd)
    pyperclip.copy(pwd)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = web_input.get()
    email = email_input.get()
    pwd = pwd_input.get()
    new_data = {
        website: {
            "email": email,
            "password": pwd
            }
        }

    if web_input.get() == "" or pwd_input.get() == "":
        messagebox.showinfo(title="Error", message="You are missing some info")
    else:
        try:
            with open("./password-generator/data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("./password-generator/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("./password-generator/data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            pwd_input.delete(0, END)
            web_input.focus()


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = web_input.get()
    try:
        with open("./password-generator/data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']} \nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(message="No details for the website exists")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.minsize(width=300, height=300)
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="./password-generator/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website: ", bg=WHITE)
web_label.grid(column=0, row=1)
email_label = Label(text="Email/Username: ", bg=WHITE)
email_label.grid(column=0, row=2)
pwd_label = Label(text="Password: ", bg=WHITE)
pwd_label.grid(column=0, row=3)

# Inputs
web_input = Entry(width=35)
web_input.grid(column=1, row=1, sticky=W)
web_input.focus()
email_input = Entry(width=35)
email_input.insert(0, "matthewclifford@hotmail.co.uk")
email_input.grid(column=1, row=2, columnspan=2, sticky=W)
pwd_input = Entry(width=21)
pwd_input.grid(column=1, row=3, sticky=W)

# Button
search_btn = Button(text="Search", bg=WHITE, command=search_password)
search_btn.grid(column=2, row=1)
pwd_btn = Button(text="Generate Password", bg=WHITE, command=pwd_generator)
pwd_btn.grid(column=2, row=3)
add_btn = Button(text="Add", bg=WHITE, width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky=W)

window.mainloop()