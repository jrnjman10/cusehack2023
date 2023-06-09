import pygame
import pygame.image

pygame.init()   

pygame.display.set_caption('Otto Pilot')

screen_width, screen_height = 800, 600

screen = pygame.display.set_mode((screen_width,screen_height))

playerPositionX,playerPositionY = 0, screen_height-32



yGrav = 1

jumpHeight = 20

class Player:
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, x, y):
       # Call the parent class (Sprite) constructor
       self.image = pygame.image.load("Images/otto-right.png")
       pygame.sprite.Sprite.__init__(self)
       self.size = self.image.get_size()
       self.biggerimage = pygame.transform.scale(self.image, ((int(self.size[0])*5), (int(self.size[1])*5)))
       self.rect = self.image.get_rect()
       self.x = int(x)
       self.y = int(y)
       self.velX = 0
       self.velY = 0
       self.color = color
       self.left = False
       self.right = False
       self.up = False
       self.jumping = False
       self.speed = jumpHeight
    def draw(self, screen):
        screen.blit(self.biggerimage, self.rect)

def update(self):
    self.velX = 0

    if self.left and not self.right:
        self.velX = -self.speed
    if self.right and not self.left:
        self.velX = self.speed
    if self.jumping:
        print("jumping")
        self.y -= self.velY
        self.velY -= yGrav
        if self.velY < -jumpHeight:
            self.jumping = False
            self.velY = jumpHeight
    else:
        self.velY -= yGrav
        
    self.x += self.velX
    
    self.rect = pygame.Rect(self.x,self.y, 32, 32)

'''
    def update(self):
        self.velX = 0
        self.velY = self.speed

        if self.left and not self.right:
            self.velX = -self.speed
        if self.right and not self.left:
            self.velX = self.speed
        if self.jumping:
            print("jumping")
            self.y -= self.velY
            self.velY -= yGrav
            if self.velY < -jumpHeight:
                self.jumping = False
                self.velY = jumpHeight
        else:
            self.velY = 0      




        
        self.x += self.velX
        
        self.rect = pygame.Rect(self.x,self.y, 32, 32)'''
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

player = Player("green",playerPositionX,playerPositionY)



jumping = False



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
            elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.right = True
            elif event.key == pygame.K_UP or event.key == ord('w') or pygame.K_SPACE and not jumping:
                player.jumping = True
            else:
                print("nokey")
            if event.key == ord('q'):
                pygame.quit() 



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.left = False
            elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.right = False
            elif event.key == pygame.K_UP or event.key == ord('w') or pygame.K_SPACE:
                player.up = False
            else:
                print("nokey")
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


