from game.scripting.action import Action
from game.shared.color import Color
import random

class Grow_Snakes(Action):
    """A thing that is done.
    
    The responsibility of action is to do somthing that is integral or important in the game. Thus,
    it has one method, execute(), which should be overridden by derived classes.
    """

    def execute(self, cast, script):
        """Executes something that is important in the game. This method should be overriden by 
        derived classes.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        decision = random.randint(1, 6)
        if decision == 1:
            snakes = cast.get_actors('snakes')
            snakes[0].grow_tail(1)
            snakes[1].grow_tail(1)