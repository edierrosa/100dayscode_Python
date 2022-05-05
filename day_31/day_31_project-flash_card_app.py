import random
from tkinter import *
import pandas as pd


# Create global variables
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# Create global dictionaries
card = {}
learn_vocab = {}


# Import data
try:
    data = pd.read_csv("./day_31/data/vocab_to_learn.csv")
except FileNotFoundError:
    previous_data = pd.read_csv("./day_31/data/french_words.csv")
    learn_vocab = previous_data.to_dict(orient="records")
else:
    learn_vocab = data.to_dict(orient="records")


# Functions
def create_card():
    """Generate a card from learn_vocab words"""
    global card, card_timer
    window.after_cancel(card_timer)
    card = random.choice(learn_vocab)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(language_word, text=card["French"], fill="black")
    canvas.itemconfig(background_image, image=front_image)
    card_timer = window.after(ms=3000, func=english_translation)


def english_translation():
    """Generate the translation card from learn_vocab words"""
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(language_word, text=card["English"], fill="white")
    canvas.itemconfig(background_image, image=back_image)


def known_word():
    """Remove known word from learn_vocab words and save to csv file"""
    learn_vocab.remove(card)
    create_card()
    data = pd.DataFrame(learn_vocab)
    data.to_csv("./day_31/data/vocab_to_learn.csv", index=False)


# UI Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# Set card timer
card_timer = window.after(ms=3000, func=english_translation)


# Canvas
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)


# Canvas image
front_image = PhotoImage(file="./day_31/images/card_front.png")
back_image = PhotoImage(file="./day_31/images/card_back.png")
background_image = canvas.create_image(400, 263, image=front_image)


# Canvas texts
language_text = canvas.create_text(
    400, 150, text="", font=(FONT_NAME, 40, "italic"))
language_word = canvas.create_text(
    400, 288, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
right_image = PhotoImage(file="./day_31/images/right.png")
right_button = Button(
    image=right_image, activebackground=BACKGROUND_COLOR, highlightthickness=0, border=0, command=known_word)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="./day_31/images/wrong.png")
wrong_button = Button(
    image=wrong_image, activebackground=BACKGROUND_COLOR,
    highlightthickness=0, border=0, command=create_card)
wrong_button.grid(column=0, row=1)


create_card()


window.mainloop()
