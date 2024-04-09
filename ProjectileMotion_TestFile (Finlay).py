import pygame as pg
import math as m
#creates class for dart object
class dart(object):
    def __init__(self,x,y,radius,colour):
           self.x = x
           self.y = y
           self.radius = radius
           self.colour = colour
    #draws the dart on the surface
    def draw(self, screen):
          pg.draw.circle(screen, (0,0,0), (self.x,self.y), self.radius)
          pg.draw.circle(screen, self.colour, (self.x,self.y), self.radius-1) 
    #emulates the dart path by calculating the each coordinate that the dart will pass through and returning that to be passed as parameters in the draw function
    def dartPath(startX, startY, initialSpeed, angle, time):
        #calculates the velocity of the ball along eaach axis based on the angle the ball was fired at
        velx = m.cos(m.radians(angle)) * initialSpeed
        vely = m.sin(m.radians(angle)) * initialSpeed

        #projectile motion equations
        xMotion = velx * time

        yMotion = (vely * time) + ((-9.8 * (time)**2)/2)

        #finds the next coordinate along the darts path
        newx = round(xMotion + startX)
        newy = round(startY - yMotion)

        return (newx, newy)

#acts as the frames, (makes the game screen update with the new given info)
def redraw(dShot):
      screen.fill((64,64,64))
      dart1.draw(screen)
      if dShot ==False:
        pg.draw.line(screen, (255,255,255), line[0], line[1])
      pg.display.update()
      
#screen setup
screen = pg.display.set_mode((500,500))


x,y = screen.get_size()

#initial variables the be declared 
xdd = 5
ydd = y/2
dshot = False
run = True
dart1 = dart(xdd, ydd, 5, (255,255,255))

while run:
    pg.time.delay(5)
    mousePos = pg.mouse.get_pos()
    #draws a line between the dart and the players mouse position, (is used the calculate the angle and initial speed)
    line = [(dart1.x,dart1.y), mousePos]
    redraw(dshot)

    #if the dart is shot, increments the time and finds the new coordinates of the ball and then updates the dart object's position
    if dshot:
        time += 0.05
        pos = dart.dartPath(xDart,yDart, initialSpeed,angle,time)
       # print(pos)
        dart1.x = pos[0]
        dart1.y = pos[1]



    for event in pg.event.get():
        if event.type ==  pg.QUIT:
            run = False
        
        keys = pg.key.get_pressed()

        if keys[pg.K_UP] and dshot == False:
                dart1.y -= 2
                print(dart1.x, dart1.y)


        if keys[pg.K_DOWN] and dshot == False:
                dart1.y += 2

        #onmouse click, initialises the darts motion, and calculates the initial velocity and angle
        if event.type == pg.MOUSEBUTTONDOWN:
                dshot=True
                xDart = dart1.x
                yDart = dart1.y
                time = 0
                #calculates the angle based on the right angled triangle created by the line from the dart to the mouse, and the distance between the dart and the lines x and y coords
                angle = m.degrees(m.atan((dart1.y - line[1][1])/ (line[1][0] - dart1.x)))
                print(angle)
                #calculates the initial speed based on the length of the line. can be adjusted by changing the value the equation is divided by
                #                                                                                  v- here
                initialSpeed = m.sqrt((line[1][1] - line[0][1])**2 + (line[1][0] - line[0][0])**2)/2

        if keys[pg.K_LEFT]:
                pg.QUIT
        
