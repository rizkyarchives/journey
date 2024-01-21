from turtle import Turtle
HEIGHT_SIZE = 600
SQUARE_SIZE = 20
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        with open("high_score.txt", "r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("white")
        self.setposition(x = 0, y = (HEIGHT_SIZE/2)-(SQUARE_SIZE * 1.5))

    def addScore(self):
        self.score += 1

    def writeScore(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", False, align= 'center', font=("Courier", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.writeScore()
    
    def game_over_text(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, align= 'center', font=("Courier", 20, "normal"))
