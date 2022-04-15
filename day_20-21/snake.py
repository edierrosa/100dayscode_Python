from turtle import Turtle


MOVE_DISTANCE = 20


class Snake:
    """Model snakes"""

    def __init__(self):
        self.sections = []
        self.create_snake()
        self.head = self.sections[0]

    def create_snake(self):
        """Create a snake"""
        start_x = 0
        for _ in range(3):
            self.add_section((start_x, 0))
            start_x -= 20

    def add_section(self, position):
        "Add section to the snake"
        self.section = Turtle('square')
        self.section.color('white')
        self.section.pu()
        self.section.goto(position)
        self.sections.append(self.section)

    def reset(self):
        """Reset snake"""
        for _ in self.sections:
            _.goto(1000, 1000)
        self.sections.clear()
        self.create_snake()
        self.head = self.sections[0]

    def extend(self):
        "Extend the size of the snake"
        self.add_section(self.sections[-1].position())

    def move(self):
        """Move the snake"""
        for sec in range(len(self.sections) - 1, 0, -1):
            new_x = self.sections[sec - 1].xcor()
            new_y = self.sections[sec - 1].ycor()
            self.sections[sec].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        """Turn snake's head up"""
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        """Turn snake's head down"""
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        """Turn snake's head left"""
        if self.head.heading() != 0:
            self.head.seth(180)

    def right(self):
        """Turn snake's head right"""
        if self.head.heading() != 180:
            self.head.seth(0)
