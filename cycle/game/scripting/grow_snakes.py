from game.scripting.action import Action
from game.shared.color import Color



class Grow_Snakes(Action):
    """A thing that is done.
    
    The responsibility of action is to do somthing that is integral or important in the game. Thus,
    it has one method, execute(), which should be overridden by derived classes.
    """
    new_size=18

    new_color=255

    def execute(self, cast, script):
        """Executes something that is important in the game. This method should be overriden by 
        derived classes.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        new_size=18
        new_color=255
       
        snakes = cast.get_actors("snakes")
        segment1 = snakes[0].get_segments()
        segment2 = snakes[1].get_segments()
        self._video_service.draw_actors(segment1)
        self._video_service.draw_actors(segment2)

 
        for 1 in 5 :
            segment1.__init__.self._font_size = new_size 
            segment2.__init__.self._font_size = new_size 
            segment1.self._color = Color(new_color, 0, 0)
            segment2.self._color = Color(0, new_color, 0)

            new_size = new_size + 1
            new_color = new_color - 30

        

