import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    
    def __init__(self):
        self._is_game_over = False

    def execute(self, cast, script):
        
        if not self._is_game_over:
            self._handle_trail_collision(cast)
            self._handle_cycle_collision(cast)
            self._handle_game_over(cast)
        

   
    def _handle_trail_collision(self, cast):
        cycle1 = cast.get_first_actor("cycles")
        cycle2 = cast.get_second_actor("cycles")
        head1 = cycle1.get_trails()[0]
        head2 = cycle2.get_trails()[0]
        trails1 = cycle1.get_trails()[1:]
        trails2 = cycle2.get_trails()[1:]
        
        for trail1 in trails1:
            if head1.get_position().equals(trail1.get_position()):
                self._is_game_over = True
                ##player_2_score += 1
                ##return player_2_score
        ##for trail2 in trails2:
            ##if head2.get_position().equals(trail2.get_position()):
                self._is_game_over = True  
                ##player_1_score += 1
                ##return player_1_score    
              
    def _handle_cycle_collision(self, cast):
        cycle1 = cast.get_first_actor("cycles")
        cycle2 = cast.get_second_actor("cycles")
        head1 = cycle1.get_trails()[0]
        head2 = cycle2.get_trails()[0]
        trails1 = cycle1.get_trails()[1:]
        trails2 = cycle2.get_trails()[1:]
        ##while self._is_game_over == False:
            ##if head1.get_position().equals(head2.get_position):
                ##self._is_game_over = True  
        for trail1 in trails1:
            if head2.get_position().equals(trail1.get_position()):
                self._is_game_over = True
                ##player_2_score += 1
                ##return player_2_score
        for trail2 in trails2:
            if head1.get_position().equals(trail2.get_position()):
                self._is_game_over = True
                ##player_1_score += 1
                ##return player_1_score
            
     
    def _handle_game_over(self, cast):
        
        if self._is_game_over:
            cycle1 = cast.get_first_actor("cycles")
            trails1 = cycle1.get_trails()
            cycle2 = cast.get_first_actor("cycles")
            trails2 = cycle2.get_trails()
            

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for trail in trails1:
                trail.set_color(constants.WHITE)
            return
          

    # Use commented method if you want the players to stop moving at game over.      
    # def get_is_game_over(self):
    #     return self._is_game_over
