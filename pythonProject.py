#work in progress but this is what I have so far
import pygame

screen = pygame.display.set_mode((1280,768))

# This creates images for background
'''NOTE: This will not work without the files listed in the right file locations'''

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
player = char_tank.get_rect(center = (25,384))
char_right = pygame.transform.rotate(char_tank,-90)
char_down = pygame.transform.rotate(char_tank,180)
char_left = pygame.transform.rotate(char_tank,90)

conA_image = pygame.image.load("Assets/Objects/PNG/Decor_Items/Container_A.png").convert_alpha()
conB_image = pygame.image.load("Assets/Objects/PNG/Decor_Items/Container_B.png").convert_alpha()
conC_image = pygame.image.load("Assets/Objects/PNG/Decor_Items/Container_C.png").convert_alpha()
conD_image = pygame.image.load("Assets/Objects/PNG/Decor_Items/Container_D.png").convert_alpha()
barrier = pygame.image.load("Assets/Objects/PNG/Decor_Items/Czech_Hdgehog_A.png").convert_alpha()

conA_small = pygame.transform.scale(conA_image,(130,250))
#Rects that are used for image display
y1= conA_small.get_rect(topleft = (65,69))
y2 = conA_small.get_rect(topleft = (65,450))
y3 = conA_small.get_rect(topleft = (830,69))
y4 = conA_small.get_rect(topleft = (830,449))
y5 = conA_small.get_rect(topleft = (1025,69))
y6 = conA_small.get_rect(topleft = (1025,449))

#Rects that are used for hitboxes
y_S = pygame.Surface((127,123))
y1_rect = pygame.Rect(67,133,127,123)
y2_rect = pygame.Rect(67,514,127,123)
y3_rect = pygame.Rect(832,133,127,123)
y4_rect = pygame.Rect(832,513,127,123)
y5_rect = pygame.Rect(1027,133,127,123)
y6_rect = pygame.Rect(1027,513,127,123)

#when container is flipped the scaling x and y are reversed x=y y=x
conB_small = pygame.transform.scale(conB_image, (290,300))
vertical_conB = pygame.transform.rotate(conB_small, 90)
r1 = vertical_conB.get_rect(topleft = (245,65))
r2 = vertical_conB.get_rect(topleft = (245,415))

#Rects that are used for hitboxes
r_S = pygame.Surface((144,285))
r1_rect = pygame.Rect(323,67,144,285)
r2_rect = pygame.Rect(323,417,144,285)

conC_small = pygame.transform.scale(conC_image, (125,125))
vertical_conC = pygame.transform.rotate(conC_small, 90)
g1 = conC_small.get_rect(topleft = (640,101))
g2 = vertical_conC.get_rect(topleft = (608,513))

#Rects that are used for hitboxes
g_S = pygame.Surface ((125,61))
g1_rect = pygame.Rect(640,133,125,61)
g2_S = pygame.Surface ((61,125))
g2_rect = pygame.Rect(640,133,61,125)

conD_small = pygame.transform.scale(conD_image, (125,125))
vertical_conD = pygame.transform.rotate(conD_small, 90 )
b1 = conD_small.get_rect(topleft = (640,481))
b2 = vertical_conD.get_rect(topleft = (608,133))

#Rects that are used for hitboxes
b_S = pygame.Surface ((125,61))
b1_rect = pygame.Rect(640,513,125,61)
b2_S = pygame.Surface((61,125))
b2_rect = pygame.Rect(640,513,61,125)

barrier_small1 = pygame.transform.scale(barrier, (50,50))
h1 = barrier_small1.get_rect(topleft = (575, 330))
barrier_small2 = pygame.transform.scale(barrier, (50,50))
h2 = barrier_small2.get_rect(topleft = (575, 370))
barrier_small3 = pygame.transform.scale(barrier, (50,50))
h3 = barrier_small3.get_rect(topleft = (575, 410))

h_S = pygame.Surface ((39,123))
h_rect = pygame.Rect(581,335,39,123)
#Rects that are used for hitboxes


Ps = pygame.Surface((25,25))
Ps.fill((255,0,0))

Pr1 = pygame.Rect(25,25,25,25)
Pr1.left = y1.right + 10
Pr1.centery = y1.centery
Pr2 = pygame.Rect(25,25,25,25)
Pr2.bottom = y1.top + 45
Pr2.centerx = y1.centerx

Pr3 = pygame.Rect(25,25,25,25)
Pr3.left = y2.right + 10
Pr3.centery = y2.centery
Pr4 = pygame.Rect(25,25,25,25)
Pr4.top = y2.bottom - 40
Pr4.centerx = y2.centerx

Pr5 = pygame.Rect(25,25,25,25)
Pr5.left = r1.right - 65
Pr5.centery = r1.centery
Pr6 = pygame.Rect(25,25,25,25)
Pr6.bottom = r1.top
Pr6.centerx = r1.centerx

Pr7 = pygame.Rect(25,25,25,25)
Pr7.left = r2.right - 65
Pr7.centery = r2.centery
Pr8 = pygame.Rect(25,25,25,25)
Pr8.top = r2.bottom
Pr8.centerx = r2.centerx

Pr9 = pygame.Rect(25,25,25,25)
Pr9.bottom = g1.top +20
Pr9.centerx = g1.centerx
Pr10 = pygame.Rect(25,25,25,25)
Pr10.top = g1.bottom -20
Pr10.centerx = g1.centerx + 20

Pr11 = pygame.Rect(25,25,25,25)
Pr11.bottom = b1.top +20
Pr11.centerx = b1.centerx - 25
Pr12 = pygame.Rect(25,25,25,25)
Pr12.top = b1.bottom -20
Pr12.centerx = b1.centerx + 20

Pr13 = pygame.Rect(25,25,25,25)
Pr13.bottom = y3.top + 45
Pr13.centerx = y3.centerx
Pr14 = pygame.Rect(25,25,25,25)
Pr14.top = y3.bottom - 50
Pr14.centerx = y3.centerx

Pr15 = pygame.Rect(25,25,25,25)
Pr15.bottom = y4.top + 45
Pr15.centerx = y4.centerx
Pr16 = pygame.Rect(25,25,25,25)
Pr16.top = y4.bottom - 50
Pr16.centerx = y4.centerx

Pr17 = pygame.Rect(25,25,25,25)
Pr17.bottom = y5.top + 45
Pr17.centerx = y5.centerx
Pr18 = pygame.Rect(25,25,25,25)
Pr18.top = y5.bottom - 50
Pr18.centerx = y5.centerx

Pr19 = pygame.Rect(25,25,25,25)
Pr19.bottom = y6.top + 45
Pr19.centerx = y6.centerx
Pr20 = pygame.Rect(25,25,25,25)
Pr20.top = y6.bottom - 50
Pr20.centerx = y6.centerx

Pr21 = pygame.Rect(25,25,25,25)
Pr21.left = y5.right + 15
Pr21.centery = y5.centery
Pr22 = pygame.Rect(25,25,25,25)
Pr22.left = y6.right + 15
Pr22.centery = y6.centery

Pr23 = pygame.Rect(25,0,25,25)
Pr23.left = y4.right + 22
Pr24 = pygame.Rect(25,743,25,25)
Pr24.left = y4.right + 22

Pr25 = pygame.Rect(25,374,25,25)
Pr25.right = y4.left - 22

obstacle_list = [y1_rect,y2_rect,y3_rect,y4_rect,y5_rect,y6_rect,r1_rect,r2_rect,g1_rect,g2_rect,b1_rect,b2_rect,h_rect]
enemy_position = []

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

    #blits the containers and objects

    #yellow container
    screen.blit(conA_small, y1)  # Left Top Square (y1)
    screen.blit(conA_small, y2)  # Left Bottom Square (y2)
    screen.blit(conA_small, y3)  # Right Top Square 1 (y3)
    screen.blit(conA_small, y4)  # Right Bottom Square 1 (y4)
    screen.blit(conA_small, y5)  # Right Top Square 2 (y5)
    screen.blit(conA_small, y6)  # Right Bottom Square 2 (Y6)
    #red container
    screen.blit(vertical_conB, r1) # top red container r1
    screen.blit(vertical_conB, r2) #bottom red container r2
    #green container
    screen.blit(conC_small, g1)
    screen.blit(vertical_conC, g2)
    #blue container
    screen.blit(conD_small, b1) #b1
    screen.blit(vertical_conD, b2) #b2
    #barrier
    screen.blit(barrier_small1, h2) #h2
    screen.blit(barrier_small1, h1) #h1
    screen.blit(barrier_small1, h3) #h3




    '''''
    #Shows the positioning of the obstacle's hitbox
    screen.blit(y_S, y1_rect)
    screen.blit(y_S, y2_rect)
    screen.blit(y_S, y3_rect)
    screen.blit(y_S, y4_rect)
    screen.blit(y_S, y5_rect)
    screen.blit(y_S, y6_rect)
    screen.blit(r_S, r1_rect)
    screen.blit(r_S, r2_rect)
    screen.blit(g_S, g1_rect)
    screen.blit(g2_S, g2_rect)
    screen.blit(b_S, b1_rect)
    screen.blit(b2_S, b2_rect)
    screen.blit(h_S, h_rect)
    '''''

    '''''
    #postitions
    screen.blit(Ps, Pr1)
    screen.blit(Ps, Pr2)
    screen.blit(Ps, Pr3)
    screen.blit(Ps, Pr4)
    screen.blit(Ps, Pr5)
    screen.blit(Ps, Pr6)
    screen.blit(Ps, Pr6)
    screen.blit(Ps, Pr7)
    screen.blit(Ps, Pr8)
    screen.blit(Ps, Pr9)
    screen.blit(Ps, Pr10)
    screen.blit(Ps, Pr11)
    screen.blit(Ps, Pr12)
    screen.blit(Ps, Pr13)
    screen.blit(Ps, Pr14)
    screen.blit(Ps, Pr15)
    screen.blit(Ps, Pr16)
    screen.blit(Ps, Pr17)
    screen.blit(Ps, Pr18)
    screen.blit(Ps, Pr19)
    screen.blit(Ps, Pr20)
    screen.blit(Ps, Pr21)
    screen.blit(Ps, Pr22)
    screen.blit(Ps, Pr23)
    screen.blit(Ps, Pr24)
    screen.blit(Ps, Pr25)
    '''''

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


    #this is the collision I created
    keys = pygame.key.get_pressed()
    for rect in obstacle_list:
        if player.colliderect(rect):
            if keys[pygame.K_d]:
                if player.right >= rect.left:
                    player.x -= speed
            if keys[pygame.K_a]:
                if player.left <= rect.right:
                    player.x += speed
            if keys[pygame.K_w]:
                if player.top <= rect.bottom:
                    player = player.move(0,speed)
            if keys[pygame.K_s]:
                if player.bottom >= rect.top:
                    player.y -= speed



    update()




    pygame.display.flip()

    #establishes refresh rate at 60 fps
    clock.tick(60)