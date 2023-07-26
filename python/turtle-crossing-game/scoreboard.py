from turtle import Turtle
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

FONT = ("Courier", 15, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.score = 0
        self.level = 1
        self.printScore()

    def printScore(self):
        self.clear()
        self.write(f"Score: {self.score}  Level: {self.level}", False, align ='left', font=FONT)

    def addScore(self):
        self.score += 1
        if self.level < (25 - STARTING_MOVE_DISTANCE)/MOVE_INCREMENT:
            self.level += 1

    def gameOver(self):
        self.goto(0,0)
        self.color("red")
        self.write("Game Over!", False, align ='center', font=FONT)
