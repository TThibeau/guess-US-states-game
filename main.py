import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score=0
FONT = ('Arial',12,'bold')
guessed_states = []

df = pandas.read_csv("50_states.csv")
states_list = df.state.to_list()
to_learn_list = []

while score<50:

    user_input = screen.textinput(title=f"{score}/50 states correct", prompt="What's another state's name? ")
    user_input = " ".join(s.capitalize() for s in user_input.split())

    if user_input == "Exit":
        to_learn_list = [state for state in states_list if state not in guessed_states]
        
        new_df = pandas.DataFrame(to_learn_list)
        
        new_df.to_csv("states_to_learn.csv")
        break

    if user_input in states_list:
        guessed_states.append(user_input)
        x_cor = df[df.state == user_input].x.item()
        y_cor = df[df.state == user_input].y.item()
        
        score += 1

        word = turtle.Turtle()
        word.penup()
        word.color("black")
        word.hideturtle()
        word.goto(x_cor,y_cor)
        word.write(f"{user_input}", move=False,align="center", font=FONT)
