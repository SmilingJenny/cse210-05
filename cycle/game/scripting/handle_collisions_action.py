import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
   
    def __init__(self):
        self._is_game_over = False

    def execute(self, cast, script):
        
        if not self._is_game_over:
            self._handle_player_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
        

    def _handle_player_collision(self, cast):
        cycle = cast.get_first_actor("cycles")
        cycle.grow_tail() # Camden, do this again for the 2nd player.
        print()
            
    def _handle_segment_collision(self, cast):
        cycle = cast.get_first_actor("cycles")
        head = cycle.get_segments()[0]
        segments = cycle.get_segments()[1:]
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        
        if self._is_game_over:
            cycle = cast.get_first_actor("cycles")
            segments = cycle.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
