import pygame

pygame.init()   

pygame.display.set_caption('Otto Pilot')

screen_width, screen_height = 1080, 800

screen = pygame.display.set_mode((screen_width,screen_height))

playerPositionX,playerPositionY = 0, screen_height-32


#Sources https://www.youtube.com/watch?v=B6DrRN5z_uU

PLAYER_VEL = 5

FPS = 60

class Player(pygame.sprite.Sprite):
    color = (255,0,0)
    GRAVITY = 1
    def __init__(self, x,y, width, height):
       self.rect = pygame.Rect(x, y, width, height)
       self.x_vel = 0
       self.y_vel = 0
       self.mask = None
       self.direction = "left"
       self.animation_count = 0
       self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
    
    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0
    
    def loop(self,fps):
        self.y_vel += min(1, (self.fall_count / FPS) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        self.fall_count += 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
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


def draw(screen,player):
    screen.fill(color)
    player.draw(screen)
    pygame.display.update()




running = True 

color = "blue"



#player.rect.x = 32   # go to x
#player.rect.y = 32   # go to y

clock = pygame.time.Clock()


def handle_move(player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VEL)

player = Player(playerPositionX,playerPositionY,32,32)

while running:
   
    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():
         
        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    player.loop(FPS)
    handle_move(player)

    #Draw
    draw(screen,player)

    pygame.display.flip()
    pygame.display.set_caption('Otto Pilot')

    clock.tick(FPS)            

'''
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
'''
            

       
     

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


