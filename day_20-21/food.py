from random import randint
from turtle import Turtle


class Food(Turtle):
    """Model food"""

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.shapesize(0.5, 0.5)
        self.color('green')
        self.speed(0)
        self.refresh()

    def refresh(self):
        """Dispense food at new position"""
        food_x = randint(-280, 280)
        food_y = randint(-280, 280)
        self.goto(food_x, food_y)
