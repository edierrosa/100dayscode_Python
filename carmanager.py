from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVING_INCREMENT = 10


class CarManager():

    def __init__(self):
        """Set car manager"""
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        """Create a new car"""
        if random.randint(1, 6) == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(1, 2)
            car.pu()
            car.color(random.choice(COLORS))
            car.goto(305, random.randint(-250, 250))
            car.seth(180)
            self.cars.append(car)

    def move_cars(self):
        """Move cars"""
        for _ in self.cars:
            _.fd(self.speed)

    def speed_up(self):
        """Increase car's speed"""
        self.speed += MOVING_INCREMENT
