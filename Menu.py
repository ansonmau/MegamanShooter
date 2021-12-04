from pygame_info import *


class Menu:
  def checkButtonMenu(self, button, mouseX, mouseY):
    if button == 1:
      if self.checkPlayMenu(mouseX, mouseY) == True:
        return PLAYSTATE
      elif self.checkQuitMenu(mouseX, mouseY) == True:
        return QUITSTATE
      else:
        return MENUSTATE
      
  # check if mouse is within the play menu box
  def checkPlayMenu(self, mouseX, mouseY):
    playMenuLeft = width/4
    playMenuWidth = width/2
    playMenuTop = height/4
    playMenuHeight = height/5
    
    if mouseX >= playMenuLeft and mouseX <= playMenuLeft + playMenuWidth and mouseY >= playMenuTop and mouseY <= playMenuTop + playMenuHeight:
      return True
    return False

  #check if mouse is within the quit menu box
  def checkQuitMenu(self, mouseX, mouseY):
    playMenuLeft = width/4
    playMenuWidth = width/2
    playMenuTop = height/2
    playMenuHeight = height/5
    
    if mouseX >= playMenuLeft and mouseX <= playMenuLeft + playMenuWidth and mouseY >= playMenuTop and mouseY <= playMenuTop + playMenuHeight:
      return True
    return False

  # paint the menu screen
  def paintMenu(self, mouseX, mouseY):
    # title fonts
    fontTitle = font.SysFont("Droid Sans",width//15,bold=True)
    fontScore = font.SysFont("Droid Sans",width//25)
    fontInfo = font.SysFont("Droid Sans",width//36)  
    titleText = fontTitle.render("GAME!", 1, BLACK)
    infoText = fontInfo.render("Gain points by using the arrows to move and spacebar to shoot!", 1, WHITE)
    titleSize = fontTitle.size("GAME!")
    infoSize = fontInfo.size("Gain points by using the arrows to move and spacebar to shoot!")
    

    # current colour fonts
    fontMenu = font.SysFont("Droid Sans",width//12)	
    menuText1 = fontMenu.render("Play Game", 1, (247,243,232))
    menuText2 = fontMenu.render("Quit Game", 1, (247,243,232))
    text1Size = fontMenu.size("Play Game:")
    text2Size = fontMenu.size("Quit Game:")
    
    # determine the colour of the menu options background
    colMenu1 = BLUE
    colMenu2 = BLUE
    if self.checkPlayMenu(mouseX, mouseY):
      colMenu1 = RED
      
    if self.checkQuitMenu(mouseX, mouseY):
      colMenu2 = RED
      
    
    # Draws the menu and it's options
    pygame.draw.rect(screen,DARKGREY,(0,0,width,height))
    pygame.draw.rect(screen,RED,(25,height - infoSize[1]*2.1,width - 50,55))  
    screen.blit(titleText, (width/2 - titleSize[0]/2, height/10 - titleSize[1]/4, titleSize[0], titleSize[1]))
    screen.blit(infoText, (width/2 - infoSize[0]/2 + scroll, height - infoSize[1]*2, infoSize[0], infoSize[1]))
    pygame.draw.rect(screen,colMenu1,(0,0,width,height),50)  
    pygame.draw.rect(screen, colMenu1, (width/4, height/4, width/2, height/5))
    screen.blit(menuText1, (width/2 - text1Size[0]/2, height/4 + height/10 - text1Size[1]/2, text1Size[0], text1Size[1]))
    pygame.draw.rect(screen, colMenu2, (width/4, height/2, width/2, height/5))
    screen.blit(menuText2, (width/2 - text2Size[0]/2, height/2 + height/10 - text2Size[1]/2, text1Size[0], text1Size[1]))
