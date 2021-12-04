from Entity import Entity
from pygame_info import width, ground
import random

class Enemy(Entity):
    def __init__(self):
        self._x = random.choice([0,width-80])
        self._y = ground

        #Which sprite is active
        self._frame = 0
        self._frame_time = 5
        self._minimum_frame_time = 5
        self._sprite_width = 70
        self._sprite_height = 10

        #left = -1, right = 1
        if(self._x == 0):
            self._direction = 1
        else:
            self._direction = -1

        self._sprites = ["./assets/Met1.png","./assets/Met2.png","./assets/Met3.png","./assets/Met3.1.png"]
    
    def getFrameImage(self):
        return self._sprites[self._frame]

    def setPos(self, x):
        self._x = x

    def getHitBox(self): # had to overload hitbox method since sprite y is a lot higher than where it looks visually
        return {'top': self._y+40, 'left': self._x, 'bottom': self._y + self._sprite_height, 'right': self._x + self._sprite_width}

    def getPos(self):
        return self._x

    def update(self):
        if self._frame_time == 0:
            self._frame = (self._frame + 1) % len(self._sprites)
            self._frame_time = self._minimum_frame_time
        else:
            self._frame_time -= 1