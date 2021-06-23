from turtle import Turtle


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        x = 0
        for i in range(3):
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(x, 0)
            self.snakes.append(turtle)
            x -= 20

    def move(self):
        for snake in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake - 1].xcor()
            new_y = self.snakes[snake - 1].ycor()
            self.snakes[snake].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.snakes[0].setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.snakes[0].setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.snakes[0].setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.snakes[0].setheading(180)

    def increase_size(self):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(self.snakes[len(self.snakes) - 1].position())
        self.snakes.append(turtle)

