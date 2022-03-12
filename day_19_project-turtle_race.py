from random import randint
from turtle import Turtle, Screen
from tkinter import messagebox


screen = Screen()
screen.setup(600, 500)


colours = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

x = -280
y = -120
for colour in colours:
    turtle = Turtle(shape="turtle")
    turtle.color(colour)
    turtle.pu()
    turtle.goto(x, y)
    turtles.append(turtle)
    y += 40

user_bet = screen.textinput(
    "Make your bet", "Which turtle will win the race? Enter a colour: ")

race_start = True

while race_start:
    for turtle in turtles:
        if turtle.xcor() > 280:
            race_start = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                winner = f"Your {winning_turtle} turtle won!"
            else:
                winner = f"You've lost! The {winning_turtle} turtle finished first!"
            messagebox.showinfo(None, winner)
        turtle.fd(randint(0, 10))


screen.exitonclick()
