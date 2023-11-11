import pygame
import random
from sys import exit

# function to change and display score during gameplay
def scores():
    global score
    # collision
    if player_rect.colliderect(square_rect):
        score -= 50
    if player_rect.colliderect(heal_rect):
        score += 5
    score_surface = font.render(f"Hea mäng {score}", True, "#111111").convert_alpha()
    score_rect = score_surface.get_rect(center = (500,69))
    screen.blit(score_surface, score_rect)

# pygame initialisation and display config (size, used fonts)
pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Fly Game")
clock = pygame.time.Clock()
font = pygame.font.Font("fonts/RobotoMono-Semibold.ttf", 50)

# background surface
bg_surface = pygame.image.load("graphics/background.png").convert_alpha()

score = 1000

# square surface / spawn location
square_surface = pygame.image.load("graphics/square.png").convert_alpha()
square_rect = square_surface.get_rect(midleft = (random.randint(0, 1000), random.randint(25, 975)))

# healer surface / spawn location
heal_surface = pygame.image.load("graphics/heal.png").convert_alpha()
heal_rect = heal_surface.get_rect(midleft = (random.randint(1000, 5000), random.randint(25, 975)))

# player surface / spawn location
player_surface = pygame.image.load("graphics/player.png").convert_alpha()
player_rect = player_surface.get_rect(center = (500,500))

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
                square_rect = square_surface.get_rect(midleft = (random.randint(0, 1000), random.randint(25, 975)))
                heal_rect = heal_surface.get_rect(midleft = (random.randint(1000, 5000), random.randint(25, 975)))
                player_rect = player_surface.get_rect(center = (500,500))

    if game:
        # player movement
        player_speed = 12
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            player_speed = 6
        if keys[pygame.K_UP]:
            player_rect.y -= player_speed
        if keys[pygame.K_DOWN]:
            player_rect.y += player_speed
        if keys[pygame.K_LEFT]:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_rect.x += player_speed

        # background & text/score function
        screen.blit(bg_surface,(0,0))
        scores()
        
        # square positioning
        square_rect.x -= 5
        if square_rect.right <= 0:
            square_rect.left = 1000
            square_rect.y = random.randint(25, 975)

        # heal positioning
        heal_rect.x -= 5
        if heal_rect.right <= -2000:
            heal_rect.left = 1000
            heal_rect.y = random.randint(25, 975)

        # collision
        #if player_rect.colliderect(square_rect):
        #    player_rect.right = square_rect.left
        
        # player positioning
        if player_rect.right <= 20:
            player_rect.right = 20
        if player_rect.left >= 980:
            player_rect.left = 980
        if player_rect.top >= 980:
            player_rect.top = 980
        if player_rect.bottom <= 20:
            player_rect.bottom = 20

        # square & player blit
        screen.blit(square_surface,square_rect)
        screen.blit(heal_surface,heal_rect)
        screen.blit(player_surface,player_rect)

        # game over
        if score <= 0:
            game = False

    else:
        screen.fill("#111111")

    # internal clock
    pygame.display.update()
    clock.tick(60)
