import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
#class for handling collisions and returning a message based off who wins  
    def __init__(self):
    #init function
        self._is_game_over = False
        self.winner = ""
    def execute(self, cast, script):
    #runs on start and handles the main functions    
        if not self._is_game_over:
            self._handle_trail_collision(cast)
            self._handle_cycle_collision(cast)
            self._handle_game_over(cast)
        

   
    def _handle_trail_collision(self, cast):
    #function to determine what to do if a player collides with their own trail.
        cycle1 = cast.get_first_actor("cycles")
        cycle2 = cast.get_second_actor("cycles")
        head1 = cycle1.get_trails()[0]
        head2 = cycle2.get_trails()[0]
        trails1 = cycle1.get_trails()[1:]
        trails2 = cycle2.get_trails()[1:]
        
        for trail1 in trails1:
            if head1.get_position().equals(trail1.get_position()):
                self._is_game_over = True
                self.winner = "player2"
        #player 1 collision with own trail        
        for trail2 in trails2:
            if head2.get_position().equals(trail2.get_position()):
                self._is_game_over = True  
                self.winner = "player1"
        #player 2 collision with own trail        
    def _handle_cycle_collision(self, cast):
    #function to determine what to do if a player collides with another players trail
        cycle1 = cast.get_first_actor("cycles")
        cycle2 = cast.get_second_actor("cycles")
        head1 = cycle1.get_trails()[0]
        head2 = cycle2.get_trails()[0]
        trails1 = cycle1.get_trails()[1:]
        trails2 = cycle2.get_trails()[1:]
         
        for trail1 in trails1:
            if head2.get_position().equals(trail1.get_position()):
                self._is_game_over = True
                self.winner = "player1"
        #player two collision with player 1 trail
        for trail2 in trails2:
            if head1.get_position().equals(trail2.get_position()):
                self._is_game_over = True
                self.winner = "player2"
        #player one collision with player 2 trail
    def _handle_game_over(self, cast):
    #game over state function that    
        if self._is_game_over:
            cycle1 = cast.get_first_actor("cycles")
            trails1 = cycle1.get_trails()
            cycle2 = cast.get_second_actor("cycles")
            trails2 = cycle2.get_trails()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            #creates message actor
            if self.winner == "player1":
                message.set_text("Player 1 Wins!")
            if self.winner == "player2":
                message.set_text("Player 2 Wins!")
            #sets message based off of winner
            
            message.set_position(position)
            cast.add_actor("messages", message)
            #casts the message
            
            for trail in trails1:
                trail.set_color(constants.WHITE)
            
            for trail in trails2:
                trail.set_color(constants.WHITE)
            #sets both trails to white upon end of game

    # Use commented method if you want the players to stop moving at game over.      
    # def get_is_game_over(self):
    #     return self._is_game_over
