from pygame_info import pygame, screen, left_limit, right_limit, gun_height, gun_length, height, width, BLUE, RED, font1
from Enemy import Enemy
from Bullet import Bullet

class Map:
    def __init__(self, player, bulletList, enemyList):
        self._bullets = bulletList
        self._enemies = enemyList
        self._player = player
        self._max_enemies = 2
    
    def addBullet(self, bullet):
        self._bullets.append(bullet)
    
    def addEnemy(self, enemy):
        self._enemies.append(enemy)
    
    def removeEnemy(self, enemy):
        self._enemies.remove(enemy)
    
    def removeBullet(self, bullet):
        self._bullets.remove(bullet)

    def updateEnemies(self):
        #Spawns in new enemies and adds them to the list
        if len(self._enemies) < self._max_enemies:
            newEnemy = Enemy()
            self.addEnemy(newEnemy)

        #Checks all enemy situations and removes them from the list if they are hit or go offscreen
        for enemy in self._enemies:
            enemyX = enemy.getPos()

            if enemyX > (width + 10) or enemyX < -10:
                self._enemies.remove(enemy)    

            else:
                enemy.setPos(enemyX + (enemy.getDirection()) * 7)
    
    def updateBullets(self):
        if self._player.isShooting():
            if self._player.canShoot():
                self._player.resetShotTimer()
                if self._player.getDirection() == 1:
                    bullet_x = self._player.getX() + gun_length
                else:
                    bullet_x = self._player.getX()
                bullet_y = self._player.getY() + gun_height
                self.addBullet(Bullet(self._player.getDirection(), bullet_x, bullet_y))
        
        for bullet in self._bullets:
            if bullet.getX() <= left_limit or bullet.getX() >= right_limit + 110:
                self.removeBullet(bullet)
            else:
                bullet.setX(bullet.getX() + (bullet.getDirection() * 15))
    
    def updateCollisions(self):
        for enemy in self._enemies:
            for bullet in self._bullets:
                if self.collided(bullet, enemy):
                    self.removeEnemy(enemy)
                    self.removeBullet(bullet)
                    self._player.addScore(100)
            if enemy:
                if self.collided(self._player, enemy):
                    self.removeEnemy(enemy)
                    self._player.gotHit()

    def collided(self, entity1, entity2):
        hitbox1 = entity1.getHitBox()
        hitbox2 = entity2.getHitBox()
        c1 = hitbox2['left'] <= hitbox1['left'] <= hitbox2['right']
        c2 = hitbox2['left'] <= hitbox1['right'] <= hitbox2['right']
        c3 = hitbox2['top'] <= hitbox1['bottom']
        return (c1 and c3) or (c2 and c3)

    def draw(self):
        #Draws all enemies
        for enemy in self._enemies:
            enemy.update()
            enemy_image = pygame.image.load(enemy.getFrameImage())
            if enemy.getDirection() == 1:
                enemy_image = pygame.transform.flip(enemy_image,True,False)
            screen.blit(enemy_image, (enemy.getPos(), height - 78))
        
        #Draws all bullets
        for bullet in self._bullets:
            bullet_x = bullet.getX()
            bullet_y = bullet.getY()
            if bullet.getDirection() == -1:
                pygame.draw.ellipse(screen, BLUE, (bullet_x, bullet_y, 25, 25))
            else:
                pygame.draw.ellipse(screen, BLUE, (bullet_x, bullet_y, 25, 25)) 
                
        #Draws healthbar and writes score and controls
        pygame.draw.rect(screen,RED,(10,10,300,50))                
        pygame.draw.rect(screen,BLUE,(10,10,100*self._player.getHealth(),50))
        pygame.draw.rect(screen,(0,0,0),(10,10,300,50),2)        
        screen.blit(font1.render("Score: {}".format(self._player.getScore()), 1, (0,0,0)), (925, 25))
        #Draws megaman
        mega_image = pygame.image.load(self._player.getFrameImage())
        if self._player.getDirection() == -1:
          mega_image = pygame.transform.flip(mega_image,True,False)
        p_x = self._player.getPos()[0]
        p_y = self._player.getPos()[1]
        screen.blit(mega_image, (p_x, p_y))
        pygame.display.flip()
    