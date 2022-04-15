import random
import turtle


# Creates a turtle
timmy = turtle.Turtle()
turtle.colormode(255)


def random_colour():
    """Returns RGB random colour"""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


timmy.speed('fastest')


def draw_spirograph(size):
    """Draws a spirograph"""
    for _ in range(int(360 / size)):
        timmy.color(random_colour())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size)


draw_spirograph(5)


screen = turtle.Screen()
screen.exitonclick()
