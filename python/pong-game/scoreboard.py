from turtle import Turtle
HEIGHT = 600
WIDTH = 800

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, ((HEIGHT/2) - 40))
        self.rightscore = 0
        self.leftscore = 0
    
    def writeScore(self):
        self.clear()
        self.write(f"{self.leftscore}   {self.rightscore}", False, align= 'center', font=("Courier", 20, "normal"))
    
    def addScore(self, scorer):
        if scorer == "right":
            self.rightscore += 1
        elif scorer == "left":
            self.leftscore += 1
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, align= 'center', font=("Courier", 20, "normal"))
        self.goto(0, -50)
        if self.rightscore > self.leftscore:
            self.write(f"Right Side Won!", False, align= 'center', font=("Courier", 20, "normal"))
        elif self.rightscore < self.leftscore:
            self.write(f"Left Side Won!", False, align= 'center', font=("Courier", 20, "normal"))
        elif self.rightscore == self.leftscore:
            self.write(f"It's a Draw!", False, align= 'center', font=("Courier", 20, "normal"))


