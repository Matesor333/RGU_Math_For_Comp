# import pygame module in this program
import pygame
import math




global level
level = 1
score = 0

black = (0, 0, 0)



def board():
    pygame.init()


    win = pygame.display.set_mode((500, 500))



    global x, y, up,godMode,score
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
    ydd=0
    xdd=10

    # Used to instantly win the game.
    godMode = False
    speed =1
    #
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

    #Sets starting width for the tracer and sets the frame tracker to change tracer width
    tracerStartingWidth = 1
    changeTracerWidth = 0

    #Sets the initial colour for the tracer
    red = 255
    green = 0
    blue = 0



    if speed<0:
        speed*=-1

    




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
        if keys[pygame.K_UP] and dshot == False:
            ydd -= 2


        if keys[pygame.K_DOWN] and dshot == False:
                ydd += 2

        # Space = game won.
        if keys[pygame.K_SPACE]:
            godMode=True

        # Drawing the dart.
        pygame.draw.rect(win, (255, 0, 0), (xdd, ydd,20,10),)
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
            dshot=True

        # Checking to see if game was quit - Left Key
        if keys[pygame.K_LEFT]:
            print("Left the game")
            return 2

        # Dart movement speed along x-axis after it's fired.
        if dshot==True:
            xdd+=2

            #Gets the distance the dart is from the board
            distance = int(math.sqrt((x - xdd) ** 2 + ((y + 35) - ydd) ** 2))

            #Checks if the distance is greater than 255 and then sets the "red" in RGB to 255
            if distance > 255:
                distance = 255
                red = distance

            #Otherwse set red equal to distance as it decreases and increase the green value up by one per frame
            else:
                red = distance 
                green += 1

                #Checks if the dart is past the board and then sets the red to 255 and green to 0
                if xdd > x:
                    red = 255
                    green = 0
            
            #Checks if the tracker for the number of frames passed equals 20 and then increases the tracer width by 1 and drawing the tracer, returning the frame tracker back to 0
            if changeTracerWidth == 20:
                tracerStartingWidth = tracerStartingWidth + 1
                pygame.draw.line(win, (red, green, blue), (xdd - xdd + 5, ydd + 5), (xdd, ydd + 5), tracerStartingWidth)
                changeTracerWidth = 0

            #Otherwise, draw the tracer with the current width and then increment the tracker by 1
            else:
                pygame.draw.line(win, (red, green, blue), (xdd - xdd + 5, ydd + 5), (xdd, ydd + 5), tracerStartingWidth)
                changeTracerWidth = changeTracerWidth + 1



         # First statement checks if the drat intersects with the smallest rectangle.
        if xdd>=x3-2 and xdd<=x3 and ydd>=y3 and ydd<=y2+b3height:
            score += 3
            print("You Hit a Bullseye!")
            return 1
            
        # Checks to see if the dart intersects with the middle rectangle.
        elif xdd>=x2-2 and xdd<=x2 and ydd>=y2 and ydd<=y2+b2height:
            score += 2
            print("You Got Two Points.")
            return 1

        # Checks to see if the dart intersects with the largest rectangle.
        elif xdd>=x-2 and xdd<=x and ydd>=y and ydd<=y+bheight:
            score += 1
            print("You Got One Point.")

            return 1



        # If dart x-coordinate is greater than 500 (canvas width) - You Lost.
        elif xdd>500:
            print("You Missed!")
            return 0


        # Changes how fast the board is moving on y-axis.
        # y2 and y3 are for the two smaller boards.
        y+= speed
        y2+= speed
        y3+= speed

        # Used to change Movement direction of the board, when it hits edges.
        if y <= 0 or y >= 500 - 70:
            speed *= -1



        # Updates the canvas.
        pygame.display.update()


    # Quits the Game.
    pygame.quit()




board()