from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Udemy Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
french_label = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
french_word_label = canvas.create_text(400, 263, text="mot", font=("Arial", 60, "bold"))

# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, bd=0)
wrong_btn.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, bd=0)
right_btn.grid(column=1, row=1)


window.mainloop()
