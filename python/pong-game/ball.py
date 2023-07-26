from turtle import Turtle
import random
WIDTH = 800
HEIGHT = 600
direction = [-1, 1]
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.xvector= random.randint(10, 20) * random.choice(direction)
        self.yvector = random.randint(5, 15) * random.choice(direction)
        self.move_speed = 0.1
    
    def move(self):
        # if self.xcor() > 390 or self.xcor() < -390:
        #     self.xvector = -1 * self.xvector
        if self.ycor() > (HEIGHT/2) - 10 or self.ycor() < -1 * ((HEIGHT/2) - 10):
            self.yvector = -1 * self.yvector
        self.goto(self.xcor() + self.xvector, self.ycor() + self.yvector)

    def printposition(self):
        print(self.move_speed)
    
    def reset(self):
        self.setpos(0, 0)
        self.move_speed = 0.1