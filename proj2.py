import pygame
import os, time


# it is better to have an extra variable, than an extremely long line.
img_path1 = os.path.join('dora.png')
img_path2 = os.path.join('dora_left.png')
img_path3 = os.path.join('dora_there.png')
img_path4 = os.path.join('dora_up.png')

img_bk1 = os.path.join('traffic.png')

class Sprite(object):  # represents the sprite, not the game
    def __init__(self):
        """ The constructor of the class """
        self.image1 = pygame.image.load(img_path1)
        self.image2 = pygame.image.load(img_path2)
        self.image3 = pygame.image.load(img_path3)
        self.image4 = pygame.image.load(img_path4)
        self.image = self.image1
        self.imageBk1 = pygame.image.load(img_bk1)
        self.imageBk1 = pygame.transform.scale(self.imageBk1, (900, 700))
        self.imageBk1_rect = self.imageBk1.get_rect()

        # the bird's position
        self.x = 0
        self.y = 0

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 5 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.image=self.image3
            self.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.image=self.image4
            self.y -= dist # move up
        elif key[pygame.K_RIGHT]: # right key
            self.image=self.image1
            self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left
            self.image=self.image2

    def draw(self, surface):
        """ Draw on surface """
        surface.blit(self.imageBk1,self.imageBk1_rect)
        # blit yourself at your current position
        surface.blit(self.image,(self.x, self.y))
        #pygame.display.flip()
        #url= 
        showtext("Cars release approximately 333 million tons of carbon")
        showtext2("dioxide into the atmosphere annually.")
        pygame.display.update()
        #os.sleep(5)


def showtext(txtMsg):
    #pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(txtMsg, False, (0, 0, 0))
    screen.blit(textsurface,(80,550))
    #time.sleep(2)

def showtext2(txtMsg):
    #pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(txtMsg, False, (0, 0, 0))
    screen.blit(textsurface,(80,600))
    #time.sleep(2)



pygame.init()
screen = pygame.display.set_mode((900,700))

sprite = Sprite() # create an instance
clock = pygame.time.Clock()

#showtext("hi hi1")

running = True
while running:
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False
            break;
        elif  event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit() # quit the screen
                running = False
                break;


    if running == True:
        sprite.handle_keys() # handle the keys

        screen.fill((255,255,255)) # fill the screen with white
        sprite.handle_keys() # handle the keys

        sprite.draw(screen) # draw the bird to the screen
        pygame.display.update() # update the screen

        clock.tick(40)
    

