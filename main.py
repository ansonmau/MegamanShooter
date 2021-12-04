import pygame #Allows for use of pygame 
from pygame_info import  *
import threading
#Pip install: "pip install python-vlc"
import vlc
from time import sleep
from Map import Map
from Player import Player
from Menu import Menu


#from 

init() #Initilizes pygame
menu = Menu()

gameState = MENUSTATE
mx = my = 0
button = 0

def game():
    global gameState
    
    #Initilize Objects Player
    player = Player()
    enemies = []
    bullets = []
    
    game_map = Map(player, bullets, enemies)

    player.setPos(width/2, ground) #initial position
    
    running = True
    while running:
        pygame.draw.rect(screen, GREY, (0,0,width,height)) #Reset screen

        #Set new player positions here (jumping, and direction)
        player.update()

		#Starts multithreading for enemies update
        enemiesThread = threading.Thread(target=game_map.updateEnemies)
        enemiesThread.start()

		#Starts multithreading for bullets update
        bulletsThread = threading.Thread(target=game_map.updateBullets)
        bulletsThread.start()

		#Starts multithreading for collision update
        collisionThread = threading.Thread(target=game_map.updateCollisions)
        collisionThread.start()

		#Join the threads
        enemiesThread.join()
        bulletsThread.join()
        collisionThread.join()

        game_map.draw() #BIG DRAWING MOMENT

        if player.getHealth() == 0:
            pygame.time.wait(300)
            running = False
            gameState = MENUSTATE
    
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                    running = False
                    gameState = MENUSTATE       

            elif event.type == KEYDOWN and event.key == K_RIGHT:
                    player.setMoving(True)
                    player.setDirection(1)
                    
            elif event.type == KEYUP and event.key == K_RIGHT:
                if player.getDirection() == 1: # must check direction here to avoid making player stop if user is holding down other direction but lets go of this one
                    player.setMoving(False)        
                    player.setFrame(0)

            elif event.type == KEYDOWN and event.key == K_LEFT:
                    player.setMoving(True)
                    player.setDirection(-1)

            elif event.type == KEYUP and event.key == K_LEFT:
                if player.getDirection() == -1: # must check direction here to avoid making player stop if user is holding down other direction but lets go of this one
                    player.setMoving(False)
                    player.setFrame(0)

            elif event.type == KEYDOWN and event.key == K_UP:
                    if player.canJump():
                        player.setJumping(True)

            elif event.type == KEYDOWN and event.key == K_SPACE:
                player.setShooting(True)

            elif event.type == KEYUP and event.key == K_SPACE:
                player.setShooting(False)

        myClock.tick(60)

def music():
    i = 0
    playlist = ["CoconutMall.mp3", "SparkMusic.mp3", "MegaMusic.mp3"]
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playlist[i])
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    sleep(4)
    # While the game is running
    while gameState == PLAYSTATE:
        # If the song ends, queue up next song in playlist. Loop playlist.
        if player.get_state() == 6:
            i = i + 1
            player.set_media(Instance.media_new(playlist[i % 3]))
            player.play()
        sleep(1)





def main():
    global gameState
	 # Creates new thread for music
    t1 = threading.Thread(target=music)
    t1.start()
    print("No. of active threads: " + str(threading.active_count()))
    while gameState != QUITSTATE:
        if gameState == PLAYSTATE:
            game()
		# After game is launched initiate multithread of music
        t1.join()	
        for evnt in pygame.event.get():  
            if evnt.type == MOUSEMOTION:
                mx, my = evnt.pos
            if evnt.type == MOUSEBUTTONDOWN:
                button = evnt.button
                mx, my = evnt.pos
                #Button has been clicked, check for what happens
                if gameState == MENUSTATE:
                    gameState = menu.checkButtonMenu(button, mx, my)
        menu.paintMenu(mx, my)
        display.flip()

    pygame.display.quit() #Quits program


if __name__ == "__main__":
  main()
