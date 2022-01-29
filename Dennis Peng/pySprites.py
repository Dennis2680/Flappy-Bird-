"""
May  28,2019
Dennis Peng
This program contain all the object used in my game and they way they act and work.
"""
import pygame 

class Player(pygame.sprite.Sprite):
    '''This class defines the sprite for Player'''
    def __init__(self, screen):
        '''This initializer takes a screen surface as parameter.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)    

        #frame counter
        self.counter = 0
        # Set the image and rect attributes for the player
        self.bird = [pygame.image.load("Bird1.png"), pygame.image.load("Bird2.png")]
        self.current_image = 0
        self.image = self.bird[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.center = (150, screen.get_height()/2-50)
        
        # Instance variables to keep track of the screen surface
        # and set the initial y vector for the player.
        self.window = screen
        self.dy = -9.8
        
    def jump(self):
        '''This lets the player jump by increasing the player centre y value.'''
        self.dy = 7
    
    def update(self):
        '''This method will be called automatically to reposition the
        player sprite on the screen.'''

        # flip the images
        self.counter += 1
        if self.counter % 30 == 0:
            self.current_image += 1
            if self.current_image >= len(self.bird):
                self.current_image = 0
            self.image = self.bird[self.current_image]

        # Check if we have reached the top or bottom of the screen.
        # If not, then keep moving the player in the same y direction.
        if ((self.rect.top > -1) and (self.dy > 0)) or\
           ((self.rect.bottom < self.window.get_height()+10) and (self.dy < 0)):
            self.rect.top -= self.dy
            self.dy -= 9.8/30


            
class EndZone(pygame.sprite.Sprite):
    '''This class defines the sprite for our top end zone'''
    def __init__(self, screen):
        '''This initializer takes a screen surface as parameters. 
        For player the end zone is located at the top of the 
        screen if the player hits it the player dies.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
                
        # Our endzone sprite will be a 1 pixel tall black line.
        self.image = pygame.Surface((screen.get_width(),1))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))
         
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        
class TopPipe(pygame.sprite.Sprite):
    '''This class define the top pipe that the player has to avoid.'''
    def __init__(self, screen,y):
        ''' '''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Keep track of the screen so we can call get_witdth()
        self.window = screen
         
        # Define a Surface for our Box Sprite
        self.image = pygame.image.load("TopPipe.png").convert()
        
        # Define the position of our Box using it's rect
        self.rect = self.image.get_rect()
        self.rect.left = 1400
        self.rect.bottom = y

        self.scored = False
        
    def update(self):
        '''Automatically called in the refresh section to update our TopPipe Sprite's position.'''
        self.rect.left -= 10
        self.rect.bottom += 0
        
        #if pipe goes off the screen it kills it 
        if self.rect.right == 0:
            self.kill()
            
class BotPipe(pygame.sprite.Sprite):
    '''This class define the bottom pipe that the player has to avoid.'''
    def __init__(self, screen,y):
        ''' '''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Keep track of the screen so we can call get_witdth()
        self.window = screen
         
        # Define a Surface for our Box Sprite
        self.image = pygame.image.load("BotPipe.png").convert()

        # Define the position of our Box using it's rect
        self.rect = self.image.get_rect()
        self.rect.left = 1400
        self.rect.top = y

        self.scored = False
        
    def update(self):
        '''Automatically called in the refresh section to update our BotPipe Sprite's position.'''
        self.rect.left -= 10
        self.rect.top += 0
        
        #if pipe goes off the screen it kills it 
        if self.rect.right == 0:
            self.kill()
            
class ScoreKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self):
        '''This initializer loads the system font "Arial", and
        sets the starting score is 0.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Load our custom font, and initialize the starting score.
        self.font = pygame.font.SysFont("Arial", 30)
        self.playerScore = 0
         
    def playerScored(self):
        '''This method adds points for the player'''
        self.playerScore += 0.5
        
    def update(self):
        '''This method will be called automatically to display 
        the current score at the top of the game window.'''
        message = "Score: " + str(round(self.playerScore)) 
        self.image = self.font.render(message, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (320, 15)    
        
class Message (pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self):
        '''This initializer loads the system font "Arial", and
        sets the starting score is 0.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Load our custom font, and initialize the starting score.
        self.font = pygame.font.SysFont("Arial", 30)
        
    def update(self):
        '''This method will be called automatically to display 
        the current score at the top of the game window.'''
        message = "PRESS Q TO START GAME"
        self.image = self.font.render(message, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (320, 15)  
        
class Background(pygame.sprite.Sprite):
    '''This class defines a scrolling background sprite to display the background.'''
    def __init__(self):
        '''This initializer take the screen surface as a parameter and load the 
        background.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        #Define the image attributes for a rectangles.
        self.image = pygame.image.load("Background.png").convert()
        self.rect = self.image.get_rect()
        self.rect.left = 0

    def update(self):
        '''Automatically called in the refresh section to update our BotPipe Sprite's position.'''
        self.rect.left -= 12  
        
        if self.rect.center[0] <= 0:
            self.rect.left = 0            
            
class Floor(pygame.sprite.Sprite):
    '''This class defines a scrolling background sprite to display the floor.'''
    def __init__(self,screen):
        '''This initializer take the screen surface as a parameter and load the 
        floor.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen
        #Define the image attributes for a rectangles.
        self.image = pygame.image.load("Floor.png").convert()
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.bottom = self.screen.get_size()[1] + 50

    def update(self):
        '''Automatically called in the refresh section to update our BotPipe Sprite's position.'''
        self.rect.left -= 11

        if self.rect.center[0] <= 0:
            self.rect.left = 0