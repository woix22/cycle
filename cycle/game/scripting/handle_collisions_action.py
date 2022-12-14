import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner = ""

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_no_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_no_collision(self,cast):
        cycle = cast.get_first_actor("cycles")
        cycle2 = cast.get_second_actor("cycles")
        cycle.grow_tail(1)
        cycle2.grow_tail(1)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle = cast.get_first_actor("cycles")
        cycle2 = cast.get_second_actor("cycles")
        head = cycle.get_segments()[0]
        head2 = cycle2.get_segments()[0]
        segments = cycle.get_segments()[1:]
        segments2 = cycle2.get_segments()[1:]
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._winner = "PLAYER 2"

            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._winner = "PLAYER 1"

        for segment in segments2:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._winner = "PLAYER 1"

            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._winner = "PLAYER 2"


        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycle = cast.get_first_actor("cycles")
            cycle2 = cast.get_second_actor("cycles")
            segments = cycle.get_segments()
            segments2 = cycle2.get_segments()
            label = cast.get_first_actor("labels")
            label2 = cast.get_second_actor("labels")


            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text(f"{self._winner} WINS!")
            message.set_position(position)
            cast.add_actor("messages", message)

            label.set_color(constants.WHITE)
            label2.set_color(constants.WHITE)

            for segment in segments:
                segment.set_color(constants.WHITE)

            for segment in segments2:
                segment.set_color(constants.WHITE)
