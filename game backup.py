import pygame, random
from sys import exit

# function to change and display score during gameplay
def scores():
    global score
    global energy_collect
    # collision
    if player_rect.colliderect(duck_rect):
        score -= 1
        player_rect.y += 4
    #if player_rect.top < 
    if player_rect.colliderect(energy_rect):
        energy_rect.bottom = random.randint(-280,-220)
        energy_rect.x = random.randint(25, 417)
        energy_collect += 1
        score += 100

    score -= 1

    # HETKEL LOEB SKOORI VEEL VANAMOODI e MITTE AJA JÄRGI
    score_surface = font.render(f"Energy: {int(score)}", True, "#111111").convert_alpha()
    score_rect = score_surface.get_rect(center = (216,50))
    screen.blit(score_surface, score_rect)

    energy_col_surface = font.render(f"Collection: {energy_collect}", True, "#111111").convert_alpha()
    energy_col_rect = energy_col_surface.get_rect(center = (216,100))
    screen.blit(energy_col_surface, energy_col_rect)

def player_animation():
    global player_surface, player_index
    player_index += 0.06
    if player_index >= len(player_anim):
        player_index = 0
    player_surface = player_anim[int(player_index)]

    keys = pygame.key.get_pressed()
    """ if keys[pygame.K_UP]:
        player_surface = player_surface_up """
    """ if keys[pygame.K_DOWN]:
        player_surface = player_surface_down """
    if keys[pygame.K_LEFT]:
        player_surface = player_surface_left
    if keys[pygame.K_RIGHT]:
        player_surface = player_surface_right

# pygame initialisation and display config (size, used fonts)
pygame.init()
screen = pygame.display.set_mode((432,768)) # 9:16
pygame.display.set_caption("Moving About")
clock = pygame.time.Clock()
font = pygame.font.Font("fonts/RobotoMono-Semibold.ttf", 50)
font_small = pygame.font.Font("fonts/RobotoMono-Semibold.ttf", 20)

# background surface
bg_surface = pygame.image.load("graphics/background.png").convert_alpha()

# starting arguments
score = 1000
speed = 7
energy_collect = 0
gravity = 0

# barrel (obstacle) surface / spawn location
barrel_surface = pygame.image.load("graphics/barrel.png").convert_alpha()
barrel_surface.set_alpha(200)
barrel_rect = barrel_surface.get_rect(center = (random.randint(32,400), random.randint(-20,-10) * 10))

# duck (slowdown) surface / spawn location
duck_surface = pygame.image.load("graphics/duck.png").convert_alpha()
duck_surface.set_alpha(200)
duck_rect = duck_surface.get_rect(center = (random.randint(25,407), random.randint(-40,-20) * 10))

# energy (points) surface / spawn location
energy_surface = pygame.image.load("graphics/energy.png").convert_alpha()
energy_surface.set_alpha(200)
energy_rect = duck_surface.get_rect(center = (random.randint(25,407), random.randint(-30,-15) * 10))

# player surface / spawn location
player_surface_1 = pygame.image.load("graphics/player_1.png").convert_alpha()
player_surface_2 = pygame.image.load("graphics/player_2.png").convert_alpha()
player_anim = [player_surface_1,player_surface_2]
player_index = 0
player_surface = player_anim[player_index]
player_rect = player_surface.get_rect(center = (216,250))

# rotations
player_surface_up = player_surface
""" player_surface_down = pygame.transform.rotate(player_surface, 180) """
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
                score = 1000
                speed = 5
                energy_collect = 0
                gravity = 0
                barrel_rect = barrel_surface.get_rect(center = (random.randint(32, 400), random.randint(-20, -10) * 10))
                duck_rect = duck_surface.get_rect(center = (random.randint(25, 417), random.randint(-40, -20) * 10))
                energy_rect = duck_surface.get_rect(center = (random.randint(25, 417), random.randint(-30, -15) * 10))
                player_rect = player_surface.get_rect(center = (216,250))

    if game:
        # player movement
        player_speed = 9
        """ player_rect.y += 2 """
        if player_rect.colliderect(duck_rect):
            player_speed *= 0.3
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            player_speed = speed
        """ if keys[pygame.K_UP]:
            player_rect.y -= player_speed """
        """ if keys[pygame.K_DOWN]:
            player_rect.y += player_speed * 0.56 """
        if keys[pygame.K_LEFT]:
            player_rect.x -= player_speed * 0.7
        if keys[pygame.K_RIGHT]:
            player_rect.x += player_speed * 0.7
        if event.type == pygame.KEYDOWN and gravity >= 2:
            if event.key == pygame.K_UP:
                gravity = -9

        # levelling up
        speed = 7 + energy_collect / 16
        """ if energy_collect >= 10:
            speed = 6
        if energy_collect >= 20:
            speed = 7
        if energy_collect >= 30:
            speed = 8
        if energy_collect >= 40:
            speed = 9
        if energy_collect >= 50:
            speed = 10
        if energy_collect >= 60:
            speed = 12
        if energy_collect >= 70:
            speed = 13
        if energy_collect >= 80:
            speed = 14
        if energy_collect >= 90:
            speed = 15 """
            
        # background & text/score function
        screen.blit(bg_surface,(0,0))
        scores()

        # ... player animation ...
        player_animation()

        # imitating moon gravity
        gravity += .5
        player_rect.y += gravity

        # barrel positioning
        barrel_rect.y += speed
        if barrel_rect.top >= screen.get_height():
            barrel_rect.bottom = random.randint(-20, -10) * 10
            barrel_rect.x = random.randint(barrel_surface.get_width() // 2, screen.get_width() - barrel_surface.get_width() // 2)
            barrel_rect.y += random.randint(-1, 1) # this nudges object falling speed slightly up/down
            
        # duck positioning
        duck_rect.y += speed
        if duck_rect.top >= screen.get_height():
            duck_rect.bottom = random.randint(-40, -20) * 10
            duck_rect.x = random.randint(duck_surface.get_width() // 2, screen.get_width() - duck_surface.get_width() // 2)
            duck_rect.y += random.randint(-1, 1)

        # energy positioning
        energy_rect.y += speed * 0.9
        if energy_rect.top >= screen.get_height():
            energy_rect.bottom = random.randint(-30, -15) * 10
            energy_rect.x = random.randint(energy_surface.get_width() // 2, screen.get_width() - energy_surface.get_width() // 2)
            energy_rect.y += random.randint(-1, 1)

        # collision ver 1
        """ if player_rect.bottom >= barrel_rect.top and gravity > 0 and barrel_rect.left < player_rect.centerx < barrel_rect.right and not barrel_rect.top < player_rect.top:
            player_rect.bottom = barrel_rect.top
            gravity = -16 """
        
        # collision ver 2
        if event.type == pygame.KEYDOWN and player_rect.colliderect(barrel_rect):
            if event.key == pygame.K_UP and gravity < 0:
                gravity = -13

        # player is boxed in
        if player_rect.right <= 50:
            player_rect.right = 50
        if player_rect.left >= 382:
            player_rect.left = 382
        if player_rect.top >= 768:
            game = False
        if player_rect.bottom <= 84:
            player_rect.bottom = 84

        # blitskrieg
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
