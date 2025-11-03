BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas, random

#---Window---
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")

#---Data---
try:
    csv_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    csv_data = pandas.read_csv("data/french_words_test.csv")

vocabulary_list = csv_data.to_dict(orient="records")
WORD_PAIR = {}

#---Functions---
def flip_card():
    global WORD_PAIR
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(vocabulary_text, text=WORD_PAIR["English"], fill="white")

def new_word_pair():
    global WORD_PAIR
    WORD_PAIR = random.choice(vocabulary_list)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(vocabulary_text, text=WORD_PAIR["French"], fill="black")
    window.after(3000, flip_card)

def word_pair_is_learned():
    vocabulary_list.remove(WORD_PAIR)
    csv_data_new = pandas.DataFrame(vocabulary_list)
    csv_data_new.to_csv("data/words_to_learn.csv", index=False)
    window.after(3000, new_word_pair)

#---UI---
##---column_0---
###---Canvas---
canvas = Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
vocabulary_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
###---Wrong button---
wrong = PhotoImage(file="images/wrong.png")
button0_1 = Button(image=wrong, highlightthickness=0, command=new_word_pair)
button0_1.grid(row=1, column=0)
##---column_1---
###---Right button---
right = PhotoImage(file="images/right.png")
button1_1 = Button(image=right, highlightthickness=0, command=word_pair_is_learned)
button1_1.grid(row=1, column=1)

new_word_pair()
#---END---
window.mainloop()
