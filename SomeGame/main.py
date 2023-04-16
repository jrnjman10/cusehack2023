import pygame

pygame.init()   

screen_width, screen_height = 600, 400

screen = pygame.display.set_mode((screen_width,screen_height))





class Player:
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, x, y):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
       self.rect = pygame.Rect(x,y,32,32)
       self.x = int(x)
       self.y = int(y)
       self.velX = 0
       self.velY = 0
       self.color = "blue"
       self.left = False
       self.right = False
       self.up = False
       self.down = False
       self.speed = 4
       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       #self.image = pygame.Surface([width, height])
       #self.image.fill(color)
    def draw(self, screen):
        #could be self.image
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left and not self.right:
            self.velX = -self.speed
        if self.right and not self.left:
            self.velX = self.speed
        if self.up and not self.down:
            self.velY = -self.speed
        if self.down and not self.up:
            self.velY = self.speed
        
        self.x += self.velX
        self.y += self.velY
        
        self.rect = pygame.Rect(self.x,self.y, 32, 32)
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       #self.rect = self.image.get_rect()

# x location, y location, img width, img height, img file
class Platform(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img)).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc



#Objects

player = Player("green",screen_width/2,screen_height/2)







running = True 

color = "red"



#player.rect.x = 32   # go to x
#player.rect.y = 32   # go to y

clock = pygame.time.Clock()

while running:
   
    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():
         
        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.left = True
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.right = True
            if event.key == pygame.K_UP or event.key == ord('w') or pygame.K_SPACE:
                player.up = True
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.down = True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.left = False
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.right = False
            if event.key == ord('q'):
                pygame.quit() 
       
    #Draw
    screen.fill(color)
    player.draw(screen)

    # set background color to our window
     
    # Update our window
    player.update()
    pygame.display.flip()
    pygame.display.set_caption('Otto Pilot')

    clock.tick(120)
     

'''
Player controls
Images
'''

'''
Player class

Enemy Class

Platform class
    Moving Platforms
    Platforms


Someone stole otto's scooter
he has to get his scooter
'''


