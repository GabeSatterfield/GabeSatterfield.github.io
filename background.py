#work in progress but this is what I have so far
import pygame

screen = pygame.display.set_mode((1280,768))

# This creates images for background
back = pygame.image.load("Assets/Background/PNG/Tiles/Ground_Tile_02_C.png").convert_alpha()
mud = pygame.transform.scale(back,(64,64))
corner = pygame.image.load("Assets/Background/PNG/Hedges/Hedge_B_01.png").convert_alpha()
tlcorner = pygame.transform.scale(corner,(64,64))
trcorner = pygame.transform.rotate(tlcorner,-90)
brcorner = pygame.transform.rotate(tlcorner,180)
blcorner = pygame.transform.rotate(tlcorner,90)
sides = pygame.image.load("Assets/Background/PNG/Hedges/Hedge_B_02.png").convert_alpha()
top = pygame.transform.scale(sides,(64,64))
rside = pygame.transform.rotate(top,-90)
bottom = pygame.transform.rotate(top,180)
lside = pygame.transform.rotate(top,90)

#this creates the player
char_sprite = pygame.image.load("Assets/Character/PNG/Hulls_Color_D/Hull_01.png").convert_alpha()
char_tank = pygame.transform.scale(char_sprite,(64,64))
player = char_tank.get_rect(center = (640,384))
char_right = pygame.transform.rotate(char_tank,-90)
char_down = pygame.transform.rotate(char_tank,180)
char_left = pygame.transform.rotate(char_tank,90)


window = screen.get_rect()
speed = 3

clock = pygame.time.Clock()

up = False
down = False
left = False
right = False

#calling this method refreshes the visuals for the game
def update():

    #generates the muddy background
    for i in range(0,1280,64):
        for j in range(0,768,64):
            screen.blit(mud,(i,j))

    #generates the grassy edges, starting in top left and moving clockwise
    screen.blit(tlcorner,(0,0))

    for i in range(64,1216,64):
        screen.blit(top,(i,0))

    screen.blit(trcorner,(1216,0))

    for i in range(64,704,64):
        screen.blit(rside,(1216,i))

    screen.blit(brcorner,(1216,704))

    for i in range(64,1216,64):
        screen.blit(bottom,(i,704))

    screen.blit(blcorner,(0,704))

    for i in range(64,704,64):
        screen.blit(lside,(0,i))
    # This part should rotate the tank based on what direction the player is moving
    if up and not (right or left):
        screen.blit(char_tank,player)
    elif left and not (up or down):
        screen.blit(char_left,player)
    elif down:
        screen.blit(char_down,player)
    elif right and not (up or down):
        screen.blit(char_right,player)
    else:
        screen.blit(char_tank,player)

    #updates player position
    pygame.display.flip()

update()

running = True
while running:
    #controller
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                up = True
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_s:
                down = True
            if event.key == pygame.K_d:
                right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                up = False
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_s:
                down = False
            if event.key == pygame.K_d:
                right = False
    #player movement
    if up:
        if player.top > window.top:
            player = player.move(0,-speed)
    if left:
        if player.left > window.left:
            player = player.move(-speed,0)
    if down:
        if player.bottom < window.bottom:
            player = player.move(0,speed)
    if right:
        if player.right < window.right:
            player = player.move(speed,0)

    update()

    #establishes refresh rate at 60 fps
    clock.tick(60)
