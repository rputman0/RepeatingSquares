from random import *
import pygame

#instanciate a new window
pygame.init()
(width, height) = (300,300)

#set the width, height, and caption
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Simon Says")

#get the light colors and darker colors (red,green,blue,yellow)
blue = [0,0,255]
red = [255,0,0]
green = [0,255,0]
yellow = [255,255,0]

lightBlue = [135,206,250]
lightRed = [253,160,122]
lightGreen = [34,139,34]
lightYellow = [227,250,96]

colorSequence = list()
def getSequence(color,colorSequence):
    if(color == lightBlue):
        colorSequence.append("BLUE")
    elif(color == lightRed):
        colorSequence.append("RED")
    elif(color == lightGreen):
        colorSequence.append("GREEN")
    elif(color == lightYellow):
        colorSequence.append("YELLOW")

TOPLEFT = [0,0,150,150]
TOPRIGHT = [149,0,150,150]
BOTLEFT = [0,150,150,150]
BOTRIGHT = [150,150,150,150]

def drawSquare(color,position):
    pygame.draw.rect(screen,color,position,0)
    pygame.display.update()
    getSequence(color,colorSequence)

def drawDefault():
    pygame.draw.rect(screen, red, TOPLEFT,0)
    pygame.draw.rect(screen, blue, TOPRIGHT,0)
    pygame.draw.rect(screen, green, BOTLEFT,0)
    pygame.draw.rect(screen, yellow, BOTRIGHT,0)

def userClick():
    mousePos = pygame.mouse.get_pos()
    if(event.type == pygame.MOUSEBUTTONDOWN and (mousePos[0] > 0 and mousePos[0] < 150 and mousePos[1] < 150)):
        drawSquare(lightRed,TOPLEFT)
    elif(event.type == pygame.MOUSEBUTTONDOWN and (mousePos[0] > 150 and mousePos[0] < 300 and mousePos[1] < 150)):
        drawSquare(lightBlue,TOPRIGHT)
    elif(event.type == pygame.MOUSEBUTTONDOWN and (mousePos[0] > 0 and mousePos[0] < 150 and mousePos[1] > 150 and mousePos[1] < 300)):
        drawSquare(lightGreen,BOTLEFT)
    elif(event.type == pygame.MOUSEBUTTONDOWN and (mousePos[0] > 150 and mousePos[0] < 300 and mousePos[1] > 150 and mousePos[1] < 300)):
        drawSquare(lightYellow,BOTRIGHT)
        getSequence(lightYellow,colorSequence)
    else:
        drawDefault()
        pygame.display.update()

drawDefault()
pygame.display.update()

#CLOSING THE WINDOW (this is the main loop)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #let the user click on the buttons
        userClick()

        #press enter to start the game
        randomColor = [lightBlue,lightGreen,lightYellow,lightRed]
        squareLocation =[TOPRIGHT,BOTLEFT,BOTRIGHT,TOPLEFT]
        if(event.type == pygame.KEYDOWN):
           if(event.key == pygame.K_t): #use for test mode
               print(colorSequence)
           elif(event.key == pygame.K_RETURN):
               end = 1
               i = 0
               score = 0
               
               for i in range(i,end): #choose this for one loop
               #while(i <= end):  #to repeat
                   square = randint(0,3)
                   drawSquare(randomColor[square],squareLocation[square])
                   
                   pygame.time.wait(1000)

                   checkAgainst = colorSequence
                   print(checkAgainst)
                   colorSequence = list()

                   #wait for user input
                   userClick()

                   print(colorSequence)
               
        #7. Check if user enters the same list (clicks on squares in the same sequence)

        #8. If user has entered the same list
            #8.A - Print "Correct: Score++" and Play sound
            #8.B - Increment the list
             #8.C - Keep the last pattern the same, add one new random pattern
        #9. Else
            #9.A - Print "Wrong: Game Over\nFinal Score: Score"
            #9.B - Prompt user to try again
            #9.C - Reset the list
