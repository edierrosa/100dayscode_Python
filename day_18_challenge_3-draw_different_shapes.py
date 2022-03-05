import random
from turtle import Turtle, Screen

# Creates a turtle
timmy = Turtle()


# Drawing different shapes
def draw_form(form_sides, colour):
    degree_angle = 360 / form_sides
    timmy.color(colour)
    for _ in range(form_sides):
        timmy.fd(100)
        timmy.right(degree_angle)


colours = ['blue', 'red', 'green', 'purple', 'orange',
           'olive', 'bisque', 'sienna', 'pink', 'brown', 'teal']

for _ in range(3, 11):
    draw_form(_, random.choice(colours))


screen = Screen()
screen.exitonclick()
