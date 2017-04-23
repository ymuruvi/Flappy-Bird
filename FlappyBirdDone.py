"""==================================Information==================================
 Name:      Flappy Bird
 Purpose:   Submission for ICS201 python summative
 Author:    Nano Muruvi
 Created:   18/05/2014
 Copyright: (c) Nano 2014
 Licence:   MIT Lisence
=================================Notes/ Checklist=================================
    -This game was written in versio 3.3.1 of the python programmign language.
    -This game was made using a set of modules from PyGame.
    -You can install pygame from the following website:
        http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame
=======================================TODO=======================================
    -Add Acceleration to the bird
    -Add rotation to the bird
=================================================================================="""

#Imports modules
import pygame, sys, math, random, time, datetime, os.path
from pygame.locals import *
from datetime import timedelta

#Initializes pygame
pygame.init()
fpsClock = pygame.time.Clock()

#Assigns the fps
fps = 60

#Assigns width and length of screen
screenWid = 750
screenLen = 500

#Makes the window
resolution = ( screenWid-300, screenLen)
pygame.display.set_caption('Flappy Bird')
pygame.display.init()
screen = pygame.display.set_mode((resolution))

#These are the colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)
lightTurquoise = (153,217,234)
bgColor = (lightTurquoise)

#These are the pictures of pipes.
topL = pygame.image.load('TopPipe2.png')
topM = pygame.image.load('TopPipe1.png')
topS = pygame.image.load('TopPipe3.png')
botL = pygame.image.load('BottomPipe2.png')
botM = pygame.image.load('BottomPipe1.png')
botS = pygame.image.load('BottomPipe3.png')

#Assigns bird's image and background image.
bird = pygame.image.load('FlappyBird.png')
bgImage = pygame.image.load('BackDrop.png')

#Assigns where the pipes start
col1Start = screenWid
col2Start = col1Start+277
col3Start = col2Start + 277

#Makes the pipe columns start off screen
col1X = col1Start
col2X = col2Start
col3X = col3Start

#Makes a random number to decide what combination of
#pipes to use so that the pipe combinations are random.
pipes1 = random.randint(1,3)
pipes2 = random.randint(1,3)
pipes3 = random.randint(1,3)

#Assigns the y coordinate of each pipe to 0.
#Will be reasigned once the game starts.
topPipe1Y = 0
botPipe1Y = 0
topPipe2Y = 0
botPipe2Y = 0
topPipe3Y = 0
botPipe3Y = 0

#Assigns text information
font = pygame.font.SysFont( " Comic Sans MS", 30)
font2 = pygame.font.SysFont(" Comic Sans MS, Arial", 60)
highScoreText = font.render("High Score:", True, black)
scoreBoard = font.render("Score:", True, black)
clickToPlay = font2.render("Click to Play!", True, red)
cTPC= 30,screenLen/2-40
scoreBoardPos = (5,5)
scorePos = (100,5)
score = 0
highScore = score

#Assigns the bird's information
birdx = 100
birdy = screenLen / 2
birdWid = 51
birdLen = 36

#Variables and information needed to add acceleration for the bird
"""The equation is y=(x-birdX)^2
For this to work I increment the accX every time the loop occurs"""
accX=0
y=birdy


#makes it so that the bird will not move originally
movement = 'none'
goingUp = 0

#Sets how fast the pipes will move down the screen.
orgSpeed = 2
speed = 0
changeInTime=1
velocityAccu=0
velocity=0

#When these tuples are true the player loses
c1x,c1y = False, False
c2x,c2y = False, False
c3x,c3y = False, False

def colidedY(birdY, topPipeY, botPipeY,cY):
    if birdY >= topPipeY and birdY+36<= botPipeY:
        colCo = False
    else:
        colCo = True
def colidedX(birdX, colCo, cX):
    if (birdx >= col1X and birdx <= col1X + 84 )or (birdx + 51 >= col1X and birdx + 51 <= col1X + 84):
        c1x = True
    else:
        c1x = False
def colidedXY(cX, cY, score, highScore):
    if cX and cY:
        movement = 'none'
        birdy = int(screenLen/2)
        if score > highScore:
            highScore = score
            score = 0
            speed = 0
            col1X = col1Start
            col2X = col2Start
            col3X = col3Start
            pipes1 = random.randint(1,3)
            pipes2 = random.randint(1,3)
            pipes3 = random.randint(1,3)
            newGame = True
            clickAgain = 1
            movement = 'none'

#Makes it so that the new game happenings occur
newGame = True
clickAgain = 1

#Assigns some numbers to variables to avoid a tuple error.
two = 215
three = 315
four = 415

#Stats Stuff
clicks = 0
framesCompleted = 0
"""================================Main Game Loop================================="""
while True:

#Resets the pipes if they go beyond the screen.
    if col1X <= -82:
        col1X = screenWid
        pipes1 = random.randint(1,3)
    if col2X <= -82:
        col2X = screenWid
        pipes2 = random.randint(1,3)
    if col3X <= -82:
        col3X = screenWid
        pipes3 = random.randint(1,3)

#Moves the pipes depending on the speed.
    col1X-=speed
    col2X-=speed
    col3X-=speed

#Gets the information on the score and the highest score for later use.
    scoreAmount = font.render(str(score),True, black)
    highScoreNum = font.render(str(highScore),True, black)

#Draws the background of the screen.
    screen.fill(bgColor)
    screen.blit(bgImage,(0,0))

#Increments variables needed for acceleration to occur properly
    accX+=1

#------------------------------Takes in input types-------------------------------
    for event in pygame.event.get():

#If a mouse button is clicked the bird flaps up.
        if event.type == MOUSEBUTTONDOWN:
            clicks+=1
            if clickAgain >0 :
                clickAgain-=1
            else:
                speed = orgSpeed
                changeInTime=0
                goingUp+=10
                if goingUp > 30:
                    goingUp = 30
                movement = 'up'
                newGame = False
#This can be turned on for testing to make sure
#colission detection is working by removing the "#"'s
        #if event.type == MOUSEMOTION:
            #mousepos = pygame.mouse.get_pos()
            #birdx,birdy = mousepos
            #movement = 'none'

##Required for closing game
#This makes it so that if the window's close button is
#clicked it doesn't temporarily break the computer.
        if event.type == QUIT:
            print("High Score:",highScore)
            print("Clicks:",clicks)
            print("Frames Completed:",framesCompleted)
            print("========Game Over========")
            pygame.quit()
            sys.exit()

#---------------------------------Bird's Physics----------------------------------
#Makes it so that the bird falls down after going up a bit.
    if movement == 'up':
        if birdy <= 0:
            birdy = 2
            goingUp = 0
            movement = 'down'
            velocity=0
            changeInTime=0
            velocityAccu=0
        birdy-=4
        goingUp-=1
        if goingUp == 0:
            movement = 'down'
            goingUp = 0

#Makes it so that the bird accelerates down
    if movement == 'down':
        changeInTime +=0.4
        birdy+=changeInTime

#If the bird falls to the ground  the game restarts
        if birdy >= screenLen or birdy+36 >= screenLen:
            movement = 'none'
            birdy = int(screenLen/2)
            if score > highScore:
                highScore = score
            score = 0
            speed = 0
            col1X = col1Start
            col2X = col2Start
            col3X = col3Start
            pipes1 = random.randint(1,3)
            pipes2 = random.randint(1,3)
            pipes3 = random.randint(1,3)
            newGame = True
            clickAgain = 1
            movement = 'none'

#------------------------------Colission Conditions-------------------------------

#This part detects colissions.
##I tried to use a function for this part to make it simpler,
##but I kept having issues so I duplicated some if statements.

##Pipe 1 colission detection
    colidedY(birdy, topPipe1Y, botPipe1Y, c1y)
    colidedX(birdx, col1X, c1x)
    colidedXY(c1x,c1y,score,highScore)

    colidedY(birdy, topPipe2Y, botPipe2Y, c2y)
    colidedX(birdx, col2X, c2x)
    colidedXY(c2x,c2y,score,highScore)

    colidedY(birdy, topPipe3Y, botPipe3Y, c3y)
    colidedX(birdx, col3X, c3x)
    colidedXY(c3x,c3y,score,highScore)
    if birdy >= topPipe1Y and birdy+36<= botPipe1Y:
        c1y = False
    else:
        c1y = True
    if (birdx >= col1X and birdx <= col1X + 84 )or (birdx + 51 >= col1X and birdx + 51 <= col1X + 84):
        c1x = True
    else:
        c1x = False

    if c1y and c1x :
        movement = 'none'
        birdy = int(screenLen/2)
        if score > highScore:
            highScore = score
        score = 0
        speed = 0
        col1X = col1Start
        col2X = col2Start
        col3X = col3Start
        pipes1 = random.randint(1,3)
        pipes2 = random.randint(1,3)
        pipes3 = random.randint(1,3)
        newGame = True
        clickAgain = 1
        movement = 'none'
##Pipe 2 colission detection
    if birdy >= topPipe2Y and birdy+36<= botPipe2Y:
        c2y = False
    else:
        c2y = True
    if (birdx >= col2X and birdx <= col2X + 84 )or (birdx + 51 >= col2X and birdx + 51 <= col2X + 84):
        c2x = True
    else:
        c2x = False

    if c2y and c2x :
        movement = 'none'
        birdy = int(screenLen/2)
        if score > highScore:
            highScore = score
        score = 0
        speed = 0
        col1X = col1Start
        col2X = col2Start
        col3X = col3Start
        pipes1 = random.randint(1,3)
        pipes2 = random.randint(1,3)
        pipes3 = random.randint(1,3)
        newGame = True
        clickAgain = 1
        movement = 'none'

##Pipe 3 colission detection
    if birdy >= topPipe3Y and birdy+36<= botPipe3Y:
        c3y = False
    else:
        c3y = True
    if (birdx >= col3X and birdx <= col3X + 84 )or (birdx + 51 >= col3X and birdx + 51 <= col3X + 84):
        c3x = True
    else:
        c3x = False

    if c3y and c3x :
        movement = 'none'
        birdy = int(screenLen/2)
        if score > highScore:
            highScore = score
        score = 0
        speed = 0
        col1X = col1Start
        col2X = col2Start
        col3X = col3Start
        pipes1 = random.randint(1,3)
        pipes2 = random.randint(1,3)
        pipes3 = random.randint(1,3)
        newGame = True
        clickAgain = 1
        movement = 'none'

#-----------------------------------Draws Pipes-----------------------------------
#Takes the random number assigned to each pipes, depending on that, one of
#three possible pipe layouts are assigned to the corresponding pipe column.

##Pipes in comlumn 1
    if pipes1 == 1:
        topPipe1Y =285
        botPipe1Y =415
        screen.blit( topL, ( col1X, -15))
        screen.blit( botS, ( col1X, four))

    elif pipes1 == 2:
        topPipe1Y = 185
        botPipe1Y = 315
        screen.blit( topM, ( col1X, -15))
        screen.blit( botM, ( col1X, three))

    elif pipes1 == 3:
        topPipe1Y = 85
        botPipe1Y = 215
        screen.blit( topS, ( col1X, -15))
        screen.blit( botL, ( col1X, two))

##Pipes in comlumn 2
    if pipes2 == 1:
        topPipe2Y =285
        botPipe2Y =415
        screen.blit( topL, ( col2X, -15))
        screen.blit( botS, ( col2X, four))

    elif pipes2 == 2:
        topPipe2Y = 185
        botPipe2Y = 315
        screen.blit( topM, ( col2X, -15))
        screen.blit( botM, ( col2X, three))

    elif pipes2 == 3:
        topPipe2Y = 85
        botPipe2Y = 215
        screen.blit( topS, ( col2X, -15))
        screen.blit( botL, ( col2X, two))

##Pipe in comlumn 3
    if pipes3 == 1:
        topPipe3Y =285
        botPipe3Y =415
        screen.blit( topL, ( col3X, -15))
        screen.blit( botS, ( col3X, four))

    elif pipes3 == 2:
        topPipe3Y = 185
        botPipe3Y = 315
        screen.blit( topM, ( col3X, -15))
        screen.blit( botM, ( col3X, three))

    elif pipes3 == 3:
        topPipe3Y = 85
        botPipe3Y = 215
        screen.blit( topS, ( col3X, -15))
        screen.blit( botL, ( col3X, two))

#Draws the bird onto the screen
    screen.blit( bird, (birdx,birdy))

#Draws the text onto the screen
    screen.blit( scoreBoard, scoreBoardPos)
    screen.blit(scoreAmount, scorePos)
    screen.blit(highScoreText,(5,45))
    screen.blit(highScoreNum, (170,45))

#If it is a new game, a prompt is displayed  to click
    if newGame :
        screen.blit(clickToPlay,(cTPC))

#Each time the bird  goes into a pipe a point is added.
    if (birdx == col1X) or (birdx - 1 == col1X):
        score +=1
    elif (birdx == col2X) or (birdx - 1 == col2X):
        score +=1
    elif (birdx == col3X) or (birdx - 1 == col3X):
        score+=1

#Refreshes the screen
    pygame.display.update()
    fpsClock.tick(fps)
    framesCompleted+=1
