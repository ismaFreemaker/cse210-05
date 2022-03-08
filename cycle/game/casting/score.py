from game.casting.actor import Actor
from game.shared.point import Point
import constants
import random


class Score(Actor):
    """Shows the control design for the players.
        
        Args:
        color: must be set to red for player one and green for player two.
        position_x: establishes the banner at the upper side
        controls: Places the letters to be used during the game.
        """    

    
    def __init__(self):
        super().__init__()
        self.set_position
        self.set_color
        self.set_controls

    def banner(self, color, position_x, controls):
        
        self.set_color = color
        
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position_x = Point(x, y)
        position_x = position_x.scale(constants.CELL_SIZE)
        self.set_position(position_x)

        for control in controls:
            player_one = "W,A,S,D"
            self.set_controls(f"Player One: {player_one}")
            player_two = "I,J,K,L"
            self.set_controls(f"Player Two: {player_two}")
