from turtle import Turtle
import random

STARTING_POSITION = (0, -420)
MOVE_DISTANCE = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()  # Class inheritance. Now ball class can do everything a turtle can.
        self.shape("circle")
        self.color("grey")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.x_move = random.randint(-MOVE_DISTANCE, MOVE_DISTANCE)
        self.y_move = MOVE_DISTANCE

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def random_bounce(self):
        self.x_move = random.randint(-MOVE_DISTANCE, MOVE_DISTANCE)
