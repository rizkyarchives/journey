from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(xcor, ycor)
    
    def moveup(self):
        y = self.ycor()
        self.sety(y + 20)

    def movedown(self):
        y = self.ycor()
        self.sety(y - 20)