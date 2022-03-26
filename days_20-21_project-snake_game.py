from turtle import Screen
import time
from snake import Snake
from food import Food
from snakescoreboard import Score


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
game_score = Score()


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

XY_MAX = 285
XY_MIN = -285

start_game = True
while start_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        game_score.increase_score()

    # Collision with wall.
    if snake.head.xcor() > XY_MAX or snake.head.xcor() < XY_MIN or snake.head.ycor() > XY_MAX or snake.head.ycor() < XY_MIN:
        start_game = False
        game_score.game_over()

    # Collision with the tail.
    for _ in snake.sections[1:]:
        if snake.head.distance(_) < 10:
            start_game = False
            game_score.game_over()

screen.exitonclick()
