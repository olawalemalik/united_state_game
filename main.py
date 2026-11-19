import turtle
import  pandas
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    state_answers = screen.textinput(title=f"{len(guessed_states)}/50 State correct",
                                     prompt="what state do you want me to guess?").title()
    if state_answers == "Exit":
        missing_states = []
        for state in state_list:
            if state  not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("state_to_learn.csv")
        break
    if state_answers in state_list:
        guessed_states.append(state_answers)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_name = data[data.state == state_answers]
        t.goto(state_name.x.item() ,state_name.y.item())
        t.write(state_answers)

    if state_answers  not in guessed_states:
        print(state_list not in guessed_states)





