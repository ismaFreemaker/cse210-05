import constants

from game.scripting.grow_snakes import Grow_Snakes
from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.snake import Snake
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    
    cast.add_actor("snakes", Snake(constants.RED, 0, 300))
    cast.add_actor("snakes", Snake(constants.GREEN, 450, 300))

    cast.add_actor("scores", Score())
    cast.add_actor("scores", Score())

    scores = cast.get_actors('scores')
    # Player one
    scores[0].set_text('Player one:')
    scores[0].set_controls('W, A, S, D')
    scores[0].set_color(constants.RED)
    scores[0].set_position(Point(15, 0))
    # Player two
    scores[1].set_text('Player two:')
    scores[1].set_controls('I, J, K, L')
    scores[1].set_color(constants.GREEN)
    scores[1].set_position(Point(730, 0))
    
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", Grow_Snakes())
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
