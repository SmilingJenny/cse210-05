import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle1(Actor):
    """
    A cycle.
    
    The responsibility of cycle is to move itself.

    Attributes:
        _trails (list): The list that makes up the trail of the bicycle.
        _prepare_body (method): The body of the bicycle.
    """
    def __init__(self):
        super().__init__()
        self._trails = []
        self.create_cycle()
        

    def get_trails(self):
        return self._trails

    def move_next(self):
        # move all trails
        for trail in self._trails:
            trail.move_next()
        # update velocities
        for i in range(len(self._trails) - 1, 0, -1):
            trailing = self._trails[i]
            previous = self._trails[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)
        self.extend_trail()

    def get_cycle(self):
        return self._trails[0]

    def extend_trail(self):
        trail = self._trails[-1]
        velocity = trail.get_velocity()
        offset = velocity.reverse()
        position = trail.get_position().add(offset)
        
        trail = Actor()
        trail.set_position(position)
        trail.set_velocity(velocity)
        trail.set_text("#")
        if self._trails[0].get_color() == constants.WHITE: trail.set_color(constants.WHITE)
        else: trail.set_color(constants.RED)
        self._trails.append(trail)

    def turn_cycle(self, velocity):
        self._trails[0].set_velocity(velocity)
    
    def create_cycle(self):
        trail = Actor()
        trail.set_text("8")
        trail.set_position(Point(int(constants.MAX_X / 3), int(constants.MAX_Y / 2)))
        trail.set_color(constants.GREEN)
        trail.set_velocity(Point(0, 0))
        self._trails.append(trail)