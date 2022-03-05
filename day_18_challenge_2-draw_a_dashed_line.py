from turtle import Turtle, Screen

# Creates a turtle
timmy = Turtle()


# Draw a dashed line
for _ in range(50):
    timmy.fd(10)
    timmy.pu()
    timmy.fd(10)
    timmy.pd()


screen = Screen()
screen.exitonclick()
