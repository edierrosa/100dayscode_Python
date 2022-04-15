from turtle import Turtle


MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        """Initialise player settings"""
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.seth(90)
        self.pu()
        self.start_line()

    def move(self):
        """Move turtle"""
        self.fd(MOVE_DISTANCE)

    def finished_crossing(self):
        """Detect finished crossing"""
        return self.ycor() > 280

    def start_line(self):
        """Return player to the start line"""
        self.goto(0, -280)
