from turtle import Turtle, Screen
import time
from player import Player
from ball import Ball
from block_manager import BlockManager

score = 0

screen = Screen()
screen.setup(width=1800, height=1000)
screen.tracer(0)  # Turn off movement animations

player = Player()
blocks = BlockManager()
blocks.create_blocks()
ball = Ball()

screen.listen()  # Get screen to listen for events...
screen.onkey(player.go_left, "Left")  # ...Specifically, key events
screen.onkey(player.go_right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.01)
    screen.update()  # Turn on periodic screen updates as a replacement for tracer animations
    ball.move()     # Set ball to constantly be moving

    if ball.xcor() > 890 or ball.xcor() < -890:   # Ball bouncing against side walls
        ball.bounce_x()

    if ball.ycor() > 490:  # Ball bounding against ceiling
        ball.bounce_y()

    if ball.ycor() < -430 and abs(ball.xcor() - player.xcor()) < 80:  # Ball bounding against paddle
        ball.bounce_y()
        ball.random_bounce()  # Random bounce to introduce some difficulty

    # Ball bounding against blocks. If block is white, ball will pass straight through it
    for block in blocks.all_blocks:
        if abs(ball.xcor() - block.xcor()) < 90 and abs(ball.ycor() - block.ycor()) < 50 and block.color() != ("white",
                                                                                                               "white"):
            if abs(ball.xcor() - block.xcor()) > 84:  # Condition for bounding against side of blocks
                ball.bounce_x()
                block.color("white")
                score += 1
            else:  # Condition for bounding against top of blocks
                ball.bounce_y()
                block.color("white")
                score += 1

    if ball.ycor() < -450:  # Ball misses paddle, causing game over
        game_over = Turtle()
        game_over.goto(-700, 0)
        game_over.write("Game Over!", move=False, align="left", font=("Arial", 200, "normal"))
        game_is_on = False

    if all(block.color() == ("white", "white") for block in blocks.all_blocks):  # All blocks hit, causing game win
        you_win = Turtle()
        you_win.goto(-700, 0)
        you_win.write("You Win!", move=False, align="left", font=("Arial", 200, "normal"))
        game_is_on = False


score_display = Turtle()  # Display final score
score_display.goto(-650, -300)
score_display.write(f"Your score was {score}", move=False, align="left", font=("Arial", 128, "normal"))
game_is_on = False


screen.exitonclick()
