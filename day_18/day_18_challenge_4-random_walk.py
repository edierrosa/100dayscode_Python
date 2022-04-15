import random
import turtle


# Creates a turtle
timmy = turtle.Turtle()
turtle.colormode(255)

# Colours list
# colours = ['blue', 'red', 'green', 'purple', 'orange',
#            'olive', 'bisque', 'sienna', 'pink', 'brown', 'teal']


def random_colour():
    """Returns RGB random colour"""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# Random walk
directions = [0, 90, 180, 270]
for _ in range(200):
    timmy.speed('fast')
    timmy.pensize(5)
    # timmy.color(random.choice(colours))
    timmy.color(random_colour())
    timmy.fd(50)
    timmy.setheading(random.choice(directions))


screen = turtle.Screen()
screen.exitonclick()
