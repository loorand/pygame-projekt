import pygame, random, pickle
from sys import exit

# function to change and display score during gameplay
def scores():
    global score
    global energy_collect
    global gravity
    if player_rect.colliderect(duck_rect):
        score -= 1
        player_rect.y += 5
    if player_rect.top <= 0:
        player_rect.top = 0
        score -= 50
        gravity = -gravity
    if player_rect.colliderect(energy_rect):
        energy_rect.bottom = random.randint(-280,-220)
        energy_rect.x = random.randint(25, 417)
        energy_collect += 1
        score += 100

    score -= 1

    y = 0
    if player_rect.top < 100:
        y = player_rect.top - 100 - (80 - player_rect.top) * .5

    score_surface = font.render(f"Stamina: {(score // 10)}", True, "#bbbbbb").convert_alpha()
    score_rect = score_surface.get_rect(center = (216, y + 30))
    screen.blit(score_surface, score_rect)
    energy_col_surface = font.render(f"Purples: {energy_collect}", True, "#bbbbbb").convert_alpha()
    energy_col_rect = energy_col_surface.get_rect(center = (216, y + 70))
    screen.blit(energy_col_surface, energy_col_rect)

    score2_surface = font.render(f"Stamina: {(score // 10)}", True, "#bbbbbb").convert_alpha()
    score2_rect = score2_surface.get_rect(center = (216, y + 30 + screen.get_height()))
    screen.blit(score2_surface, score2_rect)
    energy2_col_surface = font.render(f"Purples: {energy_collect}", True, "#bbbbbb").convert_alpha()
    energy2_col_rect = energy2_col_surface.get_rect(center = (216, y + 70 + screen.get_height()))
    screen.blit(energy2_col_surface, energy2_col_rect)

def player_animation():
    global player_surface, player_index
    player_index += 0.06
    if player_index >= len(player_anim):
        player_index = 0
    player_surface = player_anim[int(player_index)]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_surface = player_surface_left
    if keys[pygame.K_RIGHT]:
        player_surface = player_surface_right

def draw_text(text, font, color, screen, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (screen_x // 2, y)
    screen.blit(textobj, textrect)

def menu_music():
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.music.load("audio/horology.mp3")
    pygame.mixer.music.set_volume(.7)
    pygame.mixer.music.play(-1, 0, 150)

def game_music():
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.music.load("audio/deserted_dunes_welcome_weary_feet.mp3")
    pygame.mixer.music.set_volume(.7)
    pygame.mixer.music.play(-1, 0, 50)

# pygame initialisation and display config (size, used fonts)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((432, 768)) # 9:16
screen_x = screen.get_width()
pygame.display.set_caption("Moving About")
clock = pygame.time.Clock()
font = pygame.font.Font("fonts/RobotoMono-Semibold.ttf", 36)

# background surface
bg_surface = pygame.image.load("graphics/background.png").convert_alpha()
bg_rect = bg_surface.get_rect(topleft = (0, 0))
bg1_surface = pygame.image.load("graphics/background.png").convert_alpha()
bg1_rect = bg_surface.get_rect(bottomleft = (0, 0))

# starting arguments
score = 1000
with open("highscore.db", "r") as file:
    highscore = int(file.read())
    dif = 0
    file.close()
speed = 7
energy_collect = 0
gravity = 0
volume = 1

# barrel surface / spawn location
barrel_surface = pygame.image.load("graphics/barrel.png").convert_alpha()
barrel_surface.set_alpha(200)
barrel_x = barrel_surface.get_width() // 2
barrel_rect = barrel_surface.get_rect(center = (random.randint(barrel_x, screen_x - barrel_x), random.randint(-20,-10) * 10))
# duck surface / spawn location
duck_surface = pygame.image.load("graphics/duck.png").convert_alpha()
duck_surface.set_alpha(200)
duck_x = duck_surface.get_width() // 2
duck_rect = duck_surface.get_rect(center = (random.randint(duck_x, screen_x - duck_x), random.randint(-40,-20) * 10))
# energy surface / spawn location
energy_surface = pygame.image.load("graphics/energy.png").convert_alpha()
energy_surface.set_alpha(200)
energy_x = energy_surface.get_width() // 2
energy_rect = duck_surface.get_rect(center = (random.randint(energy_x, screen_x - energy_x), random.randint(-30,-15) * 10))
# player surface / spawn location / animation
player_surface_1 = pygame.image.load("graphics/player_1.png").convert_alpha()
player_surface_2 = pygame.image.load("graphics/player_2.png").convert_alpha()
player_anim = [player_surface_1,player_surface_2]
player_index = 0
player_surface = player_anim[player_index]
player_rect = player_surface.get_rect(center = (216,250))

# rotations
player_surface_up = player_surface
player_surface_left = pygame.transform.rotate(player_surface, 10)
player_surface_right = pygame.transform.rotate(player_surface_2, 350)

game = False
sound = "MUTE"
menu_music()
# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("highscore.db", "r+") as file:
                if int(file.read()) < (highscore + dif):
                    file.seek(0)
                    file.write(str(highscore - dif))
                    file.truncate()
                file.close()
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            print("test")
            if volume == 1:
                volume = 0
                pygame.mixer.music.set_volume(0)
                sound = "SOUND"
            else:
                volume = 1
                pygame.mixer.music.set_volume(.7)
                sound = "MUTE"

        # game restart screen (S to restart)
        if not game:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game = True
                game_music()
                score = 1000
                speed = 5
                energy_collect = 0
                gravity = 0
                barrel_rect = barrel_surface.get_rect(center = (random.randint(barrel_x, screen_x - barrel_x), random.randint(-20,-10) * 10))
                duck_rect = duck_surface.get_rect(center = (random.randint(duck_x, screen_x - duck_x), random.randint(-40,-20) * 10))
                energy_rect = duck_surface.get_rect(center = (random.randint(energy_x, screen_x - energy_x), random.randint(-30,-15) * 10))
                player_rect = player_surface.get_rect(center = (216,250))

    if game:
        jump = pygame.mixer.Sound("audio/jump.mp3")
        jump.set_volume(.7)
        # player movement
        player_speed = 9
        if player_rect.colliderect(duck_rect):
            player_speed *= 0.3
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= player_speed * 0.6
        if keys[pygame.K_RIGHT]:
            player_rect.x += player_speed * 0.6
        if event.type == pygame.KEYDOWN and gravity >= 2:
            if event.key == pygame.K_UP:
                gravity = -9
                pygame.mixer.Sound.play(jump)

        # game maker-harder
        speed = 7 + energy_collect / 8
        # magic
        screen.blit(bg_surface, bg_rect)
        screen.blit(bg1_surface, bg1_rect)
        scores()
        player_animation()

        # imitating some sort of gravity
        gravity += .5
        player_rect.y += gravity
        # background positioning
        bg_rect.y += speed / 14 + 0.3 / speed
        if bg_rect.top >= screen.get_height():
            bg_rect.bottom = 0
        bg1_rect.y += speed / 14 + 0.3 / speed
        if bg1_rect.top >= screen.get_height():
            bg1_rect.bottom = 0
        # barrel positioning
        barrel_rect.y += speed
        if barrel_rect.top >= screen.get_height():
            barrel_rect.bottom = random.randint(-20, -10) * 10
            barrel_rect.left = random.randint(barrel_surface.get_width(), screen.get_width() - barrel_surface.get_width())
            barrel_rect.y += random.randint(-1, 1) # this nudges object falling speed slightly up/down
        # duck positioning
        duck_rect.y += speed
        if duck_rect.top >= screen.get_height():
            duck_rect.bottom = random.randint(-40, -20) * 10
            duck_rect.left = random.randint(duck_surface.get_width(), screen.get_width() - duck_surface.get_width())
            duck_rect.y += random.randint(-1, 1)
        # energy positioning
        energy_rect.y += speed * 0.9
        if energy_rect.top >= screen.get_height():
            energy_rect.bottom = random.randint(-30, -15) * 10
            energy_rect.left = random.randint(energy_surface.get_width(), screen.get_width() - energy_surface.get_width())
            energy_rect.y += random.randint(-1, 1)
        # collision ver 2
        if gravity > 0 and player_rect.colliderect(barrel_rect):
            """ if event.key == pygame.K_UP and event.type == pygame.KEYDOWN: """
            gravity = -13
        # player is boxed in! but will DIE if they fall
        if player_rect.right <= 50:
            player_rect.right = 50
        if player_rect.left >= 382:
            player_rect.left = 382
        if player_rect.top >= 768:
            game = False
            menu_music()
            if energy_collect > highscore:
                highscore = energy_collect
        if player_rect.bottom <= 84:
            player_rect.bottom = 84

        # BLITskrieg
        screen.blit(barrel_surface, barrel_rect)
        screen.blit(duck_surface, duck_rect)
        screen.blit(energy_surface, energy_rect)
        screen.blit(player_surface, player_rect)
        # game over
        if score <= 0:
            game = False
            menu_music()
            if energy_collect > highscore:
                highscore = energy_collect

    else:
        screen.blit(bg_surface, bg_rect)
        screen.blit(bg1_surface, bg1_rect)
        draw_text("Moving About", font, "#bbbbbb", screen, 40)
        draw_text("PLAY (space)", font, "#bbbbbb", screen, 160)
        draw_text("MOVE (arrows)", font, "#bbbbbb", screen, 200)
        draw_text(f"{sound} (s)", font, "#bbbbbb", screen, 240)
        draw_text(f"HIGH SCORE: {highscore - dif}", font, "#bbbbbb", screen, 320)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE and highscore - dif > 0:
            dif += 1

    # internal clock
    pygame.display.update()
    print(highscore, dif, highscore + dif, highscore - dif)
    clock.tick(60)