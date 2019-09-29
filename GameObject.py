from constants import SF


class GameObject:
    """
    Base GO class, any object in the game will inherit this class
    """
    def __init__(self, surface, color, x, y):
        self.surface = surface
        self.color = color
        self.x = x*SF
        self.y = y*SF

    @property
    def pos(self):
        return self.x, self.y

    def update(self, event_list):
        pass
