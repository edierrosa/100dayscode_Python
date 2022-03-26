from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        """Create scoreboard"""
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.pu()
        self.goto(-250, 250)
        self.color("black")
        self.update_level()

    def update_level(self):
        """Update scoreboard"""
        self.clear()
        self.write(f"Level: {self.level}", False,
                   "left", ("Courier", 15, "normal"))

    def increase_level(self):
        """Increase level score"""
        self.level += 1
        self.update_level()

    def game_over(self):
        """Start game over sequence"""
        self.home()
        self.write(f"GAME OVER!", False,
                   'center', ('Courier', 15, 'normal'))
