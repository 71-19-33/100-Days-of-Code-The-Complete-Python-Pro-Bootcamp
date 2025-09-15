import turtle, pandas
from map_state_titles import StateTitles

#screen init
screen = turtle.Screen()
screen.screensize(725, 491)
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

#get x,y coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

#data init
data_input = pandas.read_csv("50_states.csv")
state_titles = StateTitles()
correct_guesses = []

#---game sequence---
#display text input box
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

while len(correct_guesses) < 50:
    if answer_state in data_input["state"].values and answer_state not in correct_guesses:
        x = data_input.loc[data_input["state"] == answer_state, "x"].iloc[0]
        y = data_input.loc[data_input["state"] == answer_state, "y"].iloc[0]
        state_titles.display_state_title(state_title=answer_state, x_coordinate=x, y_coordinate=y)
        correct_guesses.append(answer_state)
    if answer_state == "Exit":
        break
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?").title()

# save missing states to csv
states_list = data_input["state"].tolist()
states_to_learn = [item for item in states_list if item not in correct_guesses]
data_output = pandas.DataFrame(states_to_learn)
data_output.to_csv("states_to_learn.csv")

screen.exitonclick()