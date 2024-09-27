import pygame  #import pygame module
import random
import time
# a= int(input("start"))
pygame.init()  # initialize pygame
score = 0
diabetes = 0
drop_speed = .51
collect_location = 0
# Step 1: create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PLAYER_SURFACE = pygame.image.load('Cookie_Jar.png').convert_alpha()
PLAYER_SURFACE = pygame.transform.scale(PLAYER_SURFACE, (200, 150))
PLAYER = PLAYER_SURFACE.get_rect(midbottom=(400, 600))

BG_SURFACE = pygame.image.load('PLANET_OF_DESSERT.jpeg').convert_alpha()
BG_SURFACE = pygame.transform.scale(BG_SURFACE, (800, 600))
BACKROUND = BG_SURFACE.get_rect()

Cookie_SURFACE = pygame.image.load('cookie.png').convert_alpha()
Cookie_SURFACE = pygame.transform.scale(Cookie_SURFACE, (61, 61))
Cookie = Cookie_SURFACE.get_rect(midbottom=(random.randint(0, SCREEN_WIDTH),
                                            50))

font = pygame.font.Font('cookie.ttf', 50)
font2 = pygame.font.Font('end.otf', 50)
# Step 2: create the game loop

run = True
while run:
    Cookie.y += drop_speed
    #check to see if it needs to move up
    if PLAYER.colliderect(Cookie):
        Cookie.x = random.randint(0, SCREEN_WIDTH)
        Cookie.y = 50
        score = score + 1
        drop_speed = drop_speed+.05
        diabetes = score
    elif Cookie.y >= 600:
        print("Cookie Fell")
        print("respawning...")
        Cookie.x = random.randint(0, SCREEN_WIDTH)
        Cookie.y = 50
        score = 0
        drop_speed = .51

        # text_surface2 = font2.render('Score you got diabetes', True, (255, 255, 255), (245, 32, 78))
        
        # code = catching cookies
    if diabetes >= 40 and diabetes <= 50:
        text_surface = font.render('YOU GOT DIABETES', True, (255, 255, 255), (245, 32, 78))
        text = text_surface.get_rect()
        time.sleep(3)
    else:
        text_surface = font.render(('Score  '+str(score)), True, (255, 255, 255), (245, 32, 78))
        text = text_surface.get_rect()
    screen.blit(BG_SURFACE, BACKROUND)
    screen.blit(Cookie_SURFACE, Cookie)
    screen.blit(PLAYER_SURFACE, PLAYER)
    screen.blit(text_surface, text)

    key = pygame.key.get_pressed()
    #add up and down limit/barrier
    if key[pygame.K_RIGHT] == True:
        PLAYER.x += 2
    if key[pygame.K_LEFT] == True:
        PLAYER.x -= 2
    # Step 3: Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    pygame.time.Clock().tick(600)