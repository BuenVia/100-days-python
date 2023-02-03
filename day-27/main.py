from tkinter import *

def listbox_used(e):
    return listbox.get(listbox.curselection())

def miles_km():
    miles_to_km = float(input.get()) * 1.6
    answer.config(text=round(miles_to_km, 2))


window = Tk()
window.minsize(width=150, height=100)
window.title("Miles to KM Converter")
window.config(padx=25, pady=25)

# List conversions
listbox = Listbox(height=3)
options = ["Miles to KM", "KM to Miles", "CM to Inches", "Inches to CM", "Celsius to Farenheit", "Farenheit to Celsius"]
for option in options:
    listbox.insert(options.index(option), option)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=1, row=0)



# Text input
input = Entry(width=10)
input.grid(column=1, row=2)

# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=0, row=2)


answer = Label(text=0)
answer.grid(column=4, row=2)

km = Label(text="KM")
km.grid(column=2, row=2)

# Button
button = Button(text="Calculate", command=miles_km)
button.grid(column=1, row=3)


window.mainloop()
