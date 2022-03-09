import constants
from game.casting.cycle1 import Cycle1 
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle2(Cycle1):
    """
    A second cycle.
    
    The responsibility of cycle is to move itself.
    """

    def __init__(self):
        super().__init__()
        self._trails = []
 
    def extend_trail(self):
        # Creates trail segments

        trail = self._trails[-1]
        velocity = trail.get_velocity()
        offset = velocity.reverse()
        position = trail.get_position().add(offset)
        
        trail = Actor()
        trail.set_position(position)
        trail.set_velocity(velocity)
        trail.set_text("#")
        trail.set_color(constants.YELLOW)
        self._trails.append(trail)
    
    def create_cycle(self):    
        # Creates bicycle segment

        trail = Actor()
        trail.set_text("8")
        trail.set_position(Point(int(constants.MAX_X / 3 * 2), int(constants.MAX_Y / 2)))
        trail.set_color(constants.GREEN)
        trail.set_velocity(Point(0, 0))
        self._trails.append(trail)