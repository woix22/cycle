import constants
from game.casting.cycle import Cycle
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle2(Cycle):
    """
    A cycle that makes a trail
    
    The responsibility of Cycle is to move itself.
    
    """    
    def _prepare_body(self):
        x = int(constants.MAX_X - constants.STARTING_POINT)
        y = int(constants.MAX_Y - constants.STARTING_POINT)

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "@" if i == 0 else "#"
            color = constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.GREEN)
            self._segments.append(segment)