# Copied from snake to adapt to cycle
import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.cycle import Cycle
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
    cast.add_actor("scores", Score())
    
    cast.add_actor("cycles", Cycle())
    player1 = cast.get_first_actor("cycles")
    player1.create_cycle(Point(int(constants.MAX_X / 3), int(constants.MAX_Y / 2)), constants.RED)
    
    cast.add_actor("cycles", Cycle())
    player2 = cast.get_second_actor("cycles")
    player2.create_cycle(Point(int(constants.MAX_X / 3 * 2), int(constants.MAX_Y / 2)), constants.YELLOW)
    
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()