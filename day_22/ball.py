from turtle import Turtle


class Ball(Turtle):
    """Model the ball of the game"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("white")
        self.pu()
        self.move_x = 10
        self.move_y = 10
        self.level = 0.1

    def move_to(self):
        """Move the ball"""
        x = self.xcor() + self.move_x
        y = self.ycor() + self.move_y
        self.goto(x, y)

    def bounce_y(self):
        """Make the ball bounce in the y direction"""
        self.move_y *= -1

    def bounce_x(self):
        """Make the ball bounce in the x direction and increase level"""
        self.move_x *= -1
        self.level *= 0.9

    def reset_position(self):
        """Reset ball's position"""
        self.home()
        self.level = 0.1
