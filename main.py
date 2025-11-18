
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
WRONG_IMAGE="./images/wrong.png"
RIGHT_IMAGE="./images/right.png"
FRONT="./images/card_front.png"
BACK="./images/card_back,png"

window=Tk()
window.title("Flash Card")
window.config(padx=60,pady=40,bg=BACKGROUND_COLOR )

canvas=Canvas(width=800,height=600,highlightthickness=0,bg=BACKGROUND_COLOR)



bg_image=PhotoImage(file=FRONT)
canvas.create_image(400,300,image=bg_image)
canvas.create_text(400,200,text="ENGLISH" ,font=("Ariel",40,"italic"))

canvas.create_text(400,300,text="FRENCH" ,font=("Ariel",60,"bold"))

canvas.grid(column=1,row=1)

#Text and Meaning



#images setup
right=PhotoImage(file=RIGHT_IMAGE)
wrong=PhotoImage(file=WRONG_IMAGE)


#buttons

Button_x=Button(image=wrong,highlightthickness=0)
Button_x.grid(column=0,row=3)

Button_r=Button(image=right,highlightthickness=0)
Button_r.grid(column=3,row=3)

window.mainloop()
