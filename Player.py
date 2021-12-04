from Entity import Entity
from pygame_info import ground, left_limit, right_limit

class Player(Entity):
    def __init__(self):
        self._x = 0
        self._y = 0
        self._health = 3
        self._score = 0
        self._direction = 1 # -1 = Left, 1 = Right

        self._sprite_height = 120
        self._sprite_width = 105

        #Which sprite is active
        self._frame = 0
        self._minimum_frame_time = 10
        self._frame_time = 10
        
        self._is_hit = False
        
        self._shotTimer = 0
        self._shotTimerLimit = 20

        self._is_shooting = False
        self._is_jumping = False
        self._jump_height = 0
        self._jump_time = 0
        self._is_moving = False
        
        self._images = {
            'standing': "./assets/MegaMan1.png",

            'stand shooting': "./assets/Shooting.png",

            'running': ("./assets/MegaMan2.png", "./assets/MegaMan3.png", "./assets/MegaMan4.png"),

            'run shooting': ("./assets/Shooting2.png","./assets/Shooting3.png","./assets/Shooting4.png"),

            'jumping': "./assets/MegaMan5.png",

            'jump shooting': "./assets/Shooting5.png"
        }
    
    
    def getFrameImage(self):
        if self._is_jumping:
            if self._is_shooting:
                return self._images['jump shooting']
            else:
                return self._images['jumping']
        else:
            if self._is_moving:
                if self._is_shooting:
                    return self._images['run shooting'][self._frame]
                else:
                    return self._images['running'][self._frame]
            else:
                if self._is_shooting:
                    return self._images['stand shooting']
                else:
                    return self._images['standing']
    
    def getScore(self):
        return self._score

    def resetShotTimer(self):
        self._shotTimer = self._shotTimerLimit

    def setShooting(self, isShooting):
        self._is_shooting = isShooting
        self._frame = 0
    
    def gotHit(self):
        self._is_hit = True
    
    def isShooting(self):
        return self._is_shooting
    
    def setMoving(self, isMoving):
        self._is_moving = isMoving
        self._frame = 0
    
    def isMoving(self):
        return self._is_moving
    
    def setJumping(self, jumping):
        self._is_jumping = jumping
        self._jump_time = 0
    
    def isJumping(self):
        return self._is_jumping
    
    def setShotTimer(self, shotTimer):
        self._shotTimer = shotTimer
    
    def canShoot(self):
        return self._shotTimer == 0
    
    def canJump(self):
        return not self._is_jumping
    
    def calcHeight(self, height, time):
        vel = 25
        g = 1
        return vel - g * time
    
    def getHealth(self):
        return self._health
    
    def getScore(self):
        return self._score
    
    def addScore(self, num):
        self._score += num
    
    def update(self):        
        if self._is_jumping:
            self._jump_time += 1
            self._jump_height += self.calcHeight(self._y, self._jump_time)
            if self._jump_height <= 0:
                self._is_jumping = False 
                self._jump_time = 0
            self._y = ground - self._jump_height
        
        if self._is_moving:
            if self._frame_time == 0:
                if self._is_shooting:
                    self._frame = (self._frame + 1) % len(self._images['run shooting'])
                else:
                    self._frame = (self._frame + 1) % len(self._images['running'])
                self._frame_time = self._minimum_frame_time
            else:
                self._frame_time -= 1
                
            if self._direction == -1:
                if not self._x <= left_limit:
                    self._x -= 10
            else:
                if not self._x >= right_limit:
                    self._x += 10
        
        if self._shotTimer > 0:
            self._shotTimer -= 1
        
        if self._is_hit:
            self._health -= 1
            self._is_hit = False

        