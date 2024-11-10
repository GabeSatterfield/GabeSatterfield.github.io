import pygame
import sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

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
                shot = TrapShot(self.rect.centerx, self.rect.centery, direction)
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
        self.shots.empty()

# Trap Shot Class
class TrapShot(pygame.sprite.Sprite):
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
        if not screen.get_rect().contains(self.rect):
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
            self.image.fill(WHITE)

    def disable(self):
        self.is_active = False

# Groups
gun_traps = pygame.sprite.Group()
laser = Laser(200)
laser_group = pygame.sprite.GroupSingle(laser)

# Gun Trap positions and shooting directions
directions_list = [
    [(1, 0)],  # Right
    [(0, 1)],  # Down
    [(0, -1)],  # Up
    [(1, 1), (-1, -1)],  # Diagonal
    [(1, 0), (0, 1)],  # Right and Down
    [(-1, 0), (0, -1)],  # Left and Up
    [(1, 1), (-1, 0)]  # Diagonal and Left
]

positions = [(300, 100), (400, 200), (500, 100), (600, 200), (700, 300), (600, 400), (300, 400)]

# Add Gun Traps with specific shooting directions
for pos, directions in zip(positions, directions_list):
    gun_traps.add(GunTrap(*pos, directions))

# All-directions Gun Trap
all_directions = [(1, 0), (0, 1), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
all_directions_trap = GunTrap(500, 500, all_directions)
gun_traps.add(all_directions_trap)

# Main Loop
while True:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update
    gun_traps.update()
    laser_group.update()

    # Draw
    for trap in gun_traps:
        if trap.is_active:
            screen.blit(trap.image, trap.rect)
        trap.shots.draw(screen)
    if laser.is_active:
        screen.blit(laser.image, laser.rect)
    # Always draw the blue base
    pygame.draw.rect(screen, BLUE, laser.base)

    pygame.display.flip()
    clock.tick(30)
