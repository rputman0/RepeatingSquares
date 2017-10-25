import pygame

#instanciate a new window
pygame.init()
(width, height) = (300,300)

#set the width and height, and caption
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

#create Four Squares (red,green,blue,yellow)
pygame.draw.rect(screen, red, [0,0,150,150],0)
pygame.draw.rect(screen, green, [0,150,150,150],0)
pygame.draw.rect(screen, blue, [149,0,150,150],0) #TODO: blue is slightly off
pygame.draw.rect(screen, yellow, [150,150,150,150],0)

pygame.display.update()

#CLOSING THE WINDOW, Do events here (Place at the end)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #let the user click on the buttons
        mousePos = pygame.mouse.get_pos()
        if(event.type == pygame.MOUSEBUTTONDOWN and (mousePos[0] > 0 and mousePos[0] < 150 and mousePos[1] < 150)):
            pygame.draw.rect(screen, lightRed, [0,0,150,150],0)
            #print(mousePos)
            pygame.display.update()
        elif(event.type == pygame.MOUSEBUTTONDOWN and (mousePos[0] > 150 and mousePos[0] < 300 and mousePos[1] < 150)):
            pygame.draw.rect(screen, lightBlue, [149,0,150,150],0) #TODO: blue is slightly off
            #print(mousePos)
            pygame.display.update()
        elif(event.type == pygame.MOUSEBUTTONDOWN and (mousePos[0] > 0 and mousePos[0] < 150 and mousePos[1] > 150 and mousePos[1] < 300)):
            pygame.draw.rect(screen, lightGreen, [0,150,150,150],0)
            #print(mousePos)
            pygame.display.update()
        elif(event.type == pygame.MOUSEBUTTONDOWN and (mousePos[0] > 150 and mousePos[0] < 300 and mousePos[1] > 150 and mousePos[1] < 300)):
            pygame.draw.rect(screen, lightYellow, [150,150,150,150],0)
            #print(mousePos)
            pygame.display.update()
        else:
            pygame.draw.rect(screen, red, [0,0,150,150],0)
            pygame.draw.rect(screen, green, [0,150,150,150],0)
            pygame.draw.rect(screen, blue, [149,0,150,150],0) #TODO: blue is slightly off
            pygame.draw.rect(screen, yellow, [150,150,150,150],0)
            pygame.display.update()

        #press enter to start the game
        if(event.type == pygame.KEYDOWN):
           if(event.key == pygame.K_RETURN):
                print("Hello World")

#6. Create random sequence of red,green,blue,yellow (1 = red, ...,4 = yellow)
    #6.A Store random sequence into an arraylist
    #6.B Use for loop to display arraylist on screen
        #6.C For each item, turn square into lighter color
        #6.D Wait 1 Second, turn square back into darker color
        #6.E Go to next item in arraylist
#7. Check if user enters the same arraylist (clicks on squares in the same sequence)
#8. If user has entered the same arraylist
    #8.A - Print "Correct: Score++" and Play sound
    #8.B - Increment the arraylist
         #8.C - Keep the last pattern the same, add one new random pattern
#9. Else
    #9.A - Print "Wrong: Game Over\nFinal Score: Score"
    #9.B - Prompt user to try again
    #9.C - Reset the Arraylist
#10. Upload to github
