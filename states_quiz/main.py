import turtle
import pandas
from answer import Answer

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        r_states = [state for state in all_states if state not in guessed_states]
        rem = pandas.DataFrame(r_states)
        rem.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        answer = Answer(int(state_data.x), int(state_data.y), answer_state)

