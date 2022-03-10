import constants
from game.scripting.action import Action
from game.shared.point import Point

'''
Duplicate and rename control_actions_actor.py to apply to two actors/players.
This define the movement of player_2

Updated the "I, J, K, L" keys in keyboard_service.py to be arrows.
This is done by changing 'def is_key_down(self, key)' in 'class KeyboardService'

'''

class ControlCycle2Action(Action):
    """
    An input action that controls the cycle.
    
    The responsibility of ControlCycle1Action is to get the direction and move the cycle.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlCycle1Action using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0, -constants.CELL_SIZE)

    def execute(self, cast, script):
        """Executes the control cycle1 action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('j'): #or self._keyboard_service.is_key_down(''):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'): #or self._keyboard_service.is_key_down(''):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'): #or self._keyboard_service.is_key_down(''):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'): #or self._keyboard_service.is_key_down(''):
            self._direction = Point(0, constants.CELL_SIZE)
        
        cycle2 = cast.get_second_actor("cycles")
        cycle2.turn_cycle(self._direction)
