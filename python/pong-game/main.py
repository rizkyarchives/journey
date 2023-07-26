# Classing Pong Arcade game
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import random
import time
game_is_on = True
WIDTH = 800
HEIGHT = 600
direction = [-1, 1]

def endgame():
    global game_is_on
    game_is_on = False

arena = Turtle()
arena.penup()
arena.color("white")
arena.shape("square")
arena.turtlesize(stretch_wid=30, stretch_len=0.1)
screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong-Game")
screen.tracer(0)
score = Score()

l_paddle = Paddle(-1*(WIDTH/2 - 50), 0)
r_paddle = Paddle((WIDTH/2 - 50), 0)
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.moveup, "Up")
screen.onkeypress(r_paddle.movedown, "Down")
screen.onkeypress(l_paddle.moveup, "w")
screen.onkeypress(l_paddle.movedown, "s")
screen.onkeypress(ball.printposition, "space")
screen.onkeypress(endgame, "Escape")

score.writeScore()

while game_is_on:
    if ball.xcor() >= 330 and ball.distance(r_paddle) <= 50:
        ball.xvector *= -1
        ball.move_speed *= 0.9
    if ball.xcor() <= -330 and ball.distance(l_paddle) <= 50:
        ball.xvector *= -1
        ball.move_speed *= 0.9
    if ball.xcor() > 410:
        ball.reset()
        ball.xvector = random.randint(-20, -10)
        ball.yvector = random.randint(5, 15) * random.choice(direction)
        score.addScore("left")
        score.writeScore()
    if ball.xcor() < -410:
        ball.reset()
        ball.xvector = random.randint(10, 20)
        ball.yvector = random.randint(5, 15) * random.choice(direction)
        score.addScore("right")
        score.writeScore()
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)

arena.hideturtle()
score.game_over()
screen.update()
screen.exitonclick()