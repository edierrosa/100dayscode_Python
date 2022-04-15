from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


screen.listen()


def forwards():
    """Move Timmy forwards"""
    timmy.fd(20)


def backwards():
    """Move Timmy backrwards"""
    timmy.bk(20)


def c_clock():
    """Move Timmy counter clockwise"""
    timmy.lt(10)


def clockwise():
    """Move Timmy clockwise"""
    timmy.rt(10)


def clear_drawing():
    """Clear Tim's drawings and return inicial position"""
    timmy.speed(0)
    timmy.clear()
    timmy.pu()
    timmy.home()
    timmy.pd()
    timmy.speed(6)


screen.onkey(forwards, "w")
screen.onkey(backwards, "s")
screen.onkey(c_clock, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear_drawing, "c")


screen.exitonclick()
