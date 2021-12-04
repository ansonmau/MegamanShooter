from Entity import Entity

class Bullet(Entity):
    def __init__(self, direction, x, y):
        # -1 = Left, 1 = Right
        self._direction = direction
        self._sprite_height = self._sprite_width = 25
        self._x = x
        self._y = y

    def setX(self, x):
        self._x = x