from turtle import Turtle
import random


def my_round(x, base=20):
    return base * round(x/base)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=0.9, stretch_len=0.9)
        self.color('green')
        self.speed('fastest')
        self.new_location()

    def new_location(self):
        random_x = random.randint(my_round(-280), my_round(280))
        random_y = random.randint(my_round(-280), my_round(280))
        self.goto(random_x, random_y)
