class Entity:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._sprite_width = 0
        self._sprite_height = 0
        
        self._health = 0
        #Which sprite is active
        self._frame = 0
        #left = -1, right = 1
        self._direction = 1
    
    def flip(self, direction):
        if direction == -1:
            self._direction = 1
        else:
            self._direction = 1
    
    
    def getHitBox(self):
        return {'top': self._y, 'left': self._x, 'bottom': self._y + self._sprite_height, 'right': self._x + self._sprite_width}

    def getHealth(self):
        return self._health
    
    def setHealth(self, health):
        self._health = health
    
    def setPos(self, x, y):
        self._x = x
        self._y = y

    def getPos(self):
        return (self._x, self._y)
    
    def setFrame(self, frame):
        self._frame = frame
    
    def setDirection(self, direction):
        self._direction = direction
    
    def getDirection(self):
        return self._direction
    
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y
    

    
    
    

    
    
    
    
