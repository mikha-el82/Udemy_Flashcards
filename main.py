from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- CREATE FLASHCARDS ------------------------------- #

try:
    cards_df = pandas.read_csv("data/words_to_learn.csv")
    cards_to_learn = cards_df.to_dict(orient="records")
except FileNotFoundError:
    print("File not found... using general file 'french_words.csv'")
    cards_df = pandas.read_csv("data/french_words.csv")
    cards_to_learn = cards_df.to_dict(orient="records")  # list of dictionaries


current_card = {}


def get_next_card():
    global current_card
    global flipper
    window.after_cancel(flipper)
    current_card = random.choice(cards_to_learn)
    french_word = current_card["French"]
    english_word = current_card["English"]
    print(current_card)
    print(f"This is the couple: {french_word} - {english_word}")
    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(language_label, fill="black")
    canvas.itemconfig(language_label, text="French")
    canvas.itemconfig(word_label, fill="black")
    canvas.itemconfig(word_label, text=french_word)
    flipper = window.after(3000, flip_card)


# ---------------------------- FLIP FLASHCARD ------------------------------- #


def flip_card():
    english_word = current_card["English"]
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(language_label, fill="white")
    canvas.itemconfig(language_label, text="English")
    canvas.itemconfig(word_label, fill="white")
    canvas.itemconfig(word_label, text=english_word)
    print("Flipping")

# ---------------------------- UI SETUP ------------------------------- #

def remove_card():
    cards_to_learn.remove(current_card)
    # cards_to_learn.to_csv("data/cards.csv", index=False)
    print(len(cards_to_learn))

    get_next_card()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Udemy Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flipper = window.after(3000, flip_card)

# Card Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
language_label = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 263, text="mot", font=("Arial", 60, "bold"))
card_back_img = PhotoImage(file="images/card_back.png")


# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, bd=0, command=get_next_card)
wrong_btn.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, bd=0, command=remove_card)
right_btn.grid(column=1, row=1)

get_next_card()

window.mainloop()
