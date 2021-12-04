import pygame
from pygame import *

init()

MENUSTATE = 0
QUITSTATE = 1
PLAYSTATE = 2

RED = (248, 88, 62) #All colors to be used in program

BLACK = (43,62,66)        #
WHITE = (255, 255, 255)   #
GREY = (213, 225, 221)    #
DARKGREY = (116, 126, 128)#
BLUE = (119,190,210)      #

info = pygame.display.Info()
width = info.current_w 
height = info.current_h 

ground = height - 140   
left_limit = -10 
right_limit = width-130
gun_length = 110        
gun_height = 52         
bullet_move_speed = 15  


SIZE = (width, height)
screen = display.set_mode(SIZE,pygame.FULLSCREEN)
display.set_caption('Game')


scroll, scroll2 = 0, -1300
font1 = pygame.font.SysFont("arial", 30) #Score display font
myClock = pygame.time.Clock() #Allows for fps regulation