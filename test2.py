def game_loop():
    global game, score, speed, energy_collect, gravity, player_rect  # Add 'player_rect' to the global declarations

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
                barrel_rect = barrel_surface.get_rect(center = (random.randint(32,400), random.randint(-500,-200)))
                duck_rect = duck_surface.get_rect(center = (random.randint(25,417), random.randint(-1000,-500)))
                player_rect = player_surface.get_rect(center = (216,284))

    if game:
        # player movement
        player_speed = 9
        player_rect.y += 2
        if player_rect.colliderect(duck_rect):
            player_speed *= 0.35
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            player_speed = speed
        """ if keys[pygame.K_UP]:
            player_rect.y -= player_speed """
        
        """ if keys[pygame.K_DOWN]:
            player_rect.y += player_speed * 0.56 """
        if keys[pygame.K_LEFT]:
            player_rect.x -= player_speed * 0.8
        if keys[pygame.K_RIGHT]:
            player_rect.x += player_speed * 0.8
        if event.type == pygame.KEYDOWN and gravity > 2:
            if event.key == pygame.K_UP:
                gravity = -12

        if energy_collect >= 10:
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
            speed = 15
            
        # background & text/score function
        screen.blit(bg_surface,(0,0))
        scores()

        player_animation()

        gravity += .5
        player_rect.y += gravity

        # barrel positioning
        barrel_rect.y += speed
        if barrel_rect.top >= 768:
            barrel_rect.bottom = random.randint(-250,-200)
            barrel_rect.x = random.randint(32, 400)
            barrel_rect.y += random.randint(-1, 1)

        # duck positioning
        duck_rect.y += speed
        if duck_rect.top >= 768:
            duck_rect.bottom = random.randint(-400,-350)
            duck_rect.x = random.randint(25, 417)
            duck_rect.y += random.randint(-1, 1)

        # energy positioning
        energy_rect.y += speed * 0.9
        if energy_rect.top >= 768:
            energy_rect.bottom = -500
            energy_rect.x = random.randint(25, 417)
            energy_rect.y += random.randint(-1, 1)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print(f"S: {speed}")
                print(f"B: {barrel_rect.y}")
                print(f"D: {duck_rect.y}")
                print(f"E: {energy_rect.y}")

        # collision ver 1
        """ if player_rect.bottom >= barrel_rect.top and gravity > 0 and barrel_rect.left < player_rect.centerx < barrel_rect.right and not barrel_rect.top < player_rect.top:
            player_rect.bottom = barrel_rect.top
            gravity = -16 """
        
        # collision ver 2
        if event.type == pygame.KEYDOWN and player_rect.colliderect(barrel_rect):
            if event.key == pygame.K_UP and gravity < 0:
                gravity = -16

        # player positioning
        if player_rect.right <= 50:
            player_rect.right = 50
        if player_rect.left >= 382:
            player_rect.left = 382
        if player_rect.top >= 768:
            game = False
        if player_rect.bottom <= 84:
            player_rect.bottom = 84

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
                    barrel_rect = barrel_surface.get_rect(center=(random.randint(32, 400), random.randint(-500, -200)))
                    duck_rect = duck_surface.get_rect(center=(random.randint(25, 417), random.randint(-1000, -500)))
                    player_rect = player_surface.get_rect(center=(216, 284))  # Define 'player_rect' globally

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
                        barrel_rect = barrel_surface.get_rect(center = (random.randint(32,400), random.randint(-500,-200)))
                        duck_rect = duck_surface.get_rect(center = (random.randint(25,417), random.randint(-1000,-500)))
                        player_rect = player_surface.get_rect(center = (216,284))

            if game:
                # player movement
                player_speed = 9
                player_rect.y += 2
                if player_rect.colliderect(duck_rect):
                    player_speed *= 0.35
                keys = pygame.key.get_pressed()
                if keys[pygame.K_f]:
                    player_speed = speed
                """ if keys[pygame.K_UP]:
                    player_rect.y -= player_speed """
                
                """ if keys[pygame.K_DOWN]:
                    player_rect.y += player_speed * 0.56 """
                if keys[pygame.K_LEFT]:
                    player_rect.x -= player_speed * 0.8
                if keys[pygame.K_RIGHT]:
                    player_rect.x += player_speed * 0.8
                if event.type == pygame.KEYDOWN and gravity > 2:
                    if event.key == pygame.K_UP:
                        gravity = -12

                if energy_collect >= 10:
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
                    speed = 15
                    
                # background & text/score function
                screen.blit(bg_surface,(0,0))
                scores()

                player_animation()

                gravity += .5
                player_rect.y += gravity

                # barrel positioning
                barrel_rect.y += speed
                if barrel_rect.top >= 768:
                    barrel_rect.bottom = random.randint(-250,-200)
                    barrel_rect.x = random.randint(32, 400)
                    barrel_rect.y += random.randint(-1, 1)

                # duck positioning
                duck_rect.y += speed
                if duck_rect.top >= 768:
                    duck_rect.bottom = random.randint(-400,-350)
                    duck_rect.x = random.randint(25, 417)
                    duck_rect.y += random.randint(-1, 1)

                # energy positioning
                energy_rect.y += speed * 0.9
                if energy_rect.top >= 768:
                    energy_rect.bottom = -500
                    energy_rect.x = random.randint(25, 417)
                    energy_rect.y += random.randint(-1, 1)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        print(f"S: {speed}")
                        print(f"B: {barrel_rect.y}")
                        print(f"D: {duck_rect.y}")
                        print(f"E: {energy_rect.y}")

                # collision ver 1
                """ if player_rect.bottom >= barrel_rect.top and gravity > 0 and barrel_rect.left < player_rect.centerx < barrel_rect.right and not barrel_rect.top < player_rect.top:
                    player_rect.bottom = barrel_rect.top
                    gravity = -16 """
                
                # collision ver 2
                if event.type == pygame.KEYDOWN and player_rect.colliderect(barrel_rect):
                    if event.key == pygame.K_UP and gravity < 0:
                        gravity = -16

                # player positioning
                if player_rect.right <= 50:
                    player_rect.right = 50
                if player_rect.left >= 382:
                    player_rect.left = 382
                if player_rect.top >= 768:
                    game = False
                if player_rect.bottom <= 84:
                    player_rect.bottom = 84

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


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((432, 768))
    pygame.display.set_caption("Moving About")
    clock = pygame.time.Clock()
    font = pygame.font.Font("fonts/RobotoMono-Semibold.ttf", 50)

    while True:
        choice = main_menu()
        if choice == "play":
            # Reset game state
            game = True
            score = 1000
            speed = 5
            energy_collect = 0
            gravity = 0
            player_rect = player_surface.get_rect(center=(216, 284))  # Define 'player_rect' globally

            # Initialize game objects here (before the game loop starts)
            barrel_surface = pygame.image.load("graphics/barrel.png").convert_alpha()
            barrel_rect = barrel_surface.get_rect(center=(random.randint(32, 400), random.randint(-20, -10) * 10))
            duck_surface = pygame.image.load("graphics/duck.png").convert_alpha()
            duck_rect = duck_surface.get_rect(center=(random.randint(25, 417), random.randint(-40, -20) * 10))
            energy_surface = pygame.image.load("graphics/energy.png").convert_alpha()
            energy_rect = duck_surface.get_rect(center=(random.randint(25, 417), random.randint(-30, -15) * 10))
            player_surface_1 = pygame.image.load("graphics/player_1.png").convert_alpha()
            player_surface_2 = pygame.image.load("graphics/player_2.png").convert_alpha()
            player_anim = [player_surface_1, player_surface_2]
            player_index = 0
            player_surface = player_anim[player_index]
            player_rect = player_surface.get_rect(center=(216, 284))  # Define 'player_rect' globally
            player_surface_up = player_surface
            player_surface_down = pygame.transform.rotate(player_surface, 180)
            player_surface_left = pygame.transform.rotate(player_surface, 10)
            player_surface_right = pygame.transform.rotate(player_surface, 350)

            game_loop()
        elif choice == "quit":
            pygame.quit()
            exit()
