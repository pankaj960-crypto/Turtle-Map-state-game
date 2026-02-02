import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("India Map Game")
screen.bgpic("new_india_state.gif")

data = pd.read_csv("new_india_state.csv")
all_states = data.state.to_list()
guessed_states = []

# This loop keeps the game running
while len(guessed_states) < len(all_states):
    user_guess = screen.textinput(
        title=f"{len(guessed_states)}/{len(all_states)} States Correct",
        prompt="Enter a state name (or 'Exit' to quit):"
    )

    if user_guess:
        user_guess = user_guess.title()

    # Secret exit command
    if user_guess == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break


    if user_guess in all_states and user_guess not in guessed_states:
        guessed_states.append(user_guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_row = data[data.state == user_guess]
        t.goto(int(state_row.x.item()), int(state_row.y.item()))
        t.write(user_guess)

# Keeps the window open after the loop ends
screen.mainloop()