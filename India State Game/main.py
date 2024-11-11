import turtle 
import pandas as pd

data=pd.read_csv("states_data.csv")
screen=turtle.Screen()
screen.title("India State Game")
image="India-state.gif"
screen.addshape(image)
turtle.shape(image)
state_list=data.state.to_list()

guessed_state =[]
while len(guessed_state)<29:
    answer_state =screen.textinput(title=f"Your Score : {len(guessed_state)}/30",prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_state:
                missing_states.append(state)
        unknown_state = pd.DataFrame(missing_states)
        unknown_state.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        guessed_state.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)


screen.mainloop()