import pygame, sys
import random
import time
import math
import pygame.mixer
from pygame.locals import *

puase_colour= (0,0,0)

pygame.init()
black = (0,0,0)
white = (255,255,255)
red = (255,25,25)
yellow =(255,242,0)
green = (0, 255, 0)
grey =(195,195,195)
brown = (190,128,44)
blue = (1,157,240)
BLUE =  (0,206,209)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
brown_sand =[238, 220, 130]
background_colour = (100,205,240)
(width, height) = (1300, 600)
clock = pygame.time.Clock()
c = 300
rez = (1300, 600)
exposize = (200, 200)
enemeysize =(100, 100)
radarsound=pygame.mixer.Sound('radar.wav')
bsound = pygame.mixer.Sound('crysis.wav')
exposound = pygame.mixer.Sound('bomb2.wav')
bombsound=pygame.mixer.Sound('explosion2.wav')
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('gravity and mouse throwing')
expo = 0
pygame.font.init()
puase = 0
splashscreen = 1
killed = 0
intro = 0
numnade = 3
numnade_2 = 2
radar = 0
drag = .9999
elasticity = 0.75
gravity = (math.pi, 0.02)
blood = pygame.image.load("blood.gif-w=430")
bimg = pygame.image.load("grenade2.jpg")
prodigy = pygame.transform.rotate(pygame.image.load("prodigy1.png"), -15)
start = pygame.image.load("start.png")
wolf = pygame.image.load("802.gif")
wolfg = pygame.image.load("802g.gif")
wolfj = pygame.image.load("802j.gif")
explosion =pygame.Surface.convert_alpha( pygame.image.load("explosion.png"))
after_expo = pygame.image.load("afterexpo.gif")
nade = pygame.image.load("nade.png")
in1 = pygame.image.load("in1.png")
in2 = pygame.image.load("in2.png")
in3 = pygame.image.load("in3.png")
in4 = pygame.image.load("in4.png")
in5 = pygame.image.load("in5.png")
arrow = pygame.image.load("whitearrow.gif")
lev = pygame.image.load("levelmap1.png")
lev2 = pygame.image.load("maplevel2.png")
logo = pygame.image.load("logo.gif")
cred =pygame.image.load("cred.gif")
plane = pygame.image.load("plane.png")
fin = 0
end = 0
levelcomplete = 10
maplevel =0
mobj1 = 500
moveint = -50
creed =0
def text ( text , size , font, color, x, y):
    
    screen.blit(pygame.font.SysFont(font, size).render(str(text) , 1, color), (x,y)) 

def enemey_kill( x, y, ballx, bally, ballsize,expo):
    
    if x+40 > ballx - ballsize - 90 and x+20 < ballx + ballsize + 90 and expo == 1 and y+40 > bally - ballsize - 90 and y+20 < bally + ballsize + 100:
        return True
    else:
        return False
          

def addVectors(vector1, vector2):
    angle1, length1 = vector1
    angle2, length2 = vector2
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2
    angle = 0.5 * math.pi - math.atan2(y, x)
    length  = math.hypot(x, y)

    return (angle, length)
def findBall(balls, x, y):
    for p in balls:
        if math.hypot(p.x-x, p.y-y) <= p.size:
            return p
    return None

class Wolf:

    def __init__(self,image, resize, x, y,s,):

        self.image=image

        self.y=y

        self.x=x

        self.resize=resize
        self.score = s
    
        self.sound = bombsound
        self.org = x
        
    def enemeys (self,kill) :
        
        if kill == False:
            screen.blit(pygame.transform.scale(self.image, self.resize), (self.x , self.y))
        
        if self.score == 0:
            self.x = self.org
        
           
        if kill == True :
            self.sound.play()
            screen.blit(pygame.transform.scale(after_expo, self.resize), (self.x , self.y))
            self.score = 1
            if kill == True:
                self.x = -100
            
           
                
        
         
        
        
    

    
        

    #draw enemey
Wolf1 = Wolf( wolf, enemeysize, 800 , 500,0)
Wolf2 = Wolf( wolf, enemeysize, 800 , 100,0)
Wolf3 = Wolf( wolfg, enemeysize, 800 , 500,0)
Wolf4 = Wolf( wolf, enemeysize, 900 , 200,0)
Wolf5 = Wolf( wolf, enemeysize, 1000 , 500,0)
Wolf6 = Wolf( wolf, enemeysize, 1100 , 500,0)
Wolf7 = Wolf( wolf, enemeysize, 680 , 500,0)
Wolf8 = Wolf( wolf, enemeysize, 880 , 500,0)
Wolf9 = Wolf( wolf, enemeysize, 1200 , 0,0)
#level 7
Wolf10 = Wolf( wolfg, enemeysize, 900 , 0,0)
Wolf12 = Wolf( wolfg, enemeysize, 700 , 190,0)
Wolf11 = Wolf( wolfg, enemeysize, 900 , 500,0)
Wolf13 = Wolf( wolfg, enemeysize, 1200 , 190,0)
# level 8
Wolf18 = Wolf( wolf, enemeysize, 900 , 150,0)
Wolf19 = Wolf( wolf, enemeysize, 900 , 300,0)
Wolf20 = Wolf( wolf, enemeysize, 900 , 500,0)

#level 1 sand
Wolf14 = Wolf( wolfj, enemeysize, 1200 , 500,0)
Wolf15 = Wolf( wolfg, enemeysize, 700 , 150,0)
Wolf16 = Wolf( wolfj, enemeysize, 900 , 500,0)
Wolf17 = Wolf( wolfj, enemeysize, 1200 , 210,0)
# level 2 sand
Wolf21 = Wolf( wolfj, enemeysize, 640 , 100,0)
Wolf22 = Wolf( wolfj, enemeysize, 640 , 300,0)
Wolf23 = Wolf( wolfj, enemeysize, 640 , 500,0)
# level 3 sand
Wolf24 = Wolf( wolfj, enemeysize, 640 , 500,0)
class Sprite:

    def __init__(self,a,d,width,height,color,fill):

        self.x=a

        self.y=d

        self.width=width

        self.height=height
        self.color=color
        self.splashscreen = splashscreen
        self.fill =fill
    
    def render(self,draw):

        if draw==True:

            pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height),self.fill)
        
# draw 
Sprite1=Sprite(100,50,100,100,black,0)
Sprite2=Sprite(600,450,50,150,black,0)
Sprite4=Sprite(600,300,1000,100,black,0)
Sprite3=Sprite(400,500,100,100,black,0)
Sprite5=Sprite(600,500,100,100,black,0)
Sprite6=Sprite(800,500,100,100,black,0)
# level 5
Sprite7=Sprite(600,200,50,400,black,0)
Sprite8=Sprite(600,400,500,50,black,0)
Sprite9=Sprite(800,200,50,400,black,0)
Sprite10=Sprite(1000,200,50,400,black,0)
#level 6
Sprite8=Sprite(600,400,580,50,black,0)
Sprite12=Sprite(600,100,600,50,black,0)
Sprite11=Sprite(600,450,50,150,black,0)
Sprite100=Sprite(100,100,150,150,black,20)
#level 7
Sprite13=Sprite(600,280,200,50,green,0)
Sprite14=Sprite(850,100,150,50,green,0)
Sprite15=Sprite(1100,280,200,50,green,0)
Sprite16=Sprite(850,400,150,50,green,0)
Sprite17=Sprite(600,0,50,500,green,0)
Sprite18=Sprite(600,0,700,600,grey,0)
Sprite19=Sprite(580,500,30,100,brown,0)
Sprite20=Sprite(850,500,200,100,brown,0)
Sprite21=Sprite(700,80,100,400,blue,0)
Sprite22=Sprite(900,80,100,400,blue,0)
Sprite23=Sprite(1100,80,100,400,blue,0)
# level 8
Sprite30=Sprite(800,200,50,400,black,0)
Sprite28=Sprite(800,250,300,20,black,0)
Sprite29=Sprite(800,400,300,20,black,0)
Sprite31=Sprite(1000,200,50,400,black,0)
#level 1 desart
Sprite24=Sprite(700, 0, 150, 250,brown_sand,0)
Sprite25=Sprite(700, 400, 150, 250,brown_sand,0)
Sprite26=Sprite(1000, 400, 100, 250,brown_sand,0)
Sprite27=Sprite(1200, 300, 250, 10,brown_sand,0)
#level 2 desart
Sprite33=Sprite(500, 0, 75, 600,brown_sand,0)
Sprite34=Sprite(500, 400, 300, 40,brown_sand,0)
Sprite35=Sprite(500, 200, 300, 40,brown_sand,0)
Sprite36=Sprite(800, 0, 75, 600,brown_sand,0)


class Ball():
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 0
        self.speed = 0
        self.angle = 0

    def display(self):

        
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
        
        
        
    
        
            
    def move(self):
        (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= drag
        

    def bounce(self):
        
        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.angle = - self.angle
            self.speed *= elasticity

        

        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle
            self.speed *= elasticity

        if self.y > height - self.size:
            self.y = 2*(height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
            self.speed
        

       
        
    def render(self,rx,ry,rw,rh):

        if self.x >= rx - self.size+1  and self.x <= rx +rw + self.size-1   and self.y >= ry - self.size and self.y <= ry + rh + ball.size :
            self.speed *= -elasticity
            self.angle = - self.angle
            
            if self.y >= ry -self.size and self.y <= ry-self.size +4:
                self.y = ry -self.size
            if self.y <= ry +rh + self.size and self.y >= ry +rh - self.size:
                self.y = ry+rh +self.size
                
        if self.x >= rx - self.size  and self.x <= rx +rw + self.size and self.y >= ry - self.size + 1 and self.y <= ry + rh + ball.size -1 :
            self.angle = - self.angle
            self.speed *= elasticity
            if self.x >= rx - self.size and self.x <= rx + 2 - self.size:
                self.x = self.x-2
                
            if self.x <= rx +rw + self.size  and self.x >= rx +rw + self.size - 2:
                self.x = self.x+2
                
        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
            self.speed
            
        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle
            self.speed *= elasticity

number_of_balls = 1
my_balls = []

for n in range(number_of_balls):
    size = 16
    x = 0
    y = 600    

    ball = ( Ball( x, y, size))
    ball.speed = random.random()
    ball.angle = random.uniform(0, math.pi*2)

    my_balls.append(ball)

selected_ball = None
running = True


            
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

        elif pygame.mouse.get_pos() >(400,0) and splashscreen > 1 and puase ==0 and fin == 0 and maplevel == 0 and intro == 0 :
            pygame.mouse.set_pos(0, 0)
        
        
        elif event.type == pygame.MOUSEBUTTONDOWN and splashscreen == 1 :
             if pygame.mouse.get_pos() > (100,0):
                 splashscreen = 2
                 
        elif event.type == pygame.MOUSEBUTTONUP and puase == 0 :
             selected_ball = None
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            selected_ball = findBall(my_balls, mouseX, mouseY)
        
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_ball = None
        elif event.type == KEYDOWN and splashscreen == 1 :
            
            if event.key == K_SPACE :
                splashscreen = 2
                numnade = 3
            if event.key == K_l :
                maplevel = 1
            if event.key == K_i :
                intro = 1
            if event.key == K_c :
                creed = 1
                if creed == 1:
                    creed =0
            if event.key == K_b :
                splashscreen = 3
            if event.key == K_RIGHT:
                if intro >= 1 and intro <= 5:
                    intro += 1
                if maplevel <= 3 and maplevel >= 1:
                    maplevel += 1   
            if event.key == K_LEFT:
                if maplevel <= 3 and maplevel >= 1:
                    maplevel -= 1 
                if intro >= 1 and intro <= 5:
                    intro -= 1
            if event.key == K_1:
                if maplevel == 1 and levelcomplete >= 0  :
                    Wolf1.score = 0
                    numnade = 3
                    splashscreen =2
                    maplevel = 0
                    ball.x = 0
                    ball.y =600
                if maplevel == 2 and levelcomplete >= 8  :
                    Wolf14.score = 0
                    Wolf15.score = 0
                    Wolf16.score = 0
                    Wolf17.score = 0
                    numnade = 5
                    splashscreen =10
                    maplevel = 0
                    ball.x = 0
                    ball.y =600
            if event.key == K_2:
                if maplevel == 1 and levelcomplete >= 1  :
                    Wolf2.score =0
                    Wolf5.score =0
                    splashscreen =3
                    maplevel = 0
                    numnade = 3
                    ball.x = 0
                    ball.y =600
                if maplevel == 2 and levelcomplete >= 9  :
                    Wolf21.score =0
                    Wolf22.score =0
                    Wolf23.score =0
                    Wolf24.score =0
                    splashscreen =11
                    maplevel = 0
                    numnade = 3
                    ball.x = 0
                    ball.y =600
            if event.key == K_3:
                if maplevel == 1 and levelcomplete >= 2  :
                    Wolf3.score = 0
                    splashscreen =4
                    maplevel = 0
                    numnade =2
                    ball.x = 0
                    ball.y =600
            if event.key == K_4:
                if maplevel == 1 and levelcomplete >= 3  :
                    Wolf4.score =0
                    splashscreen =5
                    Wolf4.score = 0
                    maplevel = 0
                    fin = 0
                    end = 0
                    numnade =3
                    ball.x = 0
                    ball.y =600
            if event.key == K_5:
                if maplevel == 1 and levelcomplete >= 4  :
                    splashscreen =6
                    Wolf6.score = 0
                    Wolf7.score = 0
                    Wolf8.score = 0
                    maplevel = 0
                    fin = 0
                    end = 0
                    numnade =5
                    ball.x = 0
                    ball.y =600
                    puase = 0
            if event.key == K_6:
                if maplevel == 1 and levelcomplete >= 5  :
                    splashscreen =7
                    Wolf6.score = 0
                    Wolf7.score = 0
                    Wolf8.score = 0
                    maplevel = 0
                    fin = 0
                    end = 0
                    numnade =5
                    ball.x = 0
                    ball.y =600
                    puase = 0
            if event.key == K_7:
                if maplevel == 1 and levelcomplete >= 6  :
                    splashscreen =8
                    Wolf18.score = 0
                    Wolf19.score = 0
                    Wolf20.score = 0
                    maplevel = 0
                    fin = 0
                    end = 0
                    numnade =4
                    ball.x = 0
                    ball.y =600
            if event.key == K_8:
                if maplevel == 1 and levelcomplete >= 7  :
                    splashscreen =9
                    Wolf10.score = 0
                    Wolf13.score = 0
                    Wolf14.score = 0
                    Wolf15.score = 0
                    maplevel = 0
                    fin = 0
                    end = 0
                    numnade =6
                    ball.x = 0
                    ball.y =600
        elif event.type == KEYDOWN and puase == 1 :
            if event.key == K_p :
                puase = 0
                c = 300
            if event.key == K_r:
                if splashscreen == 2:
                    Wolf1.score = 0
                    end = 0
                    fin = 0
                    puase =0
                    numnade =  3
                    c = 300
                    ball.x = 0
                    ball.y =600
                if splashscreen == 3:
                    Wolf2.score = 0
                    Wolf5.score = 0
                    puase = 0
                    end = 0
                    fin = 0
                    numnade =  3
                    c = 300
                    ball.x = 0
                    ball.y =600
                if splashscreen == 4:
                    Wolf3.score = 0
                    puase = 0
                    end = 0
                    fin = 0
                    numnade =  2
                    c = 300
                    ball.x = 0
                    ball.y =600
                if splashscreen == 5:
                    Wolf4.score = 0
                    puase = 0
                    end = 0
                    fin = 0
                    numnade =  3
                    c = 300
                    ball.x = 0
                    ball.y =600
                if splashscreen == 6:
                    Wolf7.score = 0
                    Wolf6.score = 0
                    Wolf8.score = 0
                    puase = 0
                    end = 0
                    fin = 0
                    numnade =  5
                    ball.x = 0
                    ball.y =600
                if splashscreen == 7:
                    Wolf6.score = 0
                    Wolf9.score = 0
                    puase = 0
                    end = 0
                    fin = 0
                    numnade =  4
                    ball.x = 0
                    ball.y =600
                if splashscreen == 8:
                    Wolf18.score = 0
                    Wolf19.score = 0
                    Wolf20.score = 0
                    puase = 0
                    end = 0
                    fin = 0
                    numnade =  4
                    ball.x = 0
                    ball.y =600
                if splashscreen == 9:
                    Wolf10.score = 0
                    Wolf13.score = 0
                    Wolf11.score = 0
                    Wolf12.score = 0
                    puase = 0
                    end = 0
                    fin = 0
                    numnade =  6
                    ball.x = 0
                    ball.y =600
                if splashscreen == 10:
                    Wolf14.score = 0
                    Wolf15.score = 0
                    Wolf16.score = 0
                    Wolf17.score = 0
                    puase = 0
                    end = 0
                    fin = 0
                    numnade =  5
                    ball.x = 0
                    ball.y =600
                if splashscreen == 11:
                    Wolf21.score =0
                    Wolf22.score =0
                    Wolf23.score =0
                    Wolf24.score =0
                    puase = 0
                    end = 0
                    fin = 0
                    numnade =  3
                    ball.x = 0
                    ball.y =600
            if event.key == K_h:
                splashscreen = 1
                puase = 0
                Wolf1.score = 0
                end = 0
                fin = 0  
                c = 300
                ball.x = 0
                ball.y =600
            if event.key == K_l :
                maplevel = 1
            if event.key == K_i :
                intro = 1
            if event.key == K_RIGHT:
                if maplevel <= 3 and maplevel >= 1:
                    maplevel += 1 
                if intro >= 1 and intro <= 5:
                    intro += 1
            if event.key == K_LEFT:
                if maplevel <= 3 and maplevel >= 1:
                    maplevel -= 1 
                if intro >= 1 and intro <= 5:
                    intro -= 1
            if event.key == K_1:
                if maplevel == 1 and levelcomplete >= 0  :
                    splashscreen =2
                    Wolf1.score = 0
                    maplevel = 0
                    numnade = 3
                    puase = 0
                    c = 300
                    ball.x = 0
                    ball.y =600
                if maplevel == 2 and levelcomplete >= 8  :
                    splashscreen =10
                    Wolf14.score = 0
                    Wolf15.score = 0
                    Wolf16.score = 0
                    Wolf17.score = 0
                    maplevel = 0
                    numnade = 5
                    puase = 0
                    c = 300
                    ball.x = 0
                    ball.y =600
            if event.key == K_2:
                if maplevel == 1 and levelcomplete >= 1  :
                    splashscreen =3
                    Wolf5.score = 0
                    Wolf2.score = 0
                    maplevel = 0
                    puase = 0
                    c=300
                    numnade =3
                    ball.x = 0
                    ball.y =600
                if maplevel == 2 and levelcomplete >= 9  :
                    splashscreen =11
                    Wolf21.score =0
                    Wolf22.score =0
                    Wolf23.score =0
                    Wolf24.score =0
                    maplevel = 0
                    numnade = 3
                    puase = 0
                    c = 300
                    ball.x = 0
                    ball.y =600
            if event.key == K_3:
                if maplevel == 1 and levelcomplete >= 2  :
                    splashscreen =4
                    Wolf3.score = 0
                    maplevel = 0
                    puase = 0
                    c =300
                    numnade =2
                    ball.x = 0
                    ball.y =600
            if event.key == K_4:
                if maplevel == 1 and levelcomplete >= 3  :
                    splashscreen =5
                    Wolf3.score = 0
                    maplevel = 0
                    fin = 0
                    end = 0
                    c=300
                    numnade =3
                    ball.x = 0
                    ball.y =600
                    puase = 0
            if event.key == K_5:
                if maplevel == 1 and levelcomplete >= 4  :
                    splashscreen =6
                    Wolf6.score = 0
                    Wolf7.score = 0
                    Wolf8.score = 0
                    maplevel = 0
                    c=300
                    fin = 0
                    end = 0
                    numnade =5
                    ball.x = 0
                    ball.y =600
                    puase = 0
            if event.key == K_6:
                if maplevel == 1 and levelcomplete >= 5  :
                    splashscreen =7
                    Wolf6.score = 0
                    Wolf9.score = 0
                    maplevel = 0
                    fin = 0
                    end = 0
                    c=300
                    numnade =4
                    ball.x = 0
                    ball.y =600
                    puase = 0
            if event.key == K_7:
                if maplevel == 1 and levelcomplete >= 6  :
                    splashscreen =8
                    Wolf18.score = 0
                    Wolf19.score = 0
                    Wolf20.score = 0
                    maplevel = 0
                    fin = 0
                    end = 0
                    c=300
                    numnade =6
                    ball.x = 0
                    ball.y =600
                    puase = 0
            if event.key == K_8:
                if maplevel == 1 and levelcomplete >= 7  :
                    splashscreen =9
                    Wolf10.score = 0
                    Wolf13.score = 0
                    Wolf12.score = 0
                    Wolf11.score = 0
                    maplevel = 0
                    fin = 0
                    end = 0
                    c=300
                    numnade =6
                    ball.x = 0
                    ball.y =600
                    puase = 0
        elif event.type == KEYDOWN and splashscreen > 1 and puase == 0 :
            if event.key == K_s :
                radarsound.play()
                radar = 1
                c = 1
                
            if event.key == K_SPACE and numnade > 0  :
                expo = 1
                c = 1
                exposound.play()
                if expo == 1 :
                    numnade = numnade - 1
            
            
            if event.key == K_c :
                
                if end == 1:
                    fin = 1
                if end == 2:
                    fin = 2
            if event.key == K_n :
                if fin == 1:
                    splashscreen = splashscreen+1 
                    fin = 0
                    Wolf2.score = 0
                    Wolf1.score = 0
                    Wolf3.score = 0
                    Wolf4.score = 0
                    Wolf5.score = 0
                    Wolf6.score = 0
                    Wolf7.score = 0
                    Wolf8.score = 0
                    Wolf9.score = 0
                    Wolf10.score = 0
                    Wolf11.score = 0
                    Wolf12.score = 0
                    Wolf13.score = 0
                    Wolf14.score = 0
                    Wolf15.score = 0
                    Wolf16.score = 0
                    Wolf17.score = 0
                    Wolf18.score = 0
                    Wolf19.score = 0
                    Wolf20.score = 0
                    Wolf21.score =0
                    Wolf22.score =0
                    Wolf23.score =0
                    Wolf24.score =0
                    end = 0
                    if splashscreen == 2:
                        numnade =  3
                        ball.x = 0
                        ball.y =600
                    if splashscreen == 3:
                        numnade =  3
                        ball.x = 0
                        ball.y =600
                    if splashscreen == 4:
                        numnade =  2
                        ball.x = 0
                        ball.y =600
                    if splashscreen == 5:
                        numnade =  3
                        ball.x = 0
                        ball.y =600
                    if splashscreen == 6:
                        numnade =  5
                        ball.x = 0
                        ball.y =600
                    if splashscreen == 7:
                        numnade =  4
                        ball.x = 0
                        ball.y =600
                    if splashscreen == 8:
                        numnade =  4
                        ball.x = 0
                        ball.y =600
                    if splashscreen == 9:
                        numnade =  6
                        ball.x = 0
                        ball.y =600
                    if splashscreen == 10:
                        numnade =  5
                        ball.x = 0
                        ball.y =600
                    if splashscreen == 11:
                        numnade =  3
                        ball.x = 0
                        ball.y =600
            if event.key == K_r:
                c =300
                if splashscreen == 2:
                    Wolf1.score = 0
                    end = 0
                    fin = 0
                    ball.x = 0
                    ball.y =600
                    numnade =  3
                if splashscreen == 3:
                    Wolf2.score = 0
                    Wolf5.score = 0
                    ball.x = 0
                    ball.y =600
                    end = 0
                    fin = 0
                    numnade =  3
                    
                if splashscreen == 4:
                    Wolf3.score = 0
                    puase = 0
                    end = 0
                    fin = 0
                    numnade =  2
                    ball.x = 0
                    ball.y =600
                if splashscreen == 5:
                    Wolf4.score = 0
                    puase = 0
                    end = 0
                    fin = 0
                    numnade =  3
                    ball.x = 0
                    ball.y =600
                if splashscreen == 6:
                    Wolf7.score = 0
                    Wolf6.score = 0
                    Wolf8.score = 0
                    puase = 0
                    end = 0
                    fin = 0
                    numnade =  5
                    ball.x = 0
                    ball.y =600
                if splashscreen == 7:
                    Wolf6.score = 0
                    Wolf9.score = 0
                    puase = 0
                    end = 0
                    fin = 0
                    numnade =  4
                    ball.x = 0
                    ball.y =600
                if splashscreen == 8:
                    Wolf18.score = 0
                    Wolf19.score = 0
                    Wolf20.score = 0
                    puase = 0
                    end = 0
                    fin = 0
                    numnade =  4
                    ball.x = 0
                    ball.y =600
                    puase = 0
                if splashscreen == 9:
                    Wolf10.score = 0
                    Wolf13.score = 0
                    Wolf11.score = 0
                    Wolf12.score = 0
                    puase = 0
                    end = 0
                    fin = 0
                    numnade =  6
                    ball.x = 0
                    ball.y =600
                    puase = 0
                if splashscreen == 10:
                    Wolf14.score = 0
                    Wolf15.score = 0
                    Wolf16.score = 0
                    Wolf17.score = 0
                    puase = 0
                    end = 0
                    fin = 0
                    numnade =  5
                    ball.x = 0
                    ball.y =600
                    puase = 0
                if splashscreen == 11:
                    Wolf21.score =0
                    Wolf22.score =0
                    Wolf23.score =0
                    Wolf24.score =0
                    puase = 0
                    end = 0
                    fin = 0
                    numnade =3
                    ball.x = 0
                    ball.y =600
                    puase = 0
            if event.key == K_h:
                splashscreen = 1
                Wolf1.score = 0
                end = 0
                fin = 0  
                numnade =  3
                ball.x = 0
                ball.y =600
                Wolf2.score = 0
                
            if event.key == K_p:   
                puase = 1
                c = 0.5
            if event.key == K_l :
                maplevel = 1
            if event.key == K_i :
                intro = 1
            if event.key == K_RIGHT:
                if maplevel <= 3 and maplevel >= 1:
                    maplevel += 1 
                if intro >= 1 and intro <= 5:
                    intro += 1
            if event.key == K_LEFT:
                if maplevel <= 3 and maplevel >= 1 :
                    maplevel -= 1 
                if intro >= 1 and intro <= 5:
                    intro -= 1
            if event.key == K_1:
                if maplevel == 1 and levelcomplete >= 0  :
                    numnade = 3
                    splashscreen =2
                    Wolf1.score = 0
                    maplevel = 0
                    fin = 0
                    end = 0
                    ball.x = 0
                    ball.y =600
                if maplevel == 2 and levelcomplete >= 8  :
                    numnade = 5
                    splashscreen =10
                    Wolf14.score = 0
                    Wolf15.score = 0
                    Wolf16.score = 0
                    Wolf17.score = 0
                    maplevel = 0
                    fin = 0
                    end = 0
                    ball.x = 0
                    ball.y =600
            if event.key == K_2:
                if maplevel == 1 and levelcomplete >= 1  :
                    splashscreen =3
                    Wolf2.score = 0
                    Wolf5.score = 0
                    maplevel = 0
                    fin = 0
                    numnade =3
                    end = 0
                    Wolf3.score = 0
                    Wolf1.score = 0
                    ball.x = 0
                    ball.y =600
                if maplevel == 2 and levelcomplete >= 9  :
                    numnade = 3
                    splashscreen =11
                    Wolf21.score =0
                    Wolf22.score =0
                    Wolf23.score =0
                    Wolf24.score =0
                    maplevel = 0
                    fin = 0
                    end = 0
                    ball.x = 0
                    ball.y =600
            if event.key == K_3:
                if maplevel == 1 and levelcomplete >= 2  :
                    splashscreen =4
                    Wolf3.score = 0
                    maplevel = 0
                    fin = 0
                    end = 0
                    numnade =2
                    ball.x = 0
                    ball.y =600
            if event.key == K_4:
                if maplevel == 1 and levelcomplete >= 3  :
                    splashscreen =5
                    Wolf4.score = 0
                    maplevel = 0
                    fin = 0
                    end = 0
                    numnade =3
                    ball.x = 0
                    ball.y =600
            if event.key == K_5:
                if maplevel == 1 and levelcomplete >= 4  :
                    splashscreen =6
                    Wolf6.score = 0
                    Wolf7.score = 0
                    Wolf8.score = 0
                    maplevel = 0
                    fin = 0
                    end = 0
                    numnade =5
                    ball.x = 0
                    ball.y =600
            if event.key == K_6:
                if maplevel == 1 and levelcomplete >= 5  :
                    splashscreen =7
                    Wolf6.score = 0
                    Wolf9.score = 0
                    maplevel = 0
                    fin = 0
                    end = 0
                    numnade =4
                    ball.x = 0
                    ball.y =600
            if event.key == K_7:
                if maplevel == 1 and levelcomplete >= 6  :
                    splashscreen =8
                    Wolf18.score = 0
                    Wolf19.score = 0
                    Wolf20.score = 0
                    maplevel = 0
                    fin = 0
                    end = 0
                    numnade =4
                    ball.x = 0
                    ball.y =600
            if event.key == K_8:
                if maplevel == 1 and levelcomplete >= 7  :
                    splashscreen =9
                    Wolf10.score = 0
                    Wolf13.score = 0
                    Wolf11.score = 0
                    Wolf12.score = 0
                    maplevel = 0
                    fin = 0
                    end = 0
                    numnade =6
                    ball.x = 0
                    ball.y =600
            
                    
        elif event.type == KEYUP and splashscreen > 1 :
            if event.key == K_SPACE :
                expo = 0
                ball.x = 0
                ball.y =600
                c = 300
                ball.speed= 0
            
            if event.key == K_s :
                radar = 0
                c = 300
    if selected_ball:
        (mouseX, mouseY) = pygame.mouse.get_pos()
        dx = mouseX - selected_ball.x
        dy = mouseY - selected_ball.y
        selected_ball.angle = 0.5*math.pi + math.atan2(dy, dx)
        selected_ball.speed = math.hypot(dx, dy) * 0.1
    
        
    if splashscreen == 0:
        screen.blit(pygame.transform.scale( bimg, rez), (0,0))
        screen.blit(pygame.transform.scale( blood, rez), (0,0))

    
    if splashscreen == 1:
        
        screen.blit(pygame.transform.scale( bimg, rez), (0,0))
        screen.blit(pygame.transform.scale( start, (300,120)), (420 , 300))
        screen.blit(pygame.transform.scale( prodigy, (450,300)), (-10 , 200))
        screen.blit(pygame.transform.scale( logo, (100,100)), (1200 , 500))
        text("B", 70,"none", red, 900,360)
        text("O", 70,"none", red, 900,400)
        text("U", 70,"none", red, 900,440)
        text("N", 70,"none", red, 900,480)
        text("S", 70,"none", red, 900,520)
        text("levels", 100,"none", red, 450,400)
        text("Instructions", 60,"none", red, 450,470)
        text("Credits", 60,"none", red, 450,520)
        text("By: Sohail Hameed and ", 25,"none", red, 1020,550)
        text("Ahamed Azeemuddin", 25,"none", red, 1020,565)
        bsound.play()
        text("press space for start", 25,"none", red, 0,520)
        text("press l for levels", 25,"none", red, 0,535)
        text("press i for instructions", 25,"none", red, 0,550)
        text("press c for credits", 25,"none", red, 0,565)
        text("press b for bonuse", 25,"none", red, 0,580)
    if splashscreen >1:
         bsound.stop()
    if splashscreen == 2:
        g1 = -20
        g2 = 0
            
        screen.fill(background_colour)
        pygame.draw.circle(screen, yellow, (1300, 0), 50, 0)
        for i in range(100):
            pygame.draw.polygon(screen,green,[(g1,600), (g2,590), (g2,600)],10)
            g1 += 20
            g2 += 20
        kill1 = enemey_kill(800, 500, ball.x, ball.y, ball.size,expo)
        
        
        Wolf1.enemeys(kill1)
        
        for ball in my_balls:
            if numnade > 0:
                ball.display()
            if expo == 1 :
                screen.blit(pygame.transform.scale(explosion, exposize), (ball.x - 100 , ball.y - 100))
            ball.move()
            ball.bounce()
            if expo == 0 and numnade > 0:
                screen.blit(pygame.transform.scale(nade, (50,50)), (ball.x - 25 , ball.y - 25))
               
        score_1 =  Wolf1.score 
        
        score_2 = Wolf1.score + Wolf3.score + numnade
        Sprite2.render(True)
        ball.render(600,450,50,150)
        if radar == 1:
            screen.fill(black)
            pygame.draw.circle(screen, green, (int(ball.x), int(ball.y)), 18, 0)
        text(score_1, 40,"none", red, 100,0)
        text("kills:", 40,"none", red, 0,0)
        text("garnades:", 40,"none", red, 150,0)
        text(numnade, 40,"none", red, 300,0)
        
        if score_1 == 1  :
            text("press C", 40,"none", red, 50,550)
            end = 1
            if levelcomplete < 1:
                levelcomplete = 1
        elif numnade <= 0:
            text("press C", 40,"none", red, 50,550)
            end = 2
        if fin == 1:
            screen.fill(puase_colour)
            text("Service Records", 150,"none", red, 250,0)         
            text("Next levels", 100,"none", red, 200,500)
            text("Score:", 100,"none", red, 450,100)
            text(score_2, 100,"none", red, 700,100)
            text("# of kills:", 100,"none", red, 400,170)
            text(score_1, 100,"none", red, 700,170)
            text("mouses earned ", 100,"none", red, 380,250)
            if score_2 == 3:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (830 , 350))
            if score_2 ==2:
                screen.blit(pygame.transform.scale( arrow, (100,100)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (100,100)), (600 , 350))
            if score_2==1:
                screen.blit(pygame.transform.scale( arrow, (100,100)), (350 , 350))
            text("Restart", 100,"none", red, 600,500)
            text("Home", 100,"none", red, 900,500)
            text("press n for nextlevel", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)
    

        if fin == 2:
            screen.fill(white)
            screen.blit(pygame.transform.scale( blood, rez), (0,0))
            text("Rest In Pices", 200,"none", red, 350,100)
            text("levels", 100,"none", red, 550,400)
            text("Restart", 100,"none", red, 520,300)
            text("Home", 100,"none", red, 550,500)
            text("press l for level", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)
    
    if splashscreen == 3:
        g1 = -20
        g2 = 0
        screen.fill(background_colour)
        pygame.draw.circle(screen, yellow, (1300, 0), 50, 0)
        for i in range(100):
            pygame.draw.polygon(screen,green,[(g1,600), (g2,590), (g2,600)],10)
            g1 += 20
            g2 += 20
        
        
        kill1 = enemey_kill(800, 100, ball.x, ball.y, ball.size,expo)
        kill2 = enemey_kill(Wolf5.x, Wolf5.y, ball.x, ball.y, ball.size,expo)
        Wolf2.enemeys(kill1)
        Wolf5.enemeys(kill2)
        for ball in my_balls:
            if numnade > 0:
                ball.display()
            if expo == 1 :
                screen.blit(pygame.transform.scale(explosion, exposize), (ball.x - 100 , ball.y - 100))
            ball.move()
            ball.bounce()
            if expo == 0 and numnade > 0:
                screen.blit(pygame.transform.scale(nade, (50,50)), (ball.x - 25 , ball.y - 25))
               
        
            
            
            
        ball.render(600,300,1000,100)
        

          
        score_1 = Wolf2.score + Wolf5.score 
        score_2 = Wolf2.score+numnade+Wolf5.score
        Sprite4.render(True)
        if radar == 1:
            screen.fill(black)
            pygame.draw.circle(screen, green, (int(ball.x), int(ball.y)), 18, 0)
        text(score_1, 40,"none", red, 100,0)
        text("kills:", 40,"none", red, 0,0)
        text("garnades:", 40,"none", red, 150,0)
        text(numnade, 40,"none", red, 300,0)
        
        if score_1 == 2  :
            text("press C", 40,"none", red, 50,550)
            end = 1
            if levelcomplete < 2:
                levelcomplete = 2
        elif numnade <= 0:
            text("press C", 40,"none", red, 50,550)
            end = 2
        if fin == 1:
            screen.fill(puase_colour)
            text("Service Records", 150,"none", red, 250,0)         
            text("Next levels", 100,"none", red, 200,500)
            text("Score:", 100,"none", red, 450,100)
            text(score_2, 100,"none", red, 700,100)
            text("# of kills:", 100,"none", red, 400,170)
            text(score_1, 100,"none", red, 700,170)
            text("mouses earned ", 100,"none", red, 380,250)
            if score_2 == 3:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (830 , 350))
            if score_2 ==2:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
            text("Restart", 100,"none", red, 600,500)
            text("Home", 100,"none", red, 900,500)
            text("press n for nextlevel", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)
    

        if fin == 2:
            screen.fill(white)
            screen.blit(pygame.transform.scale( blood, rez), (0,0))
            text("Rest In Pices", 200,"none", red, 350,100)
            text("levels", 100,"none", red, 550,400)
            text("Restart", 100,"none", red, 520,300)
            text("Home", 100,"none", red, 550,500)
            text("press l for level", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)
    if splashscreen == 4:
                
        screen.fill(background_colour)
        pygame.draw.circle(screen, yellow, (1300, 0), 50, 0)
        for i in range(100):
            pygame.draw.polygon(screen,green,[(g1,600), (g2,590), (g2,600)],10)
            g1 += 20
            g2 += 20
        kill2 = enemey_kill(800, 500, ball.x, ball.y, ball.size,expo)
        
        
        Wolf3.enemeys(kill2)
        for ball in my_balls:
            if numnade > 0:
                ball.display()
            if expo == 1 :
                screen.blit(pygame.transform.scale(explosion, exposize), (ball.x - 100 , ball.y - 100))
            ball.move()
            ball.bounce()
            if expo == 0 and numnade > 0:
                screen.blit(pygame.transform.scale(nade, (50,50)), (ball.x - 25 , ball.y - 25))
               
        
            
            
            
        
        ball.render(400,500,100,100)
        ball.render(600,500,100,100)
        ball.render(800,500,100,100)

        radarcount =0  
        score_1 = Wolf3.score 
        score_2 = Wolf3.score+numnade
        Sprite3.render(True)
        Sprite5.render(True)
        Sprite6.render(True)
        
        if radar == 1:
            screen.fill(black)
            radarcount += 1
            pygame.draw.circle(screen, green, (int(ball.x), int(ball.y)), 18, 0)
            if Wolf3.score == 0 :
                Wolf3.enemeys(kill2)
                
        text(score_1, 40,"none", red, 100,0)
        text("kills:", 40,"none", red, 0,0)
        text("garnades:", 40,"none", red, 150,0)
        text(numnade, 40,"none", red, 300,0)
        
        if score_1 == 1  :
            text("press C", 40,"none", red, 50,550)
            end = 1
            if levelcomplete < 3:
                levelcomplete = 3
        elif numnade <= 0:
            text("press C", 40,"none", red, 50,550)
            end = 2
        if fin == 1:
            screen.fill(puase_colour)
            text("Service Records", 150,"none", red, 250,0)         
            text("Next levels", 100,"none", red, 200,500)
            text("Score:", 100,"none", red, 450,100)
            text(score_2, 100,"none", red, 700,100)
            text("# of kills:", 100,"none", red, 400,170)
            text(score_1, 100,"none", red, 700,170)
            text("mouses earned ", 100,"none", red, 380,250)
            if score_2 == 2:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (830 , 350))
            if score_2 ==1:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
            if score_2==0:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
            
            text("Restart", 100,"none", red, 600,500)
            text("Home", 100,"none", red, 900,500)
            text("press n for nextlevel", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)
    

        if fin == 2:
            screen.fill(white)
            screen.blit(pygame.transform.scale( blood, rez), (0,0))
            text("Rest In Pices", 200,"none", red, 350,100)
            text("levels", 100,"none", red, 550,400)
            text("Restart", 100,"none", red, 520,300)
            text("Home", 100,"none", red, 550,500)
            text("press l for level", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)
    
    if splashscreen == 5:
        g1 =0
        g2 =20
        screen.fill(background_colour)
        pygame.draw.circle(screen, yellow, (1300, 0), 50, 0)
        for i in range(100):
            pygame.draw.polygon(screen,green,[(g1,600), (g2,590), (g2,600)],10)
            g1 += 20
            g2 += 20
        kill2 = enemey_kill(900, 200, ball.x, ball.y, ball.size,expo)
        
        
        Wolf4.enemeys(kill2)
        for ball in my_balls:
            if numnade > 0:
                ball.display()
            if expo == 1 :
                screen.blit(pygame.transform.scale(explosion, exposize), (ball.x - 100 , ball.y - 100))
            ball.move()
            ball.bounce()
            if expo == 0 and numnade > 0:
                screen.blit(pygame.transform.scale(nade, (50,50)), (ball.x - 25 , ball.y - 25))
               
        moveint = -50
        

            
        ball.render(600,300,1000,100)
        ball.render(640,0,10,300)
        ball.render(640,300,10,300)
        if ball.x >= 600 -ball.size and ball.x <= 620 and ball.y > 300 and ball.y < 600:
            ball.y = 0
            ball.x = 680
        if ball.x >= 600 -ball.size and ball.x <= 620 and ball.y < 300 :
            ball.y =500
            ball.x = 680 
        score_1 = Wolf4.score 
        score_2 = Wolf4.score+numnade
        Sprite4.render(True)
        if radar == 1:
            screen.fill(black)
            pygame.draw.circle(screen, green, (int(ball.x), int(ball.y)), 18, 0)
            pygame.draw.rect(screen,green,(640,300,10,300),1)
            pygame.draw.rect(screen,green,(640,0,10,300),1)
        text(score_1, 40,"none", red, 100,0)
        text("kills:", 40,"none", red, 0,0)
        text("garnades:", 40,"none", red, 150,0)
        text(numnade, 40,"none", red, 300,0)
        
        if score_1 == 1  :
            text("press C", 40,"none", red, 50,550)
            end = 1
            if levelcomplete < 4:
                levelcomplete = 4
        elif numnade <= 0:
            text("press C", 40,"none", red, 50,550)
            end = 2
        if fin == 1:
            screen.fill(puase_colour)
            text("Service Records", 150,"none", red, 250,0)         
            text("Next levels", 100,"none", red, 200,500)
            text("Score:", 100,"none", red, 450,100)
            text(score_2, 100,"none", red, 700,100)
            text("# of kills:", 100,"none", red, 400,170)
            text(score_1, 100,"none", red, 700,170)
            text("mouses earned ", 100,"none", red, 380,250)
            if score_2 == 3:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (830 , 350))
            if score_2 ==2:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
            if score_2==1:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
            text("Restart", 100,"none", red, 600,500)
            text("Home", 100,"none", red, 900,500)
            text("press n for nextlevel", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)
    

        if fin == 2:
            screen.fill(white)
            screen.blit(pygame.transform.scale( blood, rez), (0,0))
            text("Rest In Pices", 200,"none", red, 350,150)
            text("levels", 100,"none", red, 550,400)
            text("Restart", 100,"none", red, 520,300)
            text("Home", 100,"none", red, 550,500)
            text("press l for level", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)
    
    if splashscreen == 6:
        
        g1 =0
        g2 =20
        screen.fill(background_colour)
        
        pygame.draw.circle(screen, yellow, (1300, 0), 50, 0)
        for i in range(100):
            pygame.draw.polygon(screen,green,[(g1,600), (g2,590), (g2,600)],10)
            g1 += 20
            g2 += 20
        kill2 = enemey_kill(1100, 500, ball.x, ball.y, ball.size,expo)
        kill1 = enemey_kill(880, 500, ball.x, ball.y, ball.size,expo)
        kill3 = enemey_kill(680, 500, ball.x, ball.y, ball.size,expo)
        
        screen.blit(pygame.transform.scale(plane, (400,150)), ( 100, 490))
        
        Wolf6.enemeys(kill2)
        Wolf7.enemeys(kill3)
        Wolf8.enemeys(kill1)
        for ball in my_balls:
            if numnade > 0:
                ball.display()
            if expo == 1 :
                screen.blit(pygame.transform.scale(explosion, exposize), (ball.x - 100 , ball.y - 100))
            ball.move()
            ball.bounce()
            if expo == 0 and numnade > 0:
                screen.blit(pygame.transform.scale(nade, (50,50)), (ball.x - 25 , ball.y - 25))
        

            
        ball.render(600,200,50,400)
        ball.render(800,200,50,400)
        ball.render(1000,200,50,400)
        score_1 = Wolf6.score + Wolf7.score + Wolf8.score
        score_2 = Wolf6.score+numnade+ Wolf7.score + Wolf8.score
        Sprite10.render(True)
        Sprite9.render(True)
        Sprite7.render(True)
        if radar == 1:
            screen.fill(black)
            pygame.draw.circle(screen, green, (int(ball.x), int(ball.y)), 18, 0)
        text(score_1, 40,"none", red, 100,0)
        text("kills:", 40,"none", red, 0,0)
        text("garnades:", 40,"none", red, 150,0)
        text(numnade, 40,"none", red, 300,0)
        
        if score_1 == 3  :
            text("press C", 40,"none", red, 50,550)
            end = 1
            if levelcomplete < 5:
                levelcomplete = 5
        elif numnade <= 0:
            text("press C", 40,"none", red, 50,550)
            end = 2
        if fin == 1:
            screen.fill(puase_colour)
            text("Service Records", 150,"none", red, 250,0)         
            text("Next levels", 100,"none", red, 200,500)
            text("Score:", 100,"none", red, 450,100)
            text(score_2, 100,"none", red, 700,100)
            text("# of kills:", 100,"none", red, 400,170)
            text(score_1, 100,"none", red, 700,170)
            text("mouses earned ", 100,"none", red, 380,250)
            if score_2 == 5:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (830 , 350))
            if score_2 ==4:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
            if score_2==3:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
            text("Restart", 100,"none", red, 600,500)
            text("Home", 100,"none", red, 900,500)
            text("press n for nextlevel", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)
    

        if fin == 2:
            screen.fill(white)
            screen.blit(pygame.transform.scale( blood, rez), (0,0))
            text("Rest In Pices", 200,"none", red, 350,150)
            text("levels", 100,"none", red, 550,400)
            text("Restart", 100,"none", red, 520,300)
            text("Home", 100,"none", red, 550,500)
            text("press l for level", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)
    
    if splashscreen == 7:
        
        g1 =0
        g2 =20
        screen.fill(background_colour)
        
        pygame.draw.circle(screen, yellow, (1300, 0), 50, 0)
        for i in range(100):
            pygame.draw.polygon(screen,green,[(g1,600), (g2,590), (g2,600)],10)
            g1 += 20
            g2 += 20
        kill2 = enemey_kill(1100, 500, ball.x, ball.y, ball.size,expo)
        kill1 = enemey_kill(880, 500, ball.x, ball.y, ball.size,expo)
        kill3 = enemey_kill(1200, 0, ball.x, ball.y, ball.size,expo)
        
        screen.blit(pygame.transform.scale(plane, (400,150)), ( 100, 490))
        
        Wolf6.enemeys(kill2)
        Wolf9.enemeys(kill3)
        
        for ball in my_balls:
            if numnade > 0:
                ball.display()
            if expo == 1 :
                screen.blit(pygame.transform.scale(explosion, exposize), (ball.x - 100 , ball.y - 100))
            ball.move()
            ball.bounce()
            if expo == 0 and numnade > 0:
                screen.blit(pygame.transform.scale(nade, (50,50)), (ball.x - 25 , ball.y - 25))
        

            
        ball.render(600,400,580,50)
        ball.render(600,100,630,50)
        ball.render(600,450,50,150)
        score_1 = Wolf6.score + Wolf9.score
        score_2 = Wolf6.score+numnade+ Wolf9.score
        Sprite12.render(True)
        Sprite11.render(True)
        Sprite8.render(True)

        if ball.x >= 1000  and ball.x <= 1100 and ball.y < 100:
            ball.y = 400
            ball.x = 1250
        if ball.x >= 900 -ball.size and ball.x <= 950 and ball.y > 450:
            ball.y =0
            ball.x = 1280 
        if radar == 1:
            screen.fill(black)
            pygame.draw.circle(screen, green, (int(ball.x), int(ball.y)), 18, 0)
        text(score_1, 40,"none", red, 100,0)
        text("kills:", 40,"none", red, 0,0)
        text("garnades:", 40,"none", red, 150,0)
        text(numnade, 40,"none", red, 300,0)
        
        if score_1 == 2  :
            text("press C", 40,"none", red, 50,550)
            end = 1
            if levelcomplete < 6:
                levelcomplete = 6
        elif numnade <= 0:
            text("press C", 40,"none", red, 50,550)
            end = 2
        if fin == 1:
            screen.fill(puase_colour)
            text("Service Records", 150,"none", red, 250,0)         
            text("Next levels", 100,"none", red, 200,500)
            text("Score:", 100,"none", red, 450,100)
            text(score_2, 100,"none", red, 700,100)
            text("# of kills:", 100,"none", red, 400,170)
            text(score_1, 100,"none", red, 700,170)
            text("mouses earned ", 100,"none", red, 380,250)
            if score_2 == 4:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (830 , 350))
            if score_2 ==3:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
            if score_2==2:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
            text("Restart", 100,"none", red, 600,500)
            text("Home", 100,"none", red, 900,500)
            text("press n for nextlevel", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)
    

        if fin == 2:
            screen.fill(white)
            screen.blit(pygame.transform.scale( blood, rez), (0,0))
            text("Rest In Pices", 200,"none", red, 350,150)
            text("levels", 100,"none", red, 550,400)
            text("Restart", 100,"none", red, 520,300)
            text("Home", 100,"none", red, 550,500)
            text("press l for level", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)

    if splashscreen == 9:
        
        g1 =0
        g2 =20
        screen.fill(background_colour)
        
        pygame.draw.circle(screen, yellow, (1300, 0), 50, 0)
        for i in range(100):
            pygame.draw.polygon(screen,green,[(g1,600), (g2,590), (g2,600)],10)
            g1 += 20
            g2 += 20
        kill2 = enemey_kill(Wolf13.x, Wolf13.y, ball.x, ball.y, ball.size,expo)
        kill1 = enemey_kill(Wolf10.x, Wolf10.y, ball.x, ball.y, ball.size,expo)
        kill3 = enemey_kill(Wolf11.x, Wolf11.y, ball.x, ball.y, ball.size,expo)
        kill4 = enemey_kill(Wolf12.x, Wolf12.y, ball.x, ball.y, ball.size,expo)
        
        screen.blit(pygame.transform.scale(plane, (400,150)), ( 100, 490))
        
        Wolf10.enemeys(kill1)
        Wolf13.enemeys(kill2)
        Wolf11.enemeys(kill3)
        Wolf12.enemeys(kill4)
        for ball in my_balls:
            if numnade > 0:
                ball.display()
            if expo == 1 :
                screen.blit(pygame.transform.scale(explosion, exposize), (ball.x - 100 , ball.y - 100))
            ball.move()
            ball.bounce()
            if expo == 0 and numnade > 0:
                screen.blit(pygame.transform.scale(nade, (50,50)), (ball.x - 25 , ball.y - 25))
        

            
        ball.render(600,280,200,50)
        ball.render(850,100,150,50)
        ball.render(1100,280,200,50)
        ball.render(850,400,150,50)
        ball.render(600,0,50,500)
                   
        score_1 = Wolf10.score + Wolf13.score+Wolf11.score + Wolf12.score
        score_2 = Wolf10.score+numnade+ Wolf13.score+Wolf11.score + Wolf12.score
            
        Sprite17.render(True)
        Sprite18.render(True)
        Sprite19.render(True)
        Sprite20.render(True)
        Sprite21.render(True)
        Sprite22.render(True)
        Sprite23.render(True)
            

        if ball.x >= 580  and ball.x <= 610 and ball.y > 500:
            ball.y = 0
            ball.x = 670
        if ball.x >= 615  and ball.x <= 640 and ball.y > 500:
            ball.y = 550
            ball.x = 550
            
        if radar == 1:
            screen.fill(black)
            Sprite15.render(True)
            Sprite14.render(True)
            Sprite13.render(True)
            Sprite16.render(True)
            if Wolf10.score == 0 :
                Wolf10.enemeys(kill1)
            if Wolf11.score == 0 :
                Wolf11.enemeys(kill3)
            if Wolf12.score == 0 :
                Wolf12.enemeys(kill4)
            if Wolf13.score == 0 :
                Wolf13.enemeys(kill2)
            pygame.draw.circle(screen, green, (int(ball.x), int(ball.y)), 18, 0)
        text(score_1, 40,"none", red, 100,0)
        text("kills:", 40,"none", red, 0,0)
        text("garnades:", 40,"none", red, 150,0)
        text(numnade, 40,"none", red, 300,0)
        
        if score_1 == 4 :
            text("press C", 40,"none", red, 50,550)
            end = 1
            if levelcomplete < 8:
                levelcomplete = 8
        elif numnade <= 0:
            text("press C", 40,"none", red, 50,550)
            end = 2
        if fin == 1:
            screen.fill(puase_colour)
            text("Service Records", 150,"none", red, 250,0)         
            text("Next levels", 100,"none", red, 200,500)
            text("Score:", 100,"none", red, 450,100)
            text(score_2, 100,"none", red, 700,100)
            text("# of kills:", 100,"none", red, 400,170)
            text(score_1, 100,"none", red, 700,170)
            text("mouses earned ", 100,"none", red, 380,250)
            if score_2 == 4:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (830 , 350))
            if score_2 ==3:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
            if score_2==2:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
            text("Restart", 100,"none", red, 600,500)
            text("Home", 100,"none", red, 900,500)
            text("press n for nextlevel", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)
    

        if fin == 2:
            screen.fill(white)
            screen.blit(pygame.transform.scale( blood, rez), (0,0))
            text("Rest In Pices", 200,"none", red, 350,150)
            text("levels", 100,"none", red, 550,400)
            text("Restart", 100,"none", red, 520,300)
            text("Home", 100,"none", red, 550,500)
            text("press l for level", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)
    
    if splashscreen == 8:
        
        g1 =0
        g2 =20
        screen.fill(background_colour)
        
        pygame.draw.circle(screen, yellow, (1300, 0), 50, 0)
        for i in range(100):
            pygame.draw.polygon(screen,green,[(g1,600), (g2,590), (g2,600)],10)
            g1 += 20
            g2 += 20
        kill2 = enemey_kill(Wolf19.x, Wolf19.y, ball.x, ball.y, ball.size,expo)
        kill1 = enemey_kill(Wolf18.x, Wolf18.y, ball.x, ball.y, ball.size,expo)
        kill3 = enemey_kill(Wolf20.x, Wolf20.y, ball.x, ball.y, ball.size,expo)
        
        screen.blit(pygame.transform.scale(plane, (400,150)), ( 100, 490))
        
        Wolf18.enemeys(kill1)
        Wolf19.enemeys(kill2)
        Wolf20.enemeys(kill3)
        for ball in my_balls:
            if numnade > 0:
                ball.display()
            if expo == 1 :
                screen.blit(pygame.transform.scale(explosion, exposize), (ball.x - 100 , ball.y - 100))
            ball.move()
            ball.bounce()
            if expo == 0 and numnade > 0:
                screen.blit(pygame.transform.scale(nade, (50,50)), (ball.x - 25 , ball.y - 25))
        

            
        ball.render(800,200,50,400)
        ball.render(800,250,300,20)
        ball.render(800,400,300,20)
                   
        score_1 = Wolf10.score + Wolf13.score+Wolf11.score + Wolf12.score
        score_2 = Wolf10.score+numnade+ Wolf13.score+Wolf11.score + Wolf12.score
            
        Sprite28.render(True)
        Sprite30.render(True)
        Sprite29.render(True)
            
            
        if radar == 1:
            screen.fill(black)
            if Wolf10.score == 0 :
                Wolf10.enemeys(kill1)
            pygame.draw.circle(screen, green, (int(ball.x), int(ball.y)), 18, 0)
        text(score_1, 40,"none", red, 100,0)
        text("kills:", 40,"none", red, 0,0)
        text("garnades:", 40,"none", red, 150,0)
        text(numnade, 40,"none", red, 300,0)
        
        if score_1 == 3 :
            text("press C", 40,"none", red, 50,550)
            end = 1
            if levelcomplete < 7:
                levelcomplete = 7
        elif numnade <= 0:
            text("press C", 40,"none", red, 50,550)
            end = 2
        if fin == 1:
            screen.fill(puase_colour)
            text("Service Records", 150,"none", red, 250,0)         
            text("Next levels", 100,"none", red, 200,500)
            text("Score:", 100,"none", red, 450,100)
            text(score_2, 100,"none", red, 700,100)
            text("# of kills:", 100,"none", red, 400,170)
            text(score_1, 100,"none", red, 700,170)
            text("mouses earned ", 100,"none", red, 380,250)
            if score_2 == 4:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (830 , 350))
            if score_2 ==3:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
            if score_2==2:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
            text("Restart", 100,"none", red, 600,500)
            text("Home", 100,"none", red, 900,500)
            text("press n for nextlevel", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)
    

        if fin == 2:
            screen.fill(white)
            screen.blit(pygame.transform.scale( blood, rez), (0,0))
            text("Rest In Pices", 200,"none", red, 350,150)
            text("levels", 100,"none", red, 550,400)
            text("Restart", 100,"none", red, 520,300)
            text("Home", 100,"none", red, 550,500)
            text("press l for level", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)
    if splashscreen == 10:
        
        g1 =0
            
        screen.fill(BLUE)
        
        pygame.draw.circle(screen, yellow, (1300, 0), 50, 0)
        for i in range(200):
            pygame.draw.circle(screen, yellow, (g1, 600), 10, 0)
            g1 += 10
        kill2 = enemey_kill(Wolf15.x, Wolf15.y, ball.x, ball.y, ball.size,expo)
        kill1 = enemey_kill(Wolf14.x, Wolf14.y, ball.x, ball.y, ball.size,expo)
        kill3 = enemey_kill(Wolf16.x, Wolf16.y, ball.x, ball.y, ball.size,expo)
        kill4 = enemey_kill(Wolf17.x, Wolf17.y, ball.x, ball.y, ball.size,expo)
        
        Wolf14.enemeys(kill1)
        Wolf15.enemeys(kill2)
        Wolf16.enemeys(kill3)
        Wolf17.enemeys(kill4)
        for ball in my_balls:
            if numnade > 0:
                ball.display()
            if expo == 1 :
                screen.blit(pygame.transform.scale(explosion, exposize), (ball.x - 100 , ball.y - 100))
            ball.move()
            ball.bounce()
            if expo == 0 and numnade > 0:
                screen.blit(pygame.transform.scale(nade, (50,50)), (ball.x - 25 , ball.y - 25))
        

            
        ball.render(700, 0, 150, 250)
        ball.render(700, 400, 150, 250)
        ball.render(1000, 400, 100, 250)
        ball.render(1200, 300, 250, 10)
        score_1 = Wolf14.score + Wolf15.score+Wolf16.score + Wolf17.score
        score_2 = Wolf14.score+numnade+ Wolf15.score+Wolf16.score + Wolf17.score
            
        Sprite24.render(True)
        Sprite25.render(True)
        Sprite26.render(True)
        Sprite27.render(True)

            
            
        if radar == 1:
            screen.fill(black)
            if Wolf15.score == 0 :
                Wolf15.enemeys(kill2)
                
            pygame.draw.circle(screen, green, (int(ball.x), int(ball.y)), 18, 0)
        text(score_1, 40,"none", red, 100,0)
        text("kills:", 40,"none", red, 0,0)
        text("garnades:", 40,"none", red, 150,0)
        text(numnade, 40,"none", red, 300,0)
        
        if score_1 == 4 :
            text("press C", 40,"none", red, 50,550)
            end = 1
            if levelcomplete < 9:
                levelcomplete = 9
        elif numnade <= 0:
            text("press C", 40,"none", red, 50,550)
            end = 2
        if fin == 1:
            screen.fill(puase_colour)
            text("Service Records", 150,"none", red, 250,0)         
            text("Next levels", 100,"none", red, 200,500)
            text("Score:", 100,"none", red, 450,100)
            text(score_2, 100,"none", red, 700,100)
            text("# of kills:", 100,"none", red, 400,170)
            text(score_1, 100,"none", red, 700,170)
            text("mouses earned ", 100,"none", red, 380,250)
            if score_2 == 5:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (830 , 350))
            if score_2 ==4:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
            if score_2==3:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
            text("Restart", 100,"none", red, 600,500)
            text("Home", 100,"none", red, 900,500)
            text("press n for nextlevel", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)
    

        if fin == 2:
            screen.fill(white)
            screen.blit(pygame.transform.scale( blood, rez), (0,0))
            text("Rest In Pices", 200,"none", red, 350,150)
            text("levels", 100,"none", red, 550,400)
            text("Restart", 100,"none", red, 520,300)
            text("Home", 100,"none", red, 550,500)
            text("press l for level", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)

    if splashscreen == 11:
        
        g1 =0
            
        screen.fill(BLUE)
        
        pygame.draw.circle(screen, yellow, (1300, 0), 50, 0)
        for i in range(200):
            pygame.draw.circle(screen, yellow, (g1, 600), 10, 0)
            g1 += 10
        kill1 = enemey_kill(Wolf21.x, Wolf21.y, ball.x, ball.y, ball.size,expo)
        kill2 = enemey_kill(Wolf22.x, Wolf22.y, ball.x, ball.y, ball.size,expo)
        kill3 = enemey_kill(Wolf23.x, Wolf23.y, ball.x, ball.y, ball.size,expo)
            
        
        Wolf21.enemeys(kill1)
        Wolf22.enemeys(kill2)
        Wolf23.enemeys(kill3)
        for ball in my_balls:
            if numnade > 0:
                ball.display()
            if expo == 1 :
                screen.blit(pygame.transform.scale(explosion, exposize), (ball.x - 100 , ball.y - 100))
            ball.move()
            ball.bounce()
            if expo == 0 and numnade > 0:
                screen.blit(pygame.transform.scale(nade, (50,50)), (ball.x - 25 , ball.y - 25))
            if ball.x >= 450  and ball.x <= 510 and ball.y >= 0 and ball.y <= 200 :
                ball.y = 500
                ball.x = 650
            if ball.x >= 450  and ball.x <= 510 and ball.y <= 400 and ball.y >= 200 :
                ball.y = 100
                ball.x = 650
            if ball.x >= 480  and ball.x <= 510 and ball.y >= 400 and ball.y <= 600 :
                ball.y = 300
                ball.x = 650

                
            
        ball.render(500, 0, 75, 600)
        ball.render(500, 400, 300, 40)
        ball.render(500, 200, 300, 40)
        ball.render(800, 0, 75, 600)
        score_1 = Wolf21.score + Wolf22.score+Wolf23.score 
        score_2 = numnade+ Wolf21.score+Wolf22.score + Wolf23.score
            
        Sprite33.render(True)
        Sprite34.render(True)
        Sprite35.render(True)
        Sprite36.render(True)

            
        if radar == 1:
            screen.fill(black)
            if Wolf15.score == 0 :
                Wolf15.enemeys(kill2)
                
            pygame.draw.circle(screen, green, (int(ball.x), int(ball.y)), 18, 0)
        text(score_1, 40,"none", red, 100,0)
        text("kills:", 40,"none", red, 0,0)
        text("garnades:", 40,"none", red, 150,0)
        text(numnade, 40,"none", red, 300,0)
        
        if score_1 == 3 :
            text("press C", 40,"none", red, 50,550)
            end = 1
            if levelcomplete < 10:
                levelcomplete = 10
        elif numnade <= 0:
            text("press C", 40,"none", red, 50,550)
            end = 2
        if fin == 1:
            screen.fill(puase_colour)
            text("Service Records", 150,"none", red, 250,0)         
            text("Next levels", 100,"none", red, 200,500)
            text("Score:", 100,"none", red, 450,100)
            text(score_2, 100,"none", red, 700,100)
            text("# of kills:", 100,"none", red, 400,170)
            text(score_1, 100,"none", red, 700,170)
            text("mouses earned ", 100,"none", red, 380,250)
            if score_2 == 3:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (830 , 350))
            if score_2 ==2:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
                screen.blit(pygame.transform.scale( arrow, (150,150)), (600 , 350))
            if score_2==1:
                screen.blit(pygame.transform.scale( arrow, (150,150)), (350 , 350))
            text("Restart", 100,"none", red, 600,500)
            text("Home", 100,"none", red, 900,500)
            text("press n for nextlevel", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)
    

        if fin == 2:
            screen.fill(white)
            screen.blit(pygame.transform.scale( blood, rez), (0,0))
            text("Rest In Pices", 200,"none", red, 350,150)
            text("levels", 100,"none", red, 550,400)
            text("Restart", 100,"none", red, 520,300)
            text("Home", 100,"none", red, 550,500)
            text("press l for level", 25,"none", red, 0,550)
            text("press r for restart", 25,"none", red, 0,565)
            text("press h for home", 25,"none", red, 0,580)
    if splashscreen == 12:
   
        screen.fill(white)
        screen.blit(pygame.transform.scale( blood, rez), (0,0))
        text("Rest In Pices", 200,"none", red, 250,250)
        text("this game has no end ", 150,"none", red, 50,400)
        text(" play agian", 100,"none", red, 300,500)
            
    if puase == 1:
          
        screen.fill(puase_colour)
        text("Pause", 200,"none", red, 450,0)         
        text("levels", 100,"none", red, 550,250)
        text("Restart", 100,"none", red, 530,150)
        text("instructions", 100,"none", red, 450,350)
        text("Home", 100,"none", red, 560,450)
        text("press p to continue ", 25,"none", red, 0,520)
        text("press l for levels", 25,"none", red, 0,535)
        text("press i for instructions", 25,"none", red, 0,550)
        text("press r for restart", 25,"none", red, 0,565)
        text("press h for Home", 25,"none", red, 0,580)
    if intro == 1:
        screen.blit(pygame.transform.scale( in1, rez), (0,0))
        bsound.stop()
        screen.blit(pygame.transform.scale( nade, (50,50)), (100 , 100))
        screen.blit(pygame.transform.scale( arrow, (50,50)), (110 , 110))
        
        text("click and drag the garnade around to move it ", 25,"none", red, 100,520)
        text("use arrow keys to change the pages", 25,"none", red, 900,520)
    if intro == 2:
        screen.blit(pygame.transform.scale( in2, rez), (0,0))
        bsound.stop()
        pygame.draw.rect(screen,red,(400,0,2,600),0)
        screen.blit(pygame.transform.scale( nade, (50,50)), (160 , 100))
        screen.blit(pygame.transform.scale( arrow, (50,50)), (110 , 110))
        text("flick the grande and release the click ", 25,"none", red, 0,500)
        text("to throw the grande ", 25,"none", red, 0,520)
        text("*** but remeber if the grandae is out of ", 25,"none", red, 0,540)
        text("your range(the red line) you can't pick it up", 25,"none", red, 0,560)
        text("and your coursur will be rest***", 25,"none", red, 0,580)
    if intro == 3:
        screen.blit(pygame.transform.scale( in3, rez), (0,0))
        bsound.stop()
        text("once the grande is out if your range you can press space to avtivate it ", 25,"none", red, 0,500)
        text("press p to puase", 25,"none", red, 0,520)
        text("press s for a sonar to show hiden objects", 25,"none", red, 0,540)
        text("press r for restart", 25,"none", red, 0,560)
    if intro == 4:
        screen.blit(pygame.transform.scale( in4, rez), (0,0))
        bsound.stop()
    if intro == 5:
        screen.blit(pygame.transform.scale( in5, rez), (0,0))
        bsound.stop()
        text("press s for a sonar to show hiden objects", 25,"none", red, 0,540)
    if maplevel == 1:
        screen.blit(pygame.transform.scale( lev, rez), (0,0))
        bsound.stop()
        text("press the # of the level you want to play ", 25,"none", red, 0,550)
        text("use arrow keys to change the map", 25,"none", red, 900,520)
    if maplevel == 2:
        screen.blit(pygame.transform.scale( lev2, rez), (0,0))
        bsound.stop()
    if creed == 1 :
        screen.blit(pygame.transform.scale( cred, rez), (0,0))
    
        
    pygame.display.flip()
    clock.tick(c)
    
pygame.quit()

