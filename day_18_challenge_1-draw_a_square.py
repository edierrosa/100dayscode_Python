from turtle import Turtle, Screen

# Creates a turtle
timmy = Turtle()

# Draw a square
for _ in range(4):
    timmy.fd(100)
    timmy.right(90)

screen = Screen()
screen.exitonclick()
