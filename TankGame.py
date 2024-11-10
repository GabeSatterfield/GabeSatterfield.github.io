import pygame, sys
pygam.mixer.init()

screen = pygame.display.set_mode((1280,768))

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

char_sprite = pygame.image.load("Assets/Character/PNG/Hulls_Color_D/Hull_01.png").convert_alpha()
char_tank = pygame.transform.scale(char_sprite,(64,64))
player = char_tank.get_rect(center = (640,384))
char_right = pygame.transform.rotate(char_tank,-90)
char_down = pygame.transform.rotate(char_tank,180)
char_left = pygame.transform.rotate(char_tank,90)
char_upright = pygame.transform.rotate(char_tank,-45)
char_upleft = pygame.transform.rotate(char_tank,45)
char_downleft = pygame.transform.rotate(char_tank,135)
char_downright = pygame.transform.rotate(char_tank,-135)

gun_sprite = pygame.image.load("Assets/Character/PNG/Weapon_Color_D_256X256/Gun_07.png").convert_alpha()
char_gun = pygame.transform.scale(gun_sprite,(64,64))
gun_right = pygame.transform.rotate(char_gun,-90)
gun_down = pygame.transform.rotate(char_gun,180)
gun_left = pygame.transform.rotate(char_gun,90)
gun_upright = pygame.transform.rotate(char_gun,-45)
gun_upleft = pygame.transform.rotate(char_gun,45)
gun_downleft = pygame.transform.rotate(char_gun,135)
gun_downright = pygame.transform.rotate(char_gun,-135)

bullet_sprite = pygame.image.load("Assets/Character/PNG/Effects/Medium_Shell.png").convert_alpha()
player_bullet = pygame.transform.scale(bullet_sprite,(64,64))
shoot_upright = pygame.transform.rotate(player_bullet,-45)
shoot_upleft = pygame.transform.rotate(player_bullet,45)
shoot_right = pygame.transform.rotate(player_bullet,-90)
shoot_left = pygame.transform.rotate(player_bullet, 90)
shoot_downright = pygame.transform.rotate(player_bullet,-135)
shoot_downleft = pygame.transform.rotate(player_bullet,135)
shoot_down = pygame.transform.rotate(player_bullet,180)

conA_image = pygame.image.load("Assets/Objects/PNG/Decor_Items/Container_A.png").convert_alpha()
conB_image = pygame.image.load("Assets/Objects/PNG/Decor_Items/Container_B.png").convert_alpha()
conC_image = pygame.image.load("Assets/Objects/PNG/Decor_Items/Container_C.png").convert_alpha()
conD_image = pygame.image.load("Assets/Objects/PNG/Decor_Items/Container_D.png").convert_alpha()
barrier = pygame.image.load("Assets/Objects/PNG/Decor_Items/Czech_Hdgehog_A.png").convert_alpha()

explosion = pygame.image.load("Assets/Objects/PNG/Bombs/Explosion_A_02.png").convert_alpha()
bulletimpact = pygame.transform.scale(explosion, (64,64))

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

upface = False
leftface = False
downface = False
rightface = False

upright = False
upleft = False
downright = False
downleft = False

shooting = False
shoot = False
cooldown = 0

shootupleft = False
shootup = False
shootupright = False
shootright = False
shootdownright = False
shootdown = False
shootdownleft = False
shootleft = False

cb_collideup = False
cb_collideupright = False
cb_collideright = False
cb_collidedownright = False
cb_collidedown = False
cb_collidedownleft = False
cb_collideleft = False
cb_collideupleft = False

bounce = pygame.mixer.Sound('./Sounds/Bounce.m4a')
bullet = pygame.mixer.Sound('./Sounds/Bullet.mp3')
Explosion = pygame.mixer.Sound('./Sounds/Explosion.wav')
Scoreboard = pygame.mixer.Sound('./Sounds/Scoreboard.m4a')
Tank = pygame.mixer.Sound('./Sounds/Tank.mp3')
Game_Over = pygame.mixer.Sound('./Sounds/GameOver.mp3')
Background = pygame.mixer.Sound('./Sounds/War.mp3')

pygame.mixer.music.load("Assingment 5/bgm.mp3")
pygame.mixer.set_volume(.7)

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
        
    if shootupright:
        screen.blit(shoot_upright,shoot_upright_rect)
    if shootup:
        screen.blit(player_bullet,shoot_up_rect)
    if shootupleft:
        screen.blit(shoot_upleft,shoot_upleft_rect)
    if shootright:
        screen.blit(shoot_right,shoot_right_rect)
    if shootdownright:
        screen.blit(shoot_downright,shoot_downright_rect)
    if shootdown:
        screen.blit(shoot_down,shoot_down_rect)
    if shootdownleft:
        screen.blit(shoot_downleft,shoot_downleft_rect)
    if shootleft:
        screen.blit(shoot_left,shoot_left_rect)
    if shootupleft:
        screen.blit(shoot_upleft,shoot_upleft_rect)

    if upface:
        screen.blit(char_tank,player)
        screen.blit(char_gun,player)
    elif leftface:
        screen.blit(char_left,player)
        screen.blit(gun_left,player)
    elif downface:
        screen.blit(char_down,player)
        screen.blit(gun_down,player)
    elif rightface:
        screen.blit(char_right,player)
        screen.blit(gun_right,player)
    elif upright:
        screen.blit(char_upright,player)
        screen.blit(gun_upright,player)
    elif upleft:
        screen.blit(char_upleft,player)
        screen.blit(gun_upleft,player)
    elif downright:
        screen.blit(char_downright,player)
        screen.blit(gun_downright,player)
    elif downleft:
        screen.blit(char_downleft,player)
        screen.blit(gun_downleft,player)
    else:
        screen.blit(char_tank,player)
        screen.blit(char_gun,player)

    #updates player position
    pygame.display.flip()

update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_w:
                up = True
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_s:
                down = True
            if event.key == pygame.K_d:
                right = True
            if event.key == pygame.K_SPACE:
                shoot = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                up = False
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_s:
                down = False
            if event.key == pygame.K_d:
                right = False
            if event.key == pygame.K_SPACE:
                shoot = False

    for rect in obstacle_list:
        if player.colliderect(rect):
            if up and rect.collidepoint((player.centerx,player.top)):
                up = False
            if left and rect.collidepoint((player.left,player.centery)):
                left = False
            if down and rect.collidepoint((player.centerx,player.bottom)):
                down = False
            if right and rect.collidepoint((player.right,player.centery)):
                right = False

    for rect in obstacle_list:
        if shootupright:
            if rect.collidepoint(shoot_upright_rect.center):
                cb_collideupright = True
                shootupright = False
        if shootup:
            if rect.collidepoint(shoot_up_rect.center):
                cb_collideup = True
                shootup = False
        if shootupleft:
            if rect.collidepoint(shoot_upleft_rect.center):
                cb_collideupleft = True
                shootupleft = False
        if shootright:
            if rect.collidepoint(shoot_right_rect.center):
                cb_collideright = True
                shootright = False
        if shootdownright:
            if rect.collidepoint(shoot_downright_rect.center):
                cb_collidedownright = True
                shootdownright = False
        if shootdown:
            if rect.collidepoint(shoot_down_rect.center):
                cb_collidedown = True
                shootdown = False
        if shootdownleft:
            if rect.collidepoint(shoot_downleft_rect.center):
                cb_collidedownleft = True
                shootdownleft = False
        if shootleft:
            if rect.collidepoint(shoot_left_rect.center):
                cb_collideleft = True
                shootleft = False

    if up:
        if player.top > window.top:
            player = player.move(0,-speed)

    if up and not (left or right):
        if player.top > window.top:
            upface = True
            downface = False
            rightface = False
            leftface = False
            downright = False
            downleft = False
            upright = False
            upleft = False

    if up and left:
        upleft = True
        downface = False
        leftface = False
        rightface = False
        upface = False
        upright = False
        downleft = False
        downright = False

    if up and right:
        upright = True
        downface = False
        leftface = False
        rightface = False
        upface = False
        upleft = False
        downleft = False
        downright = False
            
    if left:
        if player.left > window.left:
            player = player.move(-speed,0)

    if left and not(up or down):
        if player.left > window.left:
            leftface = True
            rightface = False
            downface = False
            upface = False
            downright = False
            downleft = False
            upright = False
            upleft = False

    if down:
        if player.bottom < window.bottom:
            player = player.move(0,speed)

    if down and not (left or right):
        if player.bottom < window.bottom:
            downface = True
            rightface = False
            leftface = False
            upface = False
            downright = False
            downleft = False
            upright = False
            upleft = False

    if down and left:
        downleft = True
        downface = False
        leftface = False
        rightface = False
        upface = False
        upleft = False
        upright = False
        downright = False

    if down and right:
        downright = True
        downface = False
        leftface = False
        rightface = False
        upface = False
        upleft = False
        upright = False
        downleft = False
            
    if right:
        if player.right < window.right:
            player = player.move(speed,0)

    if right and not (down or up):
        if player.right < window.right:
            rightface = True
            leftface = False
            downface = False
            upface = False
            downright = False
            downleft = False
            upright = False
            upleft = False

    if shoot and upright and not shooting:
        shoot_upright_rect = shoot_upright.get_rect(center = (player.right, player.top + 25))
        screen.blit(shoot_upright,shoot_upright_rect)
        shooting = True
        shootupright = True

    if shoot and upface and not shooting:
        shoot_up_rect = player_bullet.get_rect(center = (player.centerx,player.top))
        screen.blit(player_bullet,shoot_up_rect)
        shooting = True
        shootup = True

    if shoot and upleft and not shooting:
        shoot_upleft_rect = shoot_upleft.get_rect(center = (player.left + 25, player.top + 25))
        screen.blit(shoot_upleft,shoot_upleft_rect)
        shooting = True
        shootupleft = True

    if shoot and rightface and not shooting:
        shoot_right_rect = shoot_right.get_rect(center = (player.right,player.centery))
        screen.blit(shoot_right,shoot_right_rect)
        shooting = True
        shootright = True

    if shoot and downright and not shooting:
        shoot_downright_rect = shoot_downright.get_rect(center = player.bottomright)
        screen.blit(shoot_downright,shoot_downright_rect)
        shooting = True
        shootdownright = True

    if shoot and downface and not shooting:
        shoot_down_rect = shoot_down.get_rect(center = (player.centerx,player.bottom))
        screen.blit(shoot_down,shoot_down_rect)
        shooting = True
        shootdown = True

    if shoot and downleft and not shooting:
        shoot_downleft_rect = shoot_downleft.get_rect(center = (player.left + 25, player.bottom))
        screen.blit(shoot_downleft,shoot_downleft_rect)
        shooting = True
        shootdownleft = True

    if shoot and leftface and not shooting:
        shoot_left_rect = shoot_left.get_rect(center = (player.left,player.centery))
        screen.blit(shoot_left, shoot_left_rect)
        shooting = True
        shootleft = True

    if shooting:
        cooldown += 1
        if cooldown == 50:
            cooldown = 0
            shooting = False

    if shootupright:
        shoot_upright_rect = shoot_upright_rect.move(10,-10)
    if shootup:
        shoot_up_rect = shoot_up_rect.move(0,-10)
    if shootupleft:
        shoot_upleft_rect = shoot_upleft_rect.move(-10,-10)
    if shootright:
        shoot_right_rect = shoot_right_rect.move(10,0)
    if shootdownright:
        shoot_downright_rect = shoot_downright_rect.move(10,10)
    if shootdown:
        shoot_down_rect = shoot_down_rect.move(0,10)
    if shootdownleft:
        shoot_downleft_rect = shoot_downleft_rect.move(-10,10)
    if shootleft:
        shoot_left_rect = shoot_left_rect.move(-10,0)

    update()
    
    if cb_collideup:
        screen.blit(bulletimpact,shoot_up_rect)
        cb_collideup = False
    if cb_collideupright:
        screen.blit(bulletimpact,shoot_upright_rect)
        cb_collideupright = False
    if cb_collideright:
        screen.blit(bulletimpact,shoot_right_rect)
        cb_collideright = False
    if cb_collidedownright:
        screen.blit(bulletimpact,shoot_downright_rect)
        cb_collidedownright = False
    if cb_collidedown:
        screen.blit(bulletimpact,shoot_down_rect)
        cb_collidedown = False
    if cb_collidedownleft:
        screen.blit(bulletimpact,shoot_downleft_rect)
        cb_collidedownleft = False
    if cb_collideleft:
        screen.blit(bulletimpact,shoot_left_rect)
        cb_collideleft = False
    if cb_collideupleft:
        screen.blit(bulletimpact,shoot_upleft_rect)
        cb_collideupleft = False
    pygame.display.flip()

    clock.tick(30)
