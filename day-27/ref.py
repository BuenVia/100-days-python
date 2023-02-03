from tkinter import *

def button_clicked():
    my_label.config(text=input.get())

# Define the window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label", font=("Ariel", 24, "normal"))
my_label.grid(column=0, row=0)
my_label.config(padx=100, pady=100)

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# Text entry
input = Entry(width=10)
input.grid(column=3, row=2)

button_two = Button(text="Second Button")
button_two.grid(column=2, row=0)





window.mainloop()