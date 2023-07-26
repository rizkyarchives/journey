# A game where a turtle must cross a road with many cars!
from turtle import Screen, Turtle
from player import Player
from scoreboard import Score
from car import Car
import time
import random

cars_list = []
screen = Screen()

screen.setup(width = 600, height = 600)
screen.title("Turtle is Crossing!")
screen.tracer(0)
screen.listen()

player = Player()
for i in range(75):
    cars_list.append(Car())
score = Score()

screen.onkeypress(player.forward, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    for car in cars_list:
        if random.random() <= 0.005 and random.random() >= 0.0:
            car.is_moving = True
        car.move()
        if car.collision(player.xcor(), player.ycor()):
            game_is_on = False
    if player.reach_finish_check():
        score.addScore()
        score.printScore()
        for car in cars_list:
            car.add_speed()
    screen.update()

score.gameOver()
screen.exitonclick()