import pygame
import random
from sys import exit

# function to change and display score during gameplay
def scores():
    global score
    # collision
    #if player_rect.colliderect(barrel_rect):
    #    score -= 50
    if player_rect.colliderect(duck_rect):
        score -= 1
    if player_rect.colliderect(energy_rect):
        energy_rect.bottom = -500
        energy_rect.x = random.randint(25, 417)
        score += 100
    score -= 1
    # HETKEL LOEB SKOORI VEEL VANAMOODI e MITTE AJA JÄRGI
    score_surface = font.render(f"Fishies: {score}", True, "#111111").convert_alpha()
    score_rect = score_surface.get_rect(center = (216,50))
    screen.blit(score_surface, score_rect)

def player_animation():
    global player_surface, player_index
    player_index += 0.06
    if player_index >= len(player_anim):
        player_index = 0
    player_surface = player_anim[int(player_index)]

# pygame initialisation and display config (size, used fonts)
pygame.init()
screen = pygame.display.set_mode((432,768)) # 9:16
pygame.display.set_caption("Swimming with the Fishies")
clock = pygame.time.Clock()
font = pygame.font.Font("fonts/RobotoMono-Semibold.ttf", 50)

# background surface
bg_surface = pygame.image.load("graphics/background.png").convert_alpha()

# arguments
score = 10000
speed = 5

# barrel surface / spawn location
barrel_surface = pygame.image.load("graphics/barrel.png").convert_alpha()
barrel_rect = barrel_surface.get_rect(center = (random.randint(32,400), random.randint(-500,-200)))

# duck surface / spawn location
duck_surface = pygame.image.load("graphics/duck.png").convert_alpha()
duck_rect = duck_surface.get_rect(center = (random.randint(25,417), random.randint(-1000,-500)))

# energy surface / spawn location
energy_surface = pygame.image.load("graphics/energy.png").convert_alpha()
energy_rect = duck_surface.get_rect(center = (random.randint(25,417), random.randint(-1500,-500)))

# player surface / spawn location
player_surface_1 = pygame.image.load("graphics/player_1.png").convert_alpha()
player_surface_2 = pygame.image.load("graphics/player_2.png").convert_alpha()
player_anim = [player_surface_1,player_surface_2]
player_index = 0
player_surface = player_anim[player_index]
player_rect = player_surface.get_rect(center = (216,384))

# rotations
player_surface_up = player_surface
player_surface_down = pygame.transform.rotate(player_surface, 180)
player_surface_left = pygame.transform.rotate(player_surface, 10)
player_surface_right = pygame.transform.rotate(player_surface, 350)

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
                score = 10000
                barrel_rect = barrel_surface.get_rect(center = (random.randint(32,400), random.randint(-500,-200)))
                duck_rect = duck_surface.get_rect(center = (random.randint(25,417), random.randint(-1000,-500)))
                player_rect = player_surface.get_rect(center = (216,284))

    if game:
        # player movement
        player_speed = 2 * speed
        if player_rect.colliderect(duck_rect):
            player_speed *= 0.5
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            player_speed = speed
        if keys[pygame.K_UP]:
            player_rect.y -= player_speed
            player_surface = player_surface_up
        if keys[pygame.K_DOWN]:
            player_rect.y += player_speed * 0.5
            player_surface = player_surface_down
        if keys[pygame.K_LEFT]:
            player_rect.x -= player_speed * 0.8
            player_surface = player_surface_left
        if keys[pygame.K_RIGHT]:
            player_rect.x += player_speed * 0.8
            player_surface = player_surface_right

        # background & text/score function
        screen.blit(bg_surface,(0,0))
        scores()

        player_animation()

        # barrel positioning
        barrel_rect.y += speed
        if barrel_rect.top >= 768:
            barrel_rect.bottom = random.randint(-250,-200)
            barrel_rect.x = random.randint(32, 400)

        # duck positioning
        duck_rect.y += speed
        if duck_rect.top >= 768:
            duck_rect.bottom = random.randint(-400,-350)
            duck_rect.x = random.randint(25, 417)

        # energy positioning
        energy_rect.y += speed * 0.9
        if energy_rect.top >= 768:
            energy_rect.bottom = -500
            energy_rect.x = random.randint(25, 417)

        # collision
        if player_rect.colliderect(barrel_rect):
            player_rect.top = barrel_rect.bottom
        
        # player positioning
        if player_rect.right <= 50:
            player_rect.right = 50
        if player_rect.left >= 382:
            player_rect.left = 382
        if player_rect.top >= 768:
            game = False
        if player_rect.bottom <= 130:
            player_rect.bottom = 130

        # barrel & player blit
        screen.blit(barrel_surface,barrel_rect)
        screen.blit(duck_surface,duck_rect)
        screen.blit(energy_surface,energy_rect)
        screen.blit(player_surface,player_rect)

        # game over
        if score <= 0:
            game = False

    else:
        screen.fill("#111111")

    # internal clock
    pygame.display.update()
    clock.tick(60)
