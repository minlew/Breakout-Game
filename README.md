# Breakout-Style Game

## Description
This is a Python implementation of a classic Breakout-style game using the Turtle graphics library. The player controls a paddle to bounce a ball and break colored blocks, aiming to clear all blocks without letting the ball fall off the bottom of the screen.

### Features

* Classic Breakout gameplay.
* Colorful blocks arranged in rows.
* Player-controlled paddle.
* Bouncing ball with random angle changes.
* Score tracking.
* Game over and win conditions.

### Technologies
* Python

### Python Libs
* Turtle graphics library.

## Getting Started
1. Clone this repository.
2. Create virtual environment.
3. Run [script](main.py) in Python. 

## How to Play
1. Use the left and right arrow keys to move the paddle.
2. Bounce the ball off the paddle to hit and break the colored blocks.
3. Try to break all the blocks without letting the ball fall off the bottom of the screen.
4. The game ends when you either break all blocks (win) or miss the ball with the paddle (lose).

## File Structure
* `main.py`: The main game loop and logic.
* `player.py`: Contains the `Player` class for the paddle.
* `ball.py`: Contains the `Ball` class for the game ball.
* `block_manager.py`: Contains the `BlockManager` class for creating and managing blocks.

## Customization
* In `ball.py`: Adjust `STARTING_POSITION` and `MOVE_DISTANCE` to change ball behavior.
* In `player.py`: Modify `STARTING_POSITION` and `MOVE_DISTANCE` to alter paddle properties.
* In `block_manager.py`: Change the `colours` list to use different block colors.
