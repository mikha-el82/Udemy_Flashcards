from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- CREATE FLASHCARDS ------------------------------- #
cards_df = pandas.read_csv("data/french_words.csv")
cards_to_learn = cards_df.to_dict(orient="records")

# ---------------------------- GET NEW FLASHCARD ------------------------------- #
def get_next_card():
    new_card = random.choice(cards_to_learn)
    french_word = new_card["French"]
    english_word = new_card["English"]
    print(f"This is the couple: {french_word} - {english_word}")
    canvas.itemconfig(language_label, text="French")
    canvas.itemconfig(word_label, text=french_word)

# ---------------------------- FLIP FLASHCARD ------------------------------- #


def flip_card(english_word):
    # pass
    canvas.itemconfig(language_label, text="English")
    canvas.itemconfig(word_label, text=english_word)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Udemy Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
language_label = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 263, text="mot", font=("Arial", 60, "bold"))
card_back_img = PhotoImage(file="images/card_back.png")


# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, bd=0, command=get_next_card)
wrong_btn.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, bd=0, command=get_next_card)
right_btn.grid(column=1, row=1)

get_next_card()

window.mainloop()
