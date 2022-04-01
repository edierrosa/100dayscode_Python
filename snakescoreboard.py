from turtle import Turtle


class Score(Turtle):
    """Create a scoreboard"""

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_game_data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.pu()
        self.goto(0, 275)
        self.color('white')
        self.update_score()

    def update_score(self):
        """Update the scoreboard"""
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", False,
                   'center', ('Courier', 15, 'normal'))

    def increase_score(self):
        """Increase game score"""
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     """Start game over sequence"""
    #     self.home()
    #     self.write(f"GAME OVER!", False,
    #                'center', ('Courier', 15, 'normal'))

    def reset(self):
        """Reset score"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_game_data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
