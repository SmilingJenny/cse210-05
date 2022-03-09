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
            self._handle_trail_collision(cast)
            self._handle_game_over(cast)
        

    def _handle_player_collision(self, cast):
        cycle = cast.get_first_actor("cycles")
        cycle.extend_trail() # Camden, do this again for the 2nd player.
        print()
            
    def _handle_trail_collision(self, cast):
        cycle = cast.get_first_actor("cycles")
        head = cycle.get_trails()[0]
        trails = cycle.get_trails()[1:]
        
        for trail in trails:
            if head.get_position().equals(trail.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        
        if self._is_game_over:
            cycle = cast.get_first_actor("cycles")
            trails = cycle.get_trails()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for trail in trails:
                trail.set_color(constants.WHITE)
            return
        
    def get_is_game_over(self):
        return self._is_game_over
