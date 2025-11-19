
from tkinter import *

import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
WRONG_IMAGE="./images/wrong.png"
RIGHT_IMAGE="./images/right.png"
FRONT="./images/card_front.png"
BACK="./images/card_back,png"

data=pandas.read_csv("./data/french_words.csv")

in_dic=data.to_dict(orient="records")
def next_card():
    random_card=random.choice(in_dic)
    french=random_card["French"]
    english=random_card["English"]
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word,text=french)
window=Tk()
window.title("Flash Card")
window.config(padx=60,pady=40,bg=BACKGROUND_COLOR )

canvas=Canvas(width=700,height=500,highlightthickness=0,bg=BACKGROUND_COLOR)



bg_image=PhotoImage(file=FRONT)
canvas.create_image(350,200,image=bg_image)
card_title=canvas.create_text(350,200,text="ENGLISH" ,font=("Ariel",40,"italic"))

card_word=canvas.create_text(350,300,text="FRENCH" ,font=("Ariel",60,"bold"))

canvas.grid(column=1,row=1)

#Text and Meaning



#images setup
right=PhotoImage(file=RIGHT_IMAGE)
wrong=PhotoImage(file=WRONG_IMAGE)


#buttons

Button_x=Button(image=wrong,highlightthickness=0,command=next_card)
Button_x.grid(column=0,row=3)

Button_r=Button(image=right,highlightthickness=0,command=next_card)
Button_r.grid(column=3,row=3)
next_card()
window.mainloop()
