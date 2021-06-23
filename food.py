from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.create_food()

    def create_food(self):
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        self.goto(x, y)
