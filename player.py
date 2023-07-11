from turtle import Turtle

STARTING_POSITION = (0, -450)
MOVE_DISTANCE = 150


class Player(Turtle):

    def __init__(self):     # Initialize player
        super().__init__()  # Class inheritance. Now player class can do everything a turtle can.
        self.shape("square")
        self.shapesize(stretch_wid=8, stretch_len=1)
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_left(self):
        if self.xcor() > - 820:  # Can't move beyond left edge of screen
            new_x = self.xcor() - MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def go_right(self):
        if self.xcor() < 820:  # Can't move beyond right edge of screen
            new_x = self.xcor() + MOVE_DISTANCE
            self.goto(new_x, self.ycor())
