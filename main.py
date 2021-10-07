from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
pair = {}
pairs = {}

#------------------------get data from csv file------------#

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    pairs = original_data.to_dict("records")
else:
    pairs = data.to_dict("records")


#---------------------get random word----------------------#


def get_word():
    global pair, flip_timer
    window.after_cancel(flip_timer)
    pair = random.choice(pairs)
    french_word = pair["French"]
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=french_word, fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)
#----------------------flip card and get translation--------#


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=pair["English"], fill="white")
#---------------------remove learned words and create to learn list---#


def remove_word():
    global pairs
    global pair
    pairs.remove(pair)
    pairs_frame = pandas.DataFrame(pairs)
    pairs_frame.to_csv("data/words_to_learn.csv", index=False)


#------------------------UI SETUP---------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=525, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")
canvas_image = canvas.create_image(403, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

#Labels
title = canvas.create_text(400, 150, text="Title", font=("Arial", 30, "italic"))

word = canvas.create_text(400, 260, text="word", font=("Arial", 50, "bold"))

#Buttons
right_button = Button(image=right, highlightthickness=0, command=lambda: [get_word(), remove_word()])
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong, highlightthickness=0, command=get_word)
wrong_button.grid(row=1, column=0)

get_word()


window.mainloop()