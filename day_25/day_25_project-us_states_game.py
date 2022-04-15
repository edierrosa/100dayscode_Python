import turtle
import pandas as pd
from state import State

# Set the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Set variables
states_data = pd.read_csv("./50_states.csv")
states = states_data.state.to_list()

# Start game
while len(states) > 0:
    answer = (screen.textinput(
        f"{50 - len(states)}/50 States Correct", "What's another State's name?")).title()
    # Exit the game and creates a csv file of missing states
    if answer == "Exit":
        missing_states_df = pd.DataFrame(states)
        missing_states_df.to_csv("what_to_learn.csv")
        break
    # Call function to write the state's name on map
    if answer in states:
        states.remove(answer)
        state = states_data[states_data.state == answer]
        new_state = State(state.state.item(), int(state.x), int(state.y))

# Keep the screen to visualse the map
screen.exitonclick()
