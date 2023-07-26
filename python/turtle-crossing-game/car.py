from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.is_moving = False
        self.move_speed = STARTING_MOVE_DISTANCE
        self.goto(340, random.randint(-12, 12) * 20)
        self.setheading(180)
    
    def roadEnd_check(self):
        if self.xcor() <= -340:
            self.is_moving = False
            self.goto(340, random.randint(-12, 12) * 20)
            return True
        return False
    
    def move(self):
        if self.is_moving == True:
            self.fd(self.move_speed)
            return self.roadEnd_check()
                
    def add_speed(self):
        if self.move_speed != 25:
            self.move_speed += MOVE_INCREMENT

    def collision(self, player_x, player_y):
        if abs(self.xcor() - player_x)  < 28:
            if self.ycor() - player_y < 21 and self.ycor() - player_y >= 0:
                return True
            if self.ycor() - player_y > -20 and self.ycor() - player_y <= 0:
                return True
        return False
