import pygame
import math

# Initialize global variables
newy = 0
newx = 0
level = 1
score = 0
speed = 1  # Initial movement speed
speed_increment = 0.75  # Amount of speed increase per level up

black = (0, 0, 0)


def dartPath(startX, startY, initialSpeed, angle, time):
    global newx, newy
    # calculates the velocity of the ball along each axis based on the angle the ball was fired at
    velx = math.cos(math.radians(angle)) * initialSpeed
    vely = math.sin(math.radians(angle)) * initialSpeed

    # projectile motion equations
    xMotion = velx * time
    yMotion = (vely * time) + ((-9.8 * (time) ** 2) / 2)

    # finds the next coordinate along the darts path
    newx = round(xMotion + startX)
    newy = round(startY - yMotion)


def board():
    pygame.init()
    win = pygame.display.set_mode((500, 500))

    global x, y, up, godMode, score, newx, newy, level, speed
    # Starting coordinates for the board.
    y = 0
    x = 450

    # Starting coordinates for the second board.
    y2 = 10
    x2 = 445

    # Starting coordinates for the third board.
    y3 = 20
    x3 = 440
    up = True

    # Starting coordinates for the dart.
    ydd = 0
    xdd = 10

    # Used to instantly win the game.
    godMode = False

    # Flag to indicate if the dart has been fired
    dshot = False

    # Board Width and Height.
    bwidth = 10
    bheight = 70

    # Width and Height for second board.
    b2width = 5
    b2height = 50

    # Width and Height for third board.
    b3width = 5
    b3height = 30

    # Sets starting width for the tracer and sets the frame tracker to change tracer width
    tracerStartingWidth = 1
    changeTracerWidth = 0

    # Sets the initial colour for the tracer
    red = 255
    green = 0
    blue = 0

    # Time variable for dart motion
    t = 1

    if speed < 0:
        speed *= -1

    # Keeps the game running - while loop 'run'.
    run = True
    while run:
        score_font = pygame.font.SysFont("arial", 30)

        # Delay before running the game.
        pygame.time.delay(10)

        # Background colour.
        win.fill((250, 250, 250))

        for event in pygame.event.get():
            # When the game is quit, run = false which stops the loop.
            if event.type == pygame.QUIT:
                run = False

        # 'Keys' variable which stores which keys are pressed.
        keys = pygame.key.get_pressed()

        # If dart isn't fired and up or down key is pressed, the dart will move up and down.
        if keys[pygame.K_UP] and not dshot:
            ydd -= 2
        if keys[pygame.K_DOWN] and not dshot:
            ydd += 2

        # Space = game won.
        if keys[pygame.K_SPACE]:
            godMode = True

        # Drawing the dart.
        pygame.draw.rect(win, (255, 0, 0), (xdd, ydd, 20, 10))
        # Drawing the board.
        pygame.draw.rect(win, (160, 32, 240), (x, y, bwidth, bheight))
        # Drawing the second board.
        pygame.draw.rect(win, (255, 165, 0), (x2, y2, b2width, b2height))
        # Drawing the third board.
        pygame.draw.rect(win, (0, 255, 0), (x3, y3, b3width, b3height))

        # Drawing the Score text.
        score_text = score_font.render(f'Score: {score}', True, (0, 0, 0))
        win.blit(score_text, [200, 0])

        # Checking to see if the fire key is pressed - Right Key.
        if keys[pygame.K_RIGHT]:
            dshot = True

        # Checking to see if game was quit - Left Key
        if keys[pygame.K_LEFT]:
            print("Left the game")
            return 2

        # Dart movement speed along x-axis after it's fired.
        if dshot:
            dartPath(xdd, ydd, 85, 0, t)
            pygame.draw.circle(win, (255, 0, 0), (newx, newy), 5)

            # Update time for next frame
            t += 0.05

            # Calculate distance from dart to board
            distance = int(math.sqrt((x - xdd) ** 2 + ((y + 35) - ydd) ** 2))

            # Adjust tracer color based on distance
            if distance > 255:
                distance = 255
                red = distance
            else:
                red = distance
                green += 1
                if xdd > x:
                    red = 255
                    green = 0

            # Check if the dart intersects with any of the boards
            if newx >= x3 - 2 and newx <= x3 and newy >= y3 and newy <= y2 + b3height:
                score += 3
                print("You Hit a Bullseye!")
                level += 1  # Increment level when the dart hits the board
                if level > 4:
                    level = 4  # Cap the level at 4
                speed = 1 + speed_increment * level  # Increase speed with each level
                print("Level:", level)  # Print current level
                return 1

            elif newx >= x2 - 2 and newx <= x2 and newy >= y2 and newy <= y2 + b2height:
                score += 2
                print("You Got Two Points.")
                level += 1  # Increment level when the dart hits the board
                if level > 4:
                    level = 4  # Cap the level at 4
                speed = 1 + speed_increment * level  # Increase speed with each level
                print("Level:", level)  # Print current level
                return 1

            elif newx >= x - 2 and newx <= x and newy >= y and newy <= y + bheight:
                score += 1
                print("You Got One Point.")
                level += 1  # Increment level when the dart hits the board
                if level > 4:
                    level = 4  # Cap the level at 4
                speed = 1 + speed_increment * level  # Increase speed with each level
                print("Level:", level)  # Print current level
                return 1

            elif newx > 500:
                print("You Missed!")
                return 0

        # Changes how fast the board is moving on y-axis.
        # y2 and y3 are for the two smaller boards.
        y += speed
        y2 += speed
        y3 += speed

        # Used to change Movement direction of the board, when it hits edges.
        if y <= 0 or y >= 500 - 70:
            speed *= -1

        # Updates the canvas.
        pygame.display.update()

    # Quits the Game.
    pygame.quit()

# Run the game loop
while True:
    result = board()
    if result == 2:
        break

