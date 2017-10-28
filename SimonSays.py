from random import *
import pygame

#instanciate a new window
pygame.init()
(width, height) = (300,300)

#set the width, height, and caption
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Simon Says")

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
computerColor = list()
computerSquare = list()

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

def getComputerSequence(color):
    if(color == lightBlue):
        computerColor.append(lightBlue)
        computerSquare.append(TOPRIGHT)
    elif(color == lightRed):
        computerColor.append(lightRed)
        computerSquare.append(TOPLEFT)
    elif(color == lightGreen):
        computerColor.append(lightGreen)
        computerSquare.append(BOTLEFT)
    elif(color == lightYellow):
        computerColor.append(lightYellow)
        computerSquare.append(BOTRIGHT)        

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

#draw and get the sequence of the square the computer drew
def drawComputerSquare(color,position):
    drawRect(color,position)
    pygame.display.update()
    getComputerSequence(color)

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

#draw the square the user click in
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

#set player defaults to zero
def setDefaults():
    colorSequence = list()
    squareSequence = list()

def help():
    print("Press '1' to start a random pattern of squares.")
    print("Press '2' to repeat a pattern generated from the user.")
    print("Press '3' to open the Help Menu.")
    print("Press 'SPACE' to start the game.")
    print("Press 'ENTER' to check if the pattern is correct.")
    print("The objective of the game is to keep guessing the correct pattern.")




    
drawDefault()
pygame.display.update()

help()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        iterator = -1
        score = 0 #let score be the endpoint
        
        if(event.type == pygame.KEYDOWN):
            
            #start random pattern of squares, by pressing 1
            if(event.key == pygame.K_1):
               #get the same square and color
               randomColor = [lightBlue,lightGreen,lightYellow,lightRed]
               squareLocation =[TOPRIGHT,BOTLEFT,BOTRIGHT,TOPLEFT]
 
               while(iterator < 20):
                   square = randint(0,3)
                   drawSquare(randomColor[square],squareLocation[square])
                   drawDefault()
                   pygame.time.wait(1000)
                   iterator += 1
               colorSequence = list()
               squareSequence = list()

               
            #repeat pattern generated from user, by pressing 2
            if(event.key == pygame.K_2):
                for i in range(0,len(colorSequence)):
                   drawSquare(colorSequence[i],squareSequence[i])
                   pygame.time.wait(1000)
                   drawDefault()
                colorSequence = list()
                squareSequence = list()


            if(event.key == pygame.K_3):
                help()

                
            #press space to start the game
            if(event.key == pygame.K_SPACE):
                while(iterator < score):
                    square = randint(0,3)
                    drawComputerSquare(randomColor[square],squareLocation[square])
                    pygame.time.wait(1000)
                    drawDefault()
                    iterator += 1
                userClick()

                
            #press return/enter to see if the player's pattern is right
            #if so, repeat the current pattern, and add one
            #then set the playerSequence to zero
            #if not, player loses
            if(event.key == pygame.K_RETURN):
                if(colorSequence == computerColor):
                    print("Correct!")
                    score += 1
                    iterator = -1
                    if(iterator < score):
                        for i in range(0,len(computerColor)):
                           drawSquare(computerColor[i],computerSquare[i])
                           pygame.time.wait(1000)
                           drawDefault()  
                        square = randint(0,3)
                        drawComputerSquare(randomColor[square],squareLocation[square])
                        pygame.time.wait(1000)
                        drawDefault()
                        iterator += 1
                    colorSequence = list()
                    squareSequence = list()
                else:
                    print("You Lost!")
                   
        #let user click on the square
        else:
           userClick()

        drawDefault()
