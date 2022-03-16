from mimetypes import init
from turtle import Turtle


class Score(Turtle):
    """Create a scoreboard"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pu()
        self.goto(0, 275)
        self.color('white')
        self.update_score()

    def update_score(self):
        """Update the scoreboard"""
        self.write(f"Score: {self.score}", False,
                   'center', ('Courier', 15, 'normal'))

    def increase_score(self):
        """Increase game score"""
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        """Start game over sequence"""
        self.home()
        self.write(f"GAME OVER!", False,
                   'center', ('Courier', 15, 'normal'))
