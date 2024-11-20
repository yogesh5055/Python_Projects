from tkinter import *

#Window

window = Tk()
window.title("Minutes to Hour")
window.minsize(width=500,height=300)


minutes_input=Entry(width=10)
minutes_input.grid(row=0,column=1)

hour_show=Label(text="0")
hour_show.grid(row=1,column=1)


label = Label(text="equal to")
label.grid(column=0,row=1)

min_label = Label(text="Mintutes")
min_label.grid(column=3,row=0)

hr_label = Label(text="Hour")
hr_label.grid(column=3,row=1)

def min_to_hour():
    minutes = minutes_input.get()
    answer = int(minutes)/60
    hour_show.config(text=str(answer))
button = Button(text="Covert",command=min_to_hour)
button.grid(column=1,row=2)






window.mainloop()
