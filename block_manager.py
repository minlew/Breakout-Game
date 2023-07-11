from turtle import Turtle
import random

colours = ["red", "orange", "yellow", "green", "blue"]


class BlockManager(Turtle):

    def __init__(self):
        super().__init__()  # Class inheritance. Now block class can do everything a turtle can.
        self.all_blocks = []
        self.color("white")
        self.x_start = -810
        self.y_start = -50

    def create_blocks(self):

        for i in range(5):  # Move block factory to the various rows
            self.x_start = -810
            self.y_start = self.y_start + 85
            for j in range(10):  # Print row of blocks at current row
                new_block = Turtle()
                new_block.shape("square")
                new_block.color(random.choice(colours))
                new_block.shapesize(stretch_wid=4, stretch_len=8.5)
                new_block.penup()
                new_block.goto(self.x_start, self.y_start)
                self.all_blocks.append(new_block)
                self.x_start = self.x_start + 179
