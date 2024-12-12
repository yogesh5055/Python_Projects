BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random
current_card = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
     orginal_data = pd.read_csv("data/french_words.csv")
     to_learn = orginal_data.to_dict(orient="records")
else:
     to_learn = data.to_dict(orient="records")



def next_card():
    global current_card,flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill='black')
    canvas.itemconfig(card_word,text=current_card['French'],fill='black')
    canvas.itemconfig(card_background,image=front_image)
    flip_timer = screen.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English",fill='white')
    canvas.itemconfig(card_word,text=current_card['English'],fill='white')
    canvas.itemconfig(card_background,image=new_image)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")

screen = Tk()
screen.title("Flash Card")
screen.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = screen.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526)

new_image = PhotoImage(file="images/card_back.png")
canvas.create_image(400,263,image=new_image)

front_image = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400,263,image=front_image)
card_title = canvas.create_text(400,150,text="",font=('Arial',40,'italic'))
card_word = canvas.create_text(400,263,text="",font=('Arial',40,'bold'))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img,bg=BACKGROUND_COLOR,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_mark = PhotoImage(file="images/right.png")
known_button = Button(image=check_mark,bg=BACKGROUND_COLOR,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)

next_card()


screen.mainloop()