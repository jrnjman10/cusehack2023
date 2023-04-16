import pygame

pygame.init()   

screen_width, screen_height = 600, 400

screen = pygame.display.set_mode((screen_width,screen_height))

running = True 

color = "red"

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
                print('left')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right')
            if event.key == pygame.K_UP or event.key == ord('w') or pygame.K_SPACE:
                print('jump')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left stop')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right stop')
            if event.key == ord('q'):
                pygame.quit()
     
    # set background color to our window
    screen.fill(color)
     
    # Update our window
    pygame.display.flip()
     
    # if color is red change it to green and
    # vice-versa
    if(color == "red"):
        color = "green"
         
    else:
        color = "red"

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


class Player ():
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

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

