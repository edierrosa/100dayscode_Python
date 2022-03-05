# import colorgram
import random
import turtle


# Creates a turtle
timmy = turtle.Turtle()
turtle.colormode(255)

# Extract RGB colours from image
# colours = colorgram.extract('image.jpg', 10)
# colours_rgb = []
# for _ in colours:
#     colours_rgb.append((_.rgb.r, _.rgb.g, _.rgb.b))

# Defines colour list
colour_list = [
    (235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237),
    (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234),
    (231, 168, 40), (184, 158, 46)
]


# Set turtle parameters
timmy.hideturtle()
timmy.speed('fastest')
timmy.penup()

# Set inicial position
timmy.setheading(225)
timmy.fd(300)
timmy.setheading(0)


def dot_painting(dots, space):
    """Creates a dot painting given dot size an space beetwen"""
    lines = 0
    while lines < dots:
        for _ in range(dots):
            timmy.dot(20, random.choice(colour_list))
            timmy.fd(space)
        timmy.bk(space * dots)
        timmy.lt(90)
        timmy.fd(space)
        timmy.rt(90)
        lines += 1


dot_painting(10, 50)


screen = turtle.Screen()
screen.exitonclick()
