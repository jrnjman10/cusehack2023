import pygame
from os import listdir
from os.path import isfile, join

pygame.init()   

pygame.display.set_caption('Otto Pilot')

screen_width, screen_height = 1080, 800

screen = pygame.display.set_mode((screen_width,screen_height))

playerPositionX,playerPositionY = 0, screen_height-32


#Sources https://www.youtube.com/watch?v=B6DrRN5z_uU

PLAYER_VEL = 5

FPS = 60

def get_block(size):
    path = join("SomeGame", "Images", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()     #For some reason the mask isn't working on this image
    surface = pygame.Surface((size,size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96,0,size,size)
    surface.blit(image,(0,0),rect)
    return pygame.transform.scale2x(surface)

class Player(pygame.sprite.Sprite):
    color = (255,0,0)
    GRAVITY = 1
    def __init__(self, x,y, width, height):
       super().__init__()
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

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       #self.rect = self.image.get_rect()


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, screen, offset_x):
        screen.blit(self.image, (self.rect.x - offset_x, self.rect.y))


class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)



#Objects


def draw(screen,player,objects):

    screen.fill(color)

    for obj in objects:
        obj.draw(screen, offset_x)

    player.draw(screen)
    pygame.display.update()




running = True 

color = "blue"

#need a blocksize
block_size = 96


player = Player(playerPositionX,playerPositionY,32,32)
floor = [Block(i * block_size, screen_height - block_size, block_size)
        for i in range(-screen_width // block_size, (screen_width * 2) // block_size)]

clock = pygame.time.Clock()


def handle_move(player,objects):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VEL)
    
    handle_vertical_collision(player,objects, player.y_vel)


def handle_vertical_collision(player, objects,dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0: 
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

        collided_objects.append(obj)

    return collieded_objects

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
    handle_move(player,floor)

    #Draw
    draw(screen,player,floor)

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


