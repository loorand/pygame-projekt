import pygame
import random
from sys import exit

# pygame initialisation and display config (size, used fonts)
pygame.init()
screen = pygame.display.set_mode((432,768)) # 9:16
pygame.display.set_caption("Swimming with the Fishies")
clock = pygame.time.Clock()
font = pygame.font.Font("fonts/RobotoMono-Semibold.ttf", 50)

# function to change and display score during gameplay
def scores():
    global score
    global energy_collect
    # collision
    if Player.rect.colliderect(Duck.rect):
        score -= 1
    if Player.rect.colliderect(Energy.rect):
        Energy.rect.bottom = random.randint(-280,-220)
        Energy.rect.x = random.randint(25, 417)
        energy_collect += 1
        score += 100
    score -= 1
    # HETKEL LOEB SKOORI VEEL VANAMOODI e MITTE AJA JÄRGI
    score_surface = font.render(f"Energy: {score}", True, "#111111").convert_alpha()
    score_rect = score_surface.get_rect(center = (216,50))
    screen.blit(score_surface, score_rect)

# background surface
bg_surface = pygame.image.load("graphics/background.png").convert_alpha()

# starting arguments
score = 1000
speed = 5

barrel = pygame.image.load("graphics/barrel.png").convert_alpha()
duck = pygame.image.load("graphics/duck.png").convert_alpha()
energy = pygame.image.load("graphics/energy.png").convert_alpha()

class Barrel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = barrel
        self.rect = self.image.get_rect(center = (x, y))

class Duck(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = duck
        self.rect = self.image.get_rect(center = (x, y))

class Energy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = energy
        self.rect = self.image.get_rect(center = (x, y))

""" surface / spawn location
# barrel (obstacle) surface / spawn location
barrel_surface = pygame.image.load("graphics/barrel.png").convert_alpha()
barrel_rect = barrel_surface.get_rect(center = (random.randint(32,400), random.randint(-500,-200)))
# duck (slowdown) surface / spawn location
duck_surface = pygame.image.load("graphics/duck.png").convert_alpha()
duck_rect = duck_surface.get_rect(center = (random.randint(25,417), random.randint(-1000,-500)))
# energy (points) surface / spawn location
energy_surface = pygame.image.load("graphics/energy.png").convert_alpha()
energy_rect = duck_surface.get_rect(center = (random.randint(25,417), random.randint(-1500,-500)))
 """

player1 = pygame.image.load("graphics/player_1.png").convert_alpha()
player2 = pygame.image.load("graphics/player_2.png").convert_alpha()

# player surface / spawn location
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image1 = player1
        self.image2 = player2
        self.rect = self.image1.get_rect(center = (x, y))
        self.anim = [self.image1, self.image2]
        self.index = 0
        self.surface = self.anim[self.index]

    def animate():
        Player.index += 0.06
        if Player.index >= len(Player.anim):
            Player.index = 0
        player_surface = Player.anim[int(Player.index)]

stuff = pygame.sprite.Group(Barrel(random.randint(32,400), random.randint(-500,-200)),
                            Duck(random.randint(25,417), random.randint(-1000,-500)),
                            Energy(random.randint(25,417), random.randint(-1500,-500)),
                            Player(216,384))


""" player_surface_1 = pygame.image.load("graphics/player_1.png").convert_alpha()
player_surface_2 = pygame.image.load("graphics/player_2.png").convert_alpha()
player_anim = [player_surface_1, player_surface_2]
player_index = 0
player_surface = player_anim[player_index]
player_rect = player_surface.get_rect(center = (216,384)) """

game = True
# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # game restart screen (S to restart)
        if not game:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                game = True
                score = 1000
                speed = 5
                energy_collect = 0

    if game:
        # player movement
        player_speed = 2.1 * speed
        if Player.rect.colliderect(Duck.rect()):
            player_speed *= 0.44
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            player_speed = speed
        if keys[pygame.K_UP]:
            Player.rect.y -= player_speed
        if keys[pygame.K_DOWN]:
            Player.rect.y += player_speed * 0.56
        if keys[pygame.K_LEFT]:
            Player.rect.x -= player_speed * 0.8
        if keys[pygame.K_RIGHT]:
            Player.rect.x += player_speed * 0.8

        # background & text/score function
        screen.blit(bg_surface,(0,0))
        scores()

        Player.animate()

        # barrel positioning
        Barrel.rect.y += speed
        if Barrel.rect.top >= 768:
            Barrel.rect.bottom = random.randint(-250,-200)
            Barrel.rect.x = random.randint(32, 400)

        # duck positioning
        Duck.rect.y += speed
        if Duck.rect.top >= 768:
            Duck.rect.bottom = random.randint(-400,-350)
            Duck.rect.x = random.randint(25, 417)

        # energy positioning
        Energy.rect.y += speed * 0.9
        if Energy.rect.top >= 768:
            Energy.rect.bottom = -500
            Energy.rect.x = random.randint(25, 417)

        # collision
        if Player.rect.colliderect(Barrel.rect):
            Player.rect.top = Barrel.rect.bottom
        
        # player positioning
        if Player.rect.right <= 50:
            Player.rect.right = 50
        if Player.rect.left >= 382:
            Player.rect.left = 382
        if Player.rect.top >= 768:
            game = False
        if Player.rect.bottom <= 130:
            Player.rect.bottom = 130

        # barrel & player blit
        stuff.blit(screen)
        """ screen.blit(Barrel.surface,Barrel.rect)
        screen.blit(Duck.surface,Duck.rect)
        screen.blit(Energy.surface,Energy.rect)
        screen.blit(Player.surface,Player.rect) """

        # game over
        if score <= 0:
            game = False

    else:
        screen.fill("#111111")

    # internal clock
    pygame.display.update()
    clock.tick(60)
