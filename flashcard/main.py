from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data_file = pandas.read_csv("./flashcard/data/words_to_learn.csv")
except FileNotFoundError:
    data_file = pandas.read_csv("./flashcard/data/spanish_words.csv")

word_list = data_file.to_dict(orient="records")
print(data_file)
current_card = {}

def correct_word():
    word_list.remove(current_card)
    pandas.DataFrame(word_list).to_csv("./flashcard/data/words_to_learn.csv", index=False)
    new_word()

def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_list)
    canvas.itemconfigure(card_title, text="Spanish", fill="black")
    canvas.itemconfigure(card_text, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(card, image=card_img_front)
    flip_timer = window.after(3000, func=show_translation)

def show_translation():
    canvas.itemconfigure(card_title, text="English", fill="white")
    canvas.itemconfigure(card_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card, image=card_img_back)
    
window = Tk()
window.minsize(width=900, height=700)
window.title("Flashify")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=show_translation)

# Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img_front = PhotoImage(file="./flashcard/images/card_front.png")
card_img_back = PhotoImage(file="./flashcard/images/card_back.png")
card = canvas.create_image(400, 263, image=card_img_front)
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Courier", 18, "italic"))
card_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Courier", 36, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file="flashcard\images\wrong.png")
correct_img = PhotoImage(file="flashcard/images/right.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=new_word)
correct_btn = Button(image=correct_img, highlightthickness=0, command=correct_word)
wrong_btn.grid(column=0, row=1)
correct_btn.grid(column=1, row=1)

new_word()

window.mainloop()