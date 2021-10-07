from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

#------------------------UI SETUP---------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=525, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")
canvas.create_image(403, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

#Labels
title = canvas.create_text(400, 150, text="French", font=("Arial", 30, "italic"))

word = canvas.create_text(400, 260, text="word", font=("Arial", 50, "bold"))

#Buttons
right_button = Button(image=right, highlightthickness=0)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong, highlightthickness=0)
wrong_button.grid(row=1, column=0)



window.mainloop()