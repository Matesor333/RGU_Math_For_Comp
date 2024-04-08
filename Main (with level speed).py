import pygame

global score
score = 0

black = (0, 0, 0)

def board(level):
    pygame.init()

    win = pygame.display.set_mode((500, 500))

    global x, y, up, godMode, score, first_hit
    y = 0
    x = 450
    y2 = 10
    x2 = 445
    y3 = 20
    x3 = 440
    up = True
    ydd = 0
    xdd = 10
    godMode = False
    speed = 1
    dshot = False
    bwidth = 10
    bheight = 70
    b2width = 5
    b2height = 50
    b3width = 5
    b3height = 30

    if speed < 0:
        speed *= -1

    run = True
    first_hit = True
    while run:
        score_font = pygame.font.SysFont("arial", 30)
        pygame.time.delay(10)
        win.fill((250, 250, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and dshot == False:
            ydd -= 2

        if keys[pygame.K_DOWN] and dshot == False:
            ydd += 2

        if keys[pygame.K_SPACE]:
            godMode = True

        pygame.draw.rect(win, (255, 0, 0), (xdd, ydd, 20, 10))
        pygame.draw.rect(win, (160, 32, 240), (x, y, bwidth, bheight))
        pygame.draw.rect(win, (255, 165, 0), (x2, y2, b2width, b2height))
        pygame.draw.rect(win, (0, 255, 0), (x3, y3, b3width, b3height))

        score_text = score_font.render(f'Score: {score}', True, (0, 0, 0))
        win.blit(score_text, [200, 0])

        if keys[pygame.K_RIGHT]:
            dshot = True

        if keys[pygame.K_LEFT]:
            print("Left the game")
            return 2

        if dshot == True:
            xdd += 2

        if xdd >= x3 - 2 and xdd <= x3 and ydd >= y3 and ydd <= y2 + b3height:
            score += 3
            if first_hit:
                print(f"You Hit a Bullseye! Level: {level}")
                first_hit = False
            return 1

        elif xdd >= x2 - 2 and xdd <= x2 and ydd >= y2 and ydd <= y2 + b2height:
            score += 2
            if first_hit:
                print(f"You Got Two Points. Level: {level}")
                first_hit = False
            return 1

        elif xdd >= x - 2 and xdd <= x and ydd >= y and ydd <= y + bheight:
            score += 1
            if first_hit:
                print(f"You Got One Point. Level: {level}")
                first_hit = False
            return 1

        elif xdd > 500:
            print("You Missed!")
            return 0

        # Increase movement speed based on level
        if level == 2:
            speed = 2
        elif level == 3:
            speed = 3
        elif level == 4:
            speed = 4

        # Update dartboard movement
        if up:
            y += speed
            y2 += speed
            y3 += speed
            if y3 >= 500 - b3height:  # Stop when reaching bottom edge
                up = False
        else:
            y -= speed
            y2 -= speed
            y3 -= speed
            if y3 <= 0:  # Reverse direction when reaching top edge
                up = True

        pygame.display.update()

    pygame.quit()

# Example usage
level = 1
while level <= 4:
    print(f"Level {level}:")
    result = board(level)
    if result == 1:  # Increase level only if the dart hits the board
        level += 1
        first_hit = True
