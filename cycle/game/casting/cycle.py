import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A cycle.
    
    The responsibility of cycle is to move itself.

    Attributes:
        _segments (list): The list of segments in the bicycle trail.
        _prepare_body (method): The body of the bicycle.
    """
    def __init__(self):
        super().__init__()
        self._segments = []

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self):
        tail = self._segments[-1]
        velocity = tail.get_velocity()
        offset = velocity.reverse()
        position = tail.get_position().add(offset)
        
        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text("#")
        segment.set_color(self.get_color())
        self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def create_cycle(self, position=Point(int(constants.MAX_X/2), int(constants.MAX_Y/2)), color=constants.GREEN):
        self.set_color(color)
        
        segment = Actor()
        segment.set_text("8")
        segment.set_position(position)
        segment.set_color(constants.GREEN)
        segment.set_velocity(Point(0, 0))
        self._segments.append(segment)