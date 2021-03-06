# Cycle
Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

## Rules
Cycle is played according to the following rules.

- Players can move up, down, left and right...
    - Player one moves using the W, S, A and D keys.
    - Player two moves using the I, K, J and L keys.

- Each player's trail grows as they move.
- Players try to maneuver so the opponent collides with their trail.
- If a player collides with their opponent's trail...
    - A "game over" message is displayed in the middle of the screen.
    - The cycles turn white.
    - Players keep moving and turning but don't run into each other.

## Project structure
```
root                    (project root folder)
+-- cycle               (source code for game)
  +-- game              (specific game classes)
  +-- __main__.py       (start game)
  +-- constants.py      (configuration of the game)
+-- README.md           (general info)
```

## Required software
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
- Alejo Bustos (ale21020@byui.edu)
- Alvaro Godoy (god21005@byui.edu)
- Daniela Atampiz (ata21001@byui.edu)
- Ismael Rojas (roj21010@byui.edu)