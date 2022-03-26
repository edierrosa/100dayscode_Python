from turtle import Turtle


class Scoreboard(Turtle):
    """Create game's scoreboard"""

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.pu()
        self.color('white')
        self.update_score()

    def update_score(self):
        """Update scoreboard"""
        self.goto(-100, 230)
        self.write(self.l_score, False, 'center', ('Courier', 40, 'normal'))
        self.goto(100, 230)
        self.write(self.r_score, False, 'center', ('Courier', 40, 'normal'))

    def increase_score(self, player):
        """Increase player's score"""
        if player == "right":
            self.r_score += 1
        elif player == "left":
            self.l_score += 1
        self.clear()
        self.update_score()
