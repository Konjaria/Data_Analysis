import turtle
import pandas
from tkinter import messagebox
image_path = "Historical_provinces_of_Georgia.gif"
screen = turtle.Screen()

screen.title("Georgian States Knowledge")
screen.addshape(image_path)
turtle.shape(image_path)
# Get  x and y coordinates  while clicking onto the turtle screen
# *******************************************
# x_cors = []
# y_cors = []
#
#
# def get_mouse_click_coor(x, y):
#     print(x, y)
#     x_cors.append(x)
#     y_cors.append(y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
#
# data_dict = {
#     "province": ["Abkhazeti","Kodori Valley","Upper Svaneti","Lower Svaneti","Lechkhumi","Racha","Samachablo","Inner Kartli","Khevi"           ,"Mtiuleti","Khevsureti","Pshavi","Tusheti","Kakheti","Hereti","Ertso-Tianeti","Tbilisi","Lower Kartli","Borchalo","Trialeti","Javakheti","Tori","Samtskhe","Upper Kartli","Adjara","Imereti","Guria","Lazeti","Samegrelo","Samurzakano"],
#     "x": x_cors,
#     "y": y_cors
# }
# print(data_dict)
# df = pandas.DataFrame(data_dict)
# df.to_csv("History_of_Georgia.csv")
GUESS_COUNT = 0
guessed_states = []
missed_states = []
data = pandas.read_csv("History_of_Georgia.csv")
# Create a list of all the Provinces
province_list = data.province.to_list()
while len(guessed_states) < 30:
    answer_province = screen.textinput(title=f"{GUESS_COUNT}/30 correct answer",
                                       prompt="Guess the Historical province of Georgia ").title()
    if answer_province == "Exit":
        for states in province_list:
            if states not in guessed_states:
                missed_states.append(states)
        data_to_learn = pandas.DataFrame(missed_states)
        data_to_learn.to_csv("Provinces_to_learn.csv")
        screen.exitonclick()
    # Check whether we have correct input or not
    for province in province_list:
        if answer_province == province:
            if answer_province not in guessed_states:
                temp = turtle.Turtle()
                GUESS_COUNT += 1
                guessed_states.append(answer_province)
                temp.hideturtle()
                temp.penup()
                temp.color("Black")
                temp.goto(int(data[data.province == answer_province].x), int(data[data.province == answer_province].y))
                temp.write(answer_province)
            else:
                messagebox.showinfo(" 👀 Information", f"{answer_province} is correct, but you have provided twice")
                continue

screen.exitonclick()