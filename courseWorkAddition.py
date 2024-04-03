import pygame as pg
import math as m

class dart(object):
    def __init__(self,x,y,radius,colour):
           self.x = x
           self.y = y
           self.radius = radius
           self.colour = colour

    def draw(self, screen):
          pg.draw.circle(screen, (0,0,0), (self.x,self.y), self.radius)
          pg.draw.circle(screen, self.colour, (self.x,self.y), self.radius-1) 

    def dartPath(startX, startY, initialSpeed, angle, time):
        velx = m.cos(m.radians(angle)) * initialSpeed
        vely = m.sin(m.radians(angle)) * initialSpeed

        xMotion = velx * time

        yMotion = (vely * time) + ((-9.8 * (time)**2)/2)

        newx = round(xMotion + startX)
        newy = round(startY - yMotion)

        return (newx, newy)

def redraw(dShot):
      screen.fill((64,64,64))
      dart1.draw(screen)
      if dShot ==False:
        pg.draw.line(screen, (255,255,255), line[0], line[1])
      pg.display.update()
      

screen = pg.display.set_mode((500,500))


x,y = screen.get_size()

xdd = 5
ydd = y/2
dshot = False
run = True
dart1 = dart(xdd, ydd, 5, (255,255,255))

while run:
    pg.time.delay(5)
    mousePos = pg.mouse.get_pos()
    line = [(dart1.x,dart1.y), mousePos]
    redraw(dshot)
   # print(line[0], line[1])
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

        if event.type == pg.MOUSEBUTTONDOWN:
                dshot=True
                xDart = dart1.x
                yDart = dart1.y
                time = 0
                angle = m.degrees(m.atan((dart1.y - line[1][1])/ (line[1][0] - dart1.x)))
                print(angle)
                initialSpeed = m.sqrt((line[1][1] - line[0][1])**2 + (line[1][0] - line[0][0])**2)/2

        if keys[pg.K_LEFT]:
                pg.QUIT
        