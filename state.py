from turtle import Turtle


class State(Turtle):

    def __init__(self, state, x, y):
        """Print State's name on map"""
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(x, y)
        self.write(f"{state}", False, "center", ('Courier', 11, 'bold'))
