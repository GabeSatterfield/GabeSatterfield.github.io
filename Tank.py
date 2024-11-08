import pygame

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Gun Trap Class
class GunTrap(pygame.sprite.Sprite):
    def __init__(self, x, y, directions):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(x, y))
        self.directions = directions
        self.shots = pygame.sprite.Group()
        self.is_active = True
        self.shoot_delay = 30
        self.shoot_timer = 0

    def shoot(self):
        if self.is_active:
            for direction in self.directions:
                shot = TankShot(self.rect.centerx, self.rect.centery, direction)
                self.shots.add(shot)

    def update(self):
        if self.is_active:
            self.shoot_timer += 1
            if self.shoot_timer >= self.shoot_delay:
                self.shoot()
                self.shoot_timer = 0
            self.shots.update()

    def disable(self):
        self.is_active = False
        self.shots.empty()  # Remove all shots when disabled

# Gun Trap Shot Class
class TankShot(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 7

    def update(self):
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed
        if not pygame.display.get_surface().get_rect().contains(self.rect):
            self.kill()

# Laser Class
class Laser(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.Surface((10, 600))
        self.image.fill(RED)
        self.rect = self.image.get_rect(midleft=(x, 0))
        self.is_active = True
        self.base = pygame.Rect(x - 5, 0, 10, 20)  # Blue base at the top of the laser

    def update(self):
        if not self.is_active:
            self.image.fill((255, 255, 255))  # Make the laser disappear when not active

    def disable(self):
        self.is_active = False

# Create 7 Gun Traps with different directions
directions_list = [
    [(1, 0)],          # Right (Shoots right)
    [(0, 1)],          # Down (Shoots down)
    [(0, -1)],         # Up (Shoots up)
    [(1, 1), (-1, -1)], # Diagonal (Shoots diagonally down-right and up-left)
    [(1, 0), (0, 1)],  # Right, Down (Shoots right and down)
    [(-1, 0), (0, -1)], # Left, Up (Shoots left and up)
    [(1, 1), (-1, 0)]  # Diagonal and Left (Shoots diagonally down-right and left)
]

positions = [(300, 100), (400, 200), (500, 100), (600, 200), (700, 300), (600, 400), (300, 400)]

# Add GunTraps with specific shooting directions
gun_traps = pygame.sprite.Group()
for pos, directions in zip(positions, directions_list):
    gun_traps.add(GunTrap(*pos, directions))  # Regular GunTraps

# Add a new Gun Trap that shoots in all directions
all_directions = [
    (1, 0),   # Right (Shoots right)
    (0, 1),   # Down (Shoots down)
    (0, -1),  # Up (Shoots up)
    (-1, 0),  # Left (Shoots left)
    (1, 1),   # Diagonal down-right (Shoots diagonally down-right)
    (1, -1),  # Diagonal up-right (Shoots diagonally up-right)
    (-1, -1), # Diagonal up-left (Shoots diagonally up-left)
    (-1, 1)   # Diagonal down-left (Shoots diagonally down-left)
]

# Positioning the new trap
all_directions_trap = GunTrap(500, 500, all_directions)
gun_traps.add(all_directions_trap)  # GunTrap shooting in all directions

# Create a Laser object
laser = Laser(200)  # Laser on the left side of the screen

# Update function for traps (to be used in the game loop)
def update_traps():
    gun_traps.update()
    laser.update()

def draw_traps(screen):
    gun_traps.draw(screen)
    for trap in gun_traps:
        trap.shots.draw(screen)
    if laser.is_active:
        screen.blit(laser.image, laser.rect)
    # Always draw the blue base for laser
    pygame.draw.rect(screen, BLUE, laser.base)
