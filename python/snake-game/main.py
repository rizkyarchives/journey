from turtle import Screen
from snake import Snake
from snakeFood import Food
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

food = Food()
snake = Snake()
score = Scoreboard()

screen.listen()
screen.onkeypress(fun = snake.up, key = "Up")
screen.onkeypress(fun = snake.down, key = "Down")
screen.onkeypress(fun = snake.left, key = "Left")
screen.onkeypress(fun = snake.right, key = "Right")
# screen.onkeypress(fun = snake.debug, key = "m")
# screen.onkeypress(fun = food.debug, key = "n")

slithering = True

def stop_slithering():
    global slithering
    slithering = False

screen.onkeypress(fun = stop_slithering, key = "m")
score.writeScore()

while slithering:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.ate_food(food.pos()):
        food.set_position()
        score.addScore()
        score.writeScore()
    if snake.wall_collision_check(SCREEN_WIDTH, SCREEN_HEIGHT) or snake.snake_collision_check():
        snake.reset()
        score.reset()

score.game_over_text()
screen.update()
screen.exitonclick()
