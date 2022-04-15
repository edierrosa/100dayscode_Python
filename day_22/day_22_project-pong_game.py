from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from pongscoreboard import Scoreboard

# Set game screen
screen = Screen()
screen.title("Pong Game")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)


# Set initial parameters
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
score = Scoreboard()


# Set keyboard commands
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


# Start game
start_game = True
while start_game:
    time.sleep(ball.level)
    screen.update()
    ball.move_to()

    # Collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with paddles.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Right paddle miss
    if ball.xcor() > 400:
        ball.reset_position()
        ball.bounce_x()
        score.increase_score("left")

    # Left paddle miss
    if ball.xcor() < -400:
        ball.reset_position()
        ball.bounce_x()
        score.increase_score("right")

screen.exitonclick()
