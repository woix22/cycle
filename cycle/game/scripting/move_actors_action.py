from game.scripting.action import Action

class MoveActorsAction(Action):
    def execute(self, cast, script):
        """Executes something that is important in the game. This method should be overriden by 
        derived classes.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        cast_list = cast.get_all_actors()
        for actor in cast_list:
            actor.move_next()

