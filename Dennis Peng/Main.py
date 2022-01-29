"""
May 28,2019
Dennis Peng
Flappy Bird
This is my take on the game of flappy bird.
"""
    
# I - IMPORT AND INITIALIZE
import pygame, pySprites, random
pygame.init()
pygame.mixer.init()

def startScreen():
    """This function is our main loop for our Flappy Bird practice screen."""

    # D - DISPLAY
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Flappy Bird")
     
    # E - ENTITIES
    background = pySprites.Background()
    pygame.mixer.music.load("song.wav")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
     
    # center opening point between the 2 pipes
    y = random.randint(200,500)
    
    # Sprites for: ScoreKeeper label, End Zones, Pipes, and Players
    floor = pySprites.Floor(screen)
    player = pySprites.Player(screen)
    endzone = pySprites.EndZone(screen)
    topPipe = pySprites.TopPipe(screen,y-90)
    botPipe = pySprites.BotPipe(screen,y+90)
    pipeGroup = pygame.sprite.Group(topPipe,botPipe)
    message = pySprites.Message()
    floorGroup = pygame.sprite.Group(floor)
    allSprites = pygame.sprite.OrderedUpdates(background,pipeGroup,floorGroup,player,endzone,message)
    
    # A - ACTION
    # A - ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True
 
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)
 
    #spwan timer for my pipes
    timer = 0
    
    # L - LOOP
    while keepGoing:
     
        # TIME
        clock.tick(60)
        
        # E - EVENT HANDLING    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
                if event.key == pygame.K_q:
                    keepGoing = False
        
        timer += 1  
        if timer%60 == 0:
            # center opening point between the 2 pipes
            y = random.randint(200,500)
            
            #spwan the new set of pipes
            a = pySprites.TopPipe(screen,y-90)
            b = pySprites.BotPipe(screen,y+90)
            pipeGroup.add(a,b)
            allSprites = pygame.sprite.OrderedUpdates(background,pipeGroup,floorGroup,player,endzone,message)
        
        #Checks if player has pass though the open of the pipes if it happens
        # than 1 point is added and a sound effect is played
        for i in pipeGroup:
            if i.rect.right == 150:
                mySound = pygame.mixer.Sound("nice.wav")
                mySound.play(0)
                mySound.set_volume(0.3)                

        # R - REFRESH SCREEN
        allSprites.update()
        allSprites.draw(screen)       
        pygame.display.flip()
         
    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)
    
def main():
    """This function is our "mainline logic" or main loop for our Flappy Bird game."""

    # D - DISPLAY
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Flappy Bird")
     
    # E - ENTITIES
    background = pySprites.Background()
    pygame.mixer.music.load("song.wav")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
     
    # center opening point between the 2 pipes
    y = random.randint(200,500)
    
    # Sprites for: ScoreKeeper label, End Zones, Pipes, and Players
    floor = pySprites.Floor(screen)
    player = pySprites.Player(screen)
    endzone = pySprites.EndZone(screen)
    topPipe = pySprites.TopPipe(screen,y-90)
    botPipe = pySprites.BotPipe(screen,y+90)
    pipeGroup = pygame.sprite.Group(topPipe,botPipe)
    scoreKeeper = pySprites.ScoreKeeper()
    floorGroup = pygame.sprite.Group(floor)
    allSprites = pygame.sprite.OrderedUpdates(background,pipeGroup,floorGroup,player,endzone,scoreKeeper)
    
    # A - ACTION
    # A - ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True
 
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)
 
    #spwan timer for my pipes
    timer = 0
    
    # L - LOOP
    while keepGoing:
     
        # TIME
        clock.tick(60)
        
        # E - EVENT HANDLING    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
        
        timer += 1  
        if timer%60 == 0:
            # center opening point between the 2 pipes
            y = random.randint(200,500)
            
            #spwan the new set of pipes
            a = pySprites.TopPipe(screen,y-90)
            b = pySprites.BotPipe(screen,y+90)
            pipeGroup.add(a,b)
            allSprites = pygame.sprite.OrderedUpdates(background,pipeGroup,floorGroup,player,endzone,scoreKeeper)
            
        #Checks if player has pass though the open of the pipes if it happens
        # than 1 point is added and a sound effect is played
        for i in pipeGroup:
            if (i.rect.right <= 150) and not i.scored:
                mySound = pygame.mixer.Sound("nice.wav")
                mySound.play(0)
                mySound.set_volume(0.3)                
                scoreKeeper.playerScored()

                i.scored = True


          
        #Checks if player hit the top if so they lose and the game closes
        if player.rect.colliderect(endzone):
            mySound = pygame.mixer.Sound("oof.wav")
            mySound.play(0)
            mySound.set_volume(0.3)            
            keepGoing = False

        # Checks if player hit the top if so they lose and the game closes
        if pygame.sprite.spritecollide(player,floorGroup,False):
            mySound = pygame.mixer.Sound("oof.wav")
            mySound.play(0)
            mySound.set_volume(0.3)
            keepGoing = False

        #Checks if player hit the pipes if so they lose and the game closes
        if pygame.sprite.spritecollide(player,pipeGroup,False):
            mySound = pygame.mixer.Sound("oof.wav")
            mySound.play(0)
            mySound.set_volume(0.3)
            keepGoing = False
            
        
        # R - REFRESH SCREEN
        allSprites.update()
        allSprites.draw(screen)       
        pygame.display.flip()
         
    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)
 
    # Close the game window
    pygame.quit()    

# Call the startScreen function
startScreen()
# Call the main function
main()        