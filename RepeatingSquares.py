from random import *
import pygame

#instanciate a new window
pygame.init()
(width, height) = (300,300)

#set the width, height, and caption
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Repeating Squares")

#get the light and dark colors (red,green,blue,yellow)
blue = [0,0,255]
red = [255,0,0]
green = [0,255,0]
yellow = [255,255,0]

lightBlue = [135,206,250]
lightRed = [253,160,122]
lightGreen = [34,139,34]
lightYellow = [227,250,96]

colorSequence = list()
squareSequence = list()

def getSequence(color,colorSequence):
    if(color == lightBlue):
        colorSequence.append(lightBlue)
        squareSequence.append(TOPRIGHT)
    elif(color == lightRed):
        colorSequence.append(lightRed)
        squareSequence.append(TOPLEFT)
    elif(color == lightGreen):
        colorSequence.append(lightGreen)
        squareSequence.append(BOTLEFT)
    elif(color == lightYellow):
        colorSequence.append(lightYellow)
        squareSequence.append(BOTRIGHT)

#squares
TOPLEFT = [0,0,150,150]
TOPRIGHT = [149,0,150,150]
BOTLEFT = [0,150,150,150]
BOTRIGHT = [150,150,150,150]

def drawRect(color,position):
    pygame.draw.rect(screen,color,position,0)

def drawSquare(color,position):
    drawRect(color,position)
    pygame.display.update()
    getSequence(color,colorSequence)

def drawDefault():
    drawRect(red,TOPLEFT)
    drawRect(blue,TOPRIGHT)
    drawRect(green,BOTLEFT)
    drawRect(yellow,BOTRIGHT)

def getMousePos(x1,y1,x2,y2):
    mousePos = pygame.mouse.get_pos()
    return (mousePos[0] > x1 and mousePos[0] < y1 and mousePos[1] > x2 and mousePos[1] < y2)

def isMouseButtonDown():
    return event.type == pygame.MOUSEBUTTONDOWN

def userClick():
    if(isMouseButtonDown() and  getMousePos(0,150,0,150) ):
        drawSquare(lightRed,TOPLEFT)
    elif(isMouseButtonDown()and getMousePos(150,300,0,150) ):
        drawSquare(lightBlue,TOPRIGHT)
    elif(isMouseButtonDown() and getMousePos(0,150,150,300) ):
        drawSquare(lightGreen,BOTLEFT)
    elif(isMouseButtonDown() and getMousePos(150,300,150,300) ):
        drawSquare(lightYellow,BOTRIGHT)
    else:
        drawDefault()
        pygame.display.update()

drawDefault()
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #get the same square and color
        randomColor = [lightBlue,lightGreen,lightYellow,lightRed]
        squareLocation =[TOPRIGHT,BOTLEFT,BOTRIGHT,TOPLEFT]

        iterator = 0
        if(event.type == pygame.KEYDOWN):
           #when the user presses enter, start random pattern
           if(event.key == pygame.K_SPACE):
               while(iterator < 20):
                   square = randint(0,3)
                   drawSquare(randomColor[square],squareLocation[square])
                   drawDefault()
                   pygame.time.wait(1000)
                   iterator += 1
           elif(event.key == pygame.K_RETURN):
                for i in range(0,len(colorSequence)):
                   #store sequence
                   drawSquare(colorSequence[i],squareSequence[i])
                   pygame.time.wait(1000)
                   drawDefault()
                colorSequence = list()
                squareSequence = list()
                   
        #let user click on the square
        else:
           userClick()

        drawDefault()
