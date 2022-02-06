import turtle
import pandas

FONT = ("Courier", "8", "normal")

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

previously_corrected_guesses = []

df = pandas.read_csv("./50_states.csv")
states_list = df["state"].to_list()

while len(previously_corrected_guesses) < 50:
    answer = screen.textinput(title=f" {len(previously_corrected_guesses)}/50 Guess the state",
                              prompt="What is your next state's name?")
    answer_titled = answer.title()
    if answer_titled in states_list:
        if answer_titled not in previously_corrected_guesses:
            previously_corrected_guesses.append(answer_titled)
            state_turtle = turtle.Turtle()
            state_turtle.penup()
            state_turtle.hideturtle()
            state_df = df[df["state"] == answer_titled]
            state_turtle.goto(int(state_df["x"]), int(state_df["y"]))
            state_turtle.write(answer_titled, align="center", font=FONT)

screen.exitonclick()
