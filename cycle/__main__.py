# Copied from snake to adapt to cycle
import constants

from game.casting.cast import Cast
# from game.casting.score import Score
from game.casting.cycle1 import Cycle1
from game.casting.cycle2 import Cycle2 
from game.scripting.script import Script
from game.scripting.control_cycle1_action import ControlCycle1Action
from game.scripting.control_cycle2_action import ControlCycle2Action
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
    cast.add_actor("cycles", Cycle1())      
    cast.add_actor("cycles", Cycle2())
    # cast.add_actor("scores", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlCycle1Action(keyboard_service))
    script.add_action("input", ControlCycle2Action(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()