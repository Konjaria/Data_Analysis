import turtle
import pandas
Guessed_states = 0
All_states = 50

screen = turtle.Screen()
screen.title("Unites States Knowledge Checking")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()


def check_answer_state(guess):
    if guess in state_list:
        return True
    else:
        return False


# Correct guesses List
correct_guesses = []

while len(correct_guesses) < 50:
    #  Convert the answer state into Title case
    answer_state = screen.textinput(title=f"{Guessed_states}/{All_states} states guessed", prompt="What's another state of U.S.").title()
    if answer_state == "Exit":
        print("I am here")
        missing_states = []
        for state in state_list:
            if state not in correct_guesses:
                missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break

    # Check if it  is one of U.S. state
    guess_is_a_state = check_answer_state(answer_state)
    # Write correct guesses onto the map
    if guess_is_a_state:
        Guessed_states += 1
        correct_guesses.append(answer_state)
        founded_row = data[data.state == answer_state]
        x_cor = int(founded_row["x"])
        y_cor = int(founded_row["y"])
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(x_cor, y_cor)
        state.write(answer_state)
