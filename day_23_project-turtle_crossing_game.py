from turtle import Screen
import time
from player import Player
from carmanager import CarManager
from turtlecrossscoreboard import Scoreboard

# Set game's screen
screen = Screen()
screen.title("Turtle Crossing")
screen.setup(600, 600)
screen.bgcolor("white")
screen.tracer(0)

# Set initial parameters
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Set keybord commands
screen.listen()
screen.onkey(player.move, "Up")


start_game = True
while start_game:
    time.sleep(0.1)
    screen.update()

    # Create cars
    car_manager.new_car()
    car_manager.move_cars()

    # Detect collision
    for _ in car_manager.cars:
        if _.distance(player) < 20:
            start_game = False
            scoreboard.game_over()

    # Successful crossing
    if player.finished_crossing():
        player.start_line()
        car_manager.speed_up()
        scoreboard.increase_level()

screen.exitonclick()
