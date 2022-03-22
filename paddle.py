from turtle import Turtle


MOVE_DISTANCE = 20


class Paddle(Turtle):
    """Model paddles"""

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.pu()
        self.goto(position, 0)

    def up(self):
        """Move paddle up"""
        self.goto(self.xcor(),
                  (self.ycor() + MOVE_DISTANCE))

    def down(self):
        """Move paddle down"""
        self.goto(self.xcor(),
                  (self.ycor() - MOVE_DISTANCE))
