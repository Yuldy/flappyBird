#Christian Phan 
#Flappy Bird - Mock - 5/24/22
import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60


#screen size:
screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))

#titling the broswer itself:
pygame.display.set_caption('Flappy Bird')


#define game variables
ground_scroll = 0
scroll_speed = 4 #move by 4 pixels



#load images
bg = pygame.image.load('/Users/christianphan/Documents/FlappyBird/assets/flappyBirdBackground.png')
ground_img = pygame.image.load('/Users/christianphan/Documents/FlappyBird/assets/ground.png')


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0 #controls the speed of the animation when it runs
        for num in range(1, 4):
            img = pygame.image.load('/Users/christianphan/Documents/FlappyBird/assets/bird1.png')
            img1 = pygame.image.load('/Users/christianphan/Documents/FlappyBird/assets/bird2.png')
            img2 = pygame.image.load('/Users/christianphan/Documents/FlappyBird/assets/bird3.png')
            self.images.append(img) 
            self.images.append(img1)
            self.images.append(img2)

        self.image = self.images[self.index]
        self.rect = self.image.get_rect() #creates rect around the image
        self.rect.center = [x, y]
        self.vel = 0


    def update(self):
        
        self.vel += 0.5
        if self.rect.bottom < 768:
            self.rect.y += int(self.vel)
    
        #handles the animation portion:
        self.counter += 1
        flap_cooldown = 5

        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images): #ensures that it doesn't go outside of an index from the list.
                self.index = 0
        self.image = self.images[self.index]
        


bird_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))

bird_group.add(flappy)



#this allows you to quite the game through the window:
run = True
while run:

    clock.tick(fps)

    #draw background
    screen.blit(bg, (0,0))

    bird_group.draw(screen)

    #draw and scroll the ground
    screen.blit(ground_img, (ground_scroll, 768))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35: #if the ground scroll image exceeds 35 pixels, it will reset the iamge
        ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
