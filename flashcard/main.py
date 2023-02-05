from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

def new_word():
    data_file = pandas.read_csv("./flashcard/data/spanish_words.csv")
    word_list = pandas.DataFrame(data_file)
    x = word_list.to_dict(orient="records")
    print(x)
    card_title.itemconfigure(text=)

window = Tk()
window.minsize(width=900, height=700)
window.title("Flashify")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = PhotoImage(file="./flashcard/images/card_front.png")
canvas.create_image(400, 263, image=card_img)
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Courier", 18, "italic"))
card_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Courier", 36, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file="flashcard\images\wrong.png")
correct_img = PhotoImage(file="flashcard/images/right.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=new_word)
correct_btn = Button(image=correct_img, highlightthickness=0, command=new_word)
wrong_btn.grid(column=0, row=1)
correct_btn.grid(column=1, row=1)


window.mainloop()