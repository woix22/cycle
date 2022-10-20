from game.casting.actor import Actor


class Label(Actor):
    """
    A label that displays a message. 
    """
    def __init__(self, message, color, position):
        super().__init__()
        self.set_text(message)
        self.set_color(color)
        self.set_position(position)

    