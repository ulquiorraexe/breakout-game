# Breakout Game

This is a simple implementation of the classic **Breakout** game using Python's `turtle` graphics library. In this game, you control a paddle to bounce a ball and break blocks arranged at the top of the screen. The goal is to destroy all the blocks without letting the ball fall off the screen.

## Features

- **Paddle Movement**: Control the paddle with the left and right arrow keys.
- **Ball Physics**: The ball bounces off walls, the paddle, and blocks.
- **Blocks**: Different colored blocks are arranged at the top of the screen. Breaking all blocks wins the round.
- **Game Restart**: If the ball falls off the screen, the game restarts, and the blocks reappear.

## Installation

To run this project, make sure you have Python installed on your machine. Then, clone this repository using the following command:

```bash
git clone https://github.com/ulquiorraexe/breakout-game.git
```

Go to the project directory and simply run the `main.py` file:
```bash
python main.py
```

## How to Play

  1. **Start the Game**: Once the game is started, use the arrow keys to control the paddle.
  2. **Paddle Control**: Use the **Right Arrow** to move the paddle to the right and the **Left Arrow** to move the paddle to the left.
  3. **Break the Blocks**: Bounce the ball to hit the blocks and break them. Once all blocks are destroyed, the round is over.
  4. **Game Over**: If the ball falls off the screen, the game will restart, and the blocks will reappear.

## Code Explanation 

  - **Game Window:** The game window is created using `turtle.Screen()` with a size of 600x600 pixels and a black background.
  - **Paddle:** A white paddle is created at the bottom of the screen and moves left and right based on keyboard inputs.
  - **Ball:** The ball is a white circle that moves in a direction, bouncing off the walls, paddle, and blocks.
  - **Blocks:** Blocks are colored squares placed at the top of the screen. They disappear when hit by the ball.
  - **Collision Detection:** The game checks for collisions between the ball and the walls, paddle, and blocks to determine if the ball should bounce or break a block.
  - **Restart:** If the ball goes below the screen, the game restarts with all blocks placed back in their original positions.

## License 

This project does not have a license.
