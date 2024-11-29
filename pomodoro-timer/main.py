from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    screen.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    labl.config(text="Timer")
    check.config(text="")
    global REPS
    REPS=0




# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS+=1
    if REPS%2 == 0 :
        labl.config(text="BREAK",bg=GREEN,highlightthickness=0,fg=RED)
        time=SHORT_BREAK_MIN*60
        counter(time)
    elif REPS%8 == 0:
        labl.config(text="BREAK",bg=GREEN,highlightthickness=0,fg=RED)
        time=LONG_BREAK_MIN*60
        counter(time)
    else:
        labl.config(text="WORK",bg=GREEN,highlightthickness=0,fg=RED)
        time=WORK_MIN*60
        counter(time)

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counter(count):
    min=math.floor(count/60)
    sec=count%60
    if sec<10:
        sec=f"0{sec}"
    global timer
    canvas.itemconfig(timer_text,text=f"{min}:{sec}")
    if count>0:
       timer=screen.after(1000,counter,count-1)
    else:
        start_timer()
        marks=""
        for _ in range(math.floor(REPS/2)):
            marks+="✔️"
        check.config(text=marks)
    




# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Promodora")
screen.config(padx=100,pady=60,bg=GREEN)



labl=Label(text="Timer",bg=GREEN,highlightthickness=0,font=("Cambria",45,"bold"),fg=RED)
labl.grid(row=0,column=1)




canvas = Canvas(width=400,height=500,highlightthickness=0,bg=GREEN)
apple_img=PhotoImage(file="apple.png")
canvas.create_image(200,250,image=apple_img)
timer_text=canvas.create_text(200,300,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)


start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="reset",highlightthickness=0,command=reset)
reset_button.grid(column=2,row=2)

check=Label(fg="black",bg=GREEN)
check.grid(row=2,column=1)





screen.mainloop()
