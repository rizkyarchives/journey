from turtle import Turtle
DISTANCE = 20
SQUARE_SIZE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Snake:
    def __init__(self):
        self.xcor = 0
        self.snakes = [] #self.snakes[0] = snake's head
        self.new_snake_pos = [0, 0] #initialize
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            snek = Turtle(shape = "square")
            snek.speed("slowest")
            snek.penup()
            snek.color("white")
            snek.goto(x = self.xcor, y = 0)
            self.xcor -= SQUARE_SIZE
            self.snakes.append(snek)
    
    def move(self):
        for j in range(len(self.snakes) - 1, 0, -1):
            self.snakes[j].goto(self.snakes[j - 1].pos())
        self.snakes[0].forward(DISTANCE)
        self.new_snake_pos[0] = self.snakes[len(self.snakes) - 1].xcor()
        self.new_snake_pos[1] = self.snakes[len(self.snakes)- 1].ycor()
    
    def up(self):
        if int(self.snakes[0].heading()) != DOWN:
            self.snakes[0].setheading(UP)

    def down(self):
        if int(self.snakes[0].heading()) != UP:
            self.snakes[0].setheading(DOWN)
                                  
    def left(self):
        if int(self.snakes[0].heading()) != RIGHT:
            self.snakes[0].setheading(LEFT)

    def right(self):
        if int(self.snakes[0].heading()) != LEFT:
            self.snakes[0].setheading(RIGHT)

    def debug(self):
        print(self.snakes[0].pos())

    def ate_food(self, food_pos):
        if self.snakes[0].distance(food_pos) < SQUARE_SIZE/2:
            snek = Turtle(shape = "square")
            snek.speed("slowest")
            snek.penup()
            snek.color("white")
            snek.goto(x = self.new_snake_pos[0], y = self.new_snake_pos[1])
            self.snakes.append(snek)
            return True
        else:
            return False
        
    def wall_collision_check(self, width, height):
        if self.snakes[0].xcor() >= width/2 or self.snakes[0].xcor() <= (-1*(width)/2) + 10:
            return True
        elif self.snakes[0].ycor() >= (height+10)/2 or self.snakes[0].ycor() <= -1*(height+10)/2:
            return True
        else:
            return False
    
    def snake_collision_check(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            if self.snakes[0].distance(self.snakes[i].pos()) < SQUARE_SIZE/2:
                return True
        return False
    
    def reset(self):
        for snake in self.snakes:
            snake.ht()
            del snake
        self.snakes = []
        self.xcor = 0
        self.new_snake_pos = [0, 0]
        self.create_snake()


