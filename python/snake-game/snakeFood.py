from turtle import Turtle, Screen
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SNAKE_SIZE = 20

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.x_possible_pos = (SCREEN_WIDTH/2 - SNAKE_SIZE)/SNAKE_SIZE
        self.y_possible_pos = (SCREEN_HEIGHT/2 - SNAKE_SIZE)/SNAKE_SIZE
        self.shape("circle")
        self.shapesize(stretch_wid = 0.5, stretch_len = 0.5)
        self.penup()
        self.color("red")
        self.set_position()

    def set_position(self):
        self.setposition(x = SNAKE_SIZE * random.randint(-1 * self.x_possible_pos, self.x_possible_pos), y = SNAKE_SIZE * random.randint(-1 * self.y_possible_pos, self.y_possible_pos - 1)) #-1 biar ada space for scoreboard text

    def debug(self):
        print(self.pos())

# screen = Screen()

# food = Food()
# print(SNAKE_SIZE * random.randint(-1 * food.x_possible_pos, food.x_possible_pos))
# print(SNAKE_SIZE * random.randint(-1 * food.y_possible_pos, food.y_possible_pos))

# screen.exitonclick()