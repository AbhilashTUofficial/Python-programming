import pygame
import sys







print("PAINT BRUSH")

# Main variables
play=True


# Creating screen
pygame.init()
drawBoardWidth=800
toolBarWidth=300
paddingWidth=20
drawBoardHeight=800
toolBarHeight=drawBoardHeight
paddingHeight=20
colorBoxHeight=200
selectionBoxHeight=400-(paddingHeight)
settingsBoxHeight=200
toolBarBorderColor=(200,200,200)
toolBarColor=(245,245,245)
drawBoardColor=(250,250,250)
font=pygame.font.SysFont("arial",18)
paddingColor=toolBarBorderColor
screenWidth=drawBoardWidth+toolBarWidth+paddingWidth
screenHeight=drawBoardHeight+paddingHeight
size=(screenWidth,screenHeight)
screen=pygame.display.set_mode(size)

r=0
g=0
b=0
screen.fill((255,255,255))

# Draw the draw-board
def drawBoard(RLevel,GLevel,BLevel):


    #Board
    #pygame.draw.rect(screen,(drawBoardColor),(0,0,screenWidth,screenHeight))



    #top padding
    pygame.draw.rect(screen,(paddingColor),(0,0,screenWidth,paddingHeight))
    #Bottom padding
    pygame.draw.rect(screen,(paddingColor),(0,(screenHeight-paddingHeight),screenWidth,paddingHeight))
    #Left padding
    pygame.draw.rect(screen,(paddingColor),(0,0,paddingWidth,screenHeight))
    #Right padding
    pygame.draw.rect(screen,(paddingColor),((screenWidth-paddingWidth),0,paddingWidth,screenHeight))
    #Tool bar
    ToolBar(RLevel,GLevel,BLevel)






def ToolBar(RLevel,GLevel,BLevel):

    # Variables

    currentColorBoxX=930
    currentColorBoxY=40
    currentColorBoxWidth=80
    currentColorBoxHeight=40
    currentColorBoxColor=(int(RLevel/870*2),int(GLevel/870*2),int(BLevel/870*2))
    colorLevelBarHeight=15
    colorLevelBarWidth=200
    colorLevelBarX=870
    colorLevelBarY=100
    colorLevelSpaceBetween=40
    REDcolorLevel=(r,0,0)
    REDcolorLevelWidth=50
    sliderRadius=10

    # Tool bar
    pygame.draw.rect(screen, (toolBarBorderColor), ((drawBoardWidth + paddingWidth), 0, toolBarWidth, toolBarHeight))
    # inner color box
    pygame.draw.rect(screen, (toolBarColor), (
    (drawBoardWidth + (paddingWidth * 2), paddingHeight, toolBarWidth - (paddingWidth * 2), colorBoxHeight)))
    # Current color box
    pygame.draw.rect(screen, (paddingColor), (currentColorBoxX, currentColorBoxY, currentColorBoxWidth, currentColorBoxHeight))
    pygame.draw.rect(screen, (currentColorBoxColor), (currentColorBoxX+3, currentColorBoxY+3, currentColorBoxWidth-6, currentColorBoxHeight-6))

    #RED color level
    pygame.draw.rect(screen, (paddingColor),(colorLevelBarX, colorLevelBarY, colorLevelBarWidth, colorLevelBarHeight))
    pygame.draw.rect(screen, (drawBoardColor), (colorLevelBarX+3, colorLevelBarY + 3, colorLevelBarWidth- 6, colorLevelBarHeight - 6))
    label = font.render("R", 1, (200, 20, 20))
    screen.blit(label, (colorLevelBarX-20, colorLevelBarY-4))
    pygame.draw.circle(screen,(paddingColor),(RLevel,colorLevelBarY+7),sliderRadius)
    pygame.draw.circle(screen,((180,0,0)),(RLevel,colorLevelBarY+7),sliderRadius-2)


    # GREEN color level
    pygame.draw.rect(screen, (paddingColor), (colorLevelBarX, colorLevelBarY+colorLevelSpaceBetween, colorLevelBarWidth, colorLevelBarHeight))
    pygame.draw.rect(screen, (drawBoardColor),(colorLevelBarX + 3, colorLevelBarY + 3+colorLevelSpaceBetween, colorLevelBarWidth - 6, colorLevelBarHeight - 6))
    label = font.render("G", 1, (20, 200, 20))
    screen.blit(label, (colorLevelBarX - 20, colorLevelBarY - 4+colorLevelSpaceBetween))
    pygame.draw.circle(screen,(paddingColor),(GLevel,colorLevelBarY+7+colorLevelSpaceBetween),sliderRadius)
    pygame.draw.circle(screen,((0,180,0)),(GLevel,colorLevelBarY+7+colorLevelSpaceBetween),sliderRadius-2)

    # BLUE color level
    pygame.draw.rect(screen, (paddingColor), (colorLevelBarX, colorLevelBarY+colorLevelSpaceBetween*2, colorLevelBarWidth, colorLevelBarHeight))
    pygame.draw.rect(screen, (drawBoardColor),(colorLevelBarX + 3, colorLevelBarY + 3+colorLevelSpaceBetween*2, colorLevelBarWidth - 6, colorLevelBarHeight - 6))
    label = font.render("B", 1, (20, 20, 200))
    screen.blit(label, (colorLevelBarX - 20, colorLevelBarY - 4+colorLevelSpaceBetween*2))
    pygame.draw.circle(screen, (paddingColor), (BLevel, colorLevelBarY + 7+(colorLevelSpaceBetween*2)), sliderRadius)
    pygame.draw.circle(screen, ((0, 0, 180)), (BLevel, colorLevelBarY + 7 + (colorLevelSpaceBetween*2)), sliderRadius - 2)








    # the box which the current color

    # inner selection box
    pygame.draw.rect(screen, (toolBarColor), ((
    drawBoardWidth + (paddingWidth * 2), (paddingHeight + colorBoxHeight + 5), toolBarWidth - (paddingWidth * 2),
    selectionBoxHeight - 10)))



    pygame.draw.rect(screen,(drawBoardColor),((880,235),(100,100)))
    pygame.draw.rect(screen,(drawBoardColor),((880,360),(100,100)))
    pygame.draw.rect(screen,(drawBoardColor),((880,485),(100,100)))



    # inner settings box
    pygame.draw.rect(screen, (toolBarColor), ((
    drawBoardWidth + (paddingWidth * 2), (paddingHeight + colorBoxHeight + selectionBoxHeight),
    toolBarWidth - (paddingWidth * 2), settingsBoxHeight)))






    pygame.display.update()


# PLAY LOOP
RLevel = 870
BLevel=870
GLevel=870


def main(RLevel,GLevel,BLevel):
    while play:


        drawBoard(RLevel,GLevel,BLevel)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            else:

                if(event.type==pygame.MOUSEMOTION):
                    cursorX=event.pos[0]
                    cursorY=event.pos[1]
                    pygame.draw.circle(screen, (255, 0, 0), (cursorX, cursorY), 20)

                    print(cursorX,"x",cursorY,"y")
                    if(1060>cursorX>870):
                        if(112>cursorY>100):

                        # red level bar
                            if(True):
                                print("hi")

                                print(RLevel)

                                RLevel=cursorX

                        if (152 > cursorY > 140):
                            # green level bar
                            if (True):
                                GLevel=cursorX
                        if (192 > cursorY > 180):
                            # blue level bar
                            if (True):
                                BLevel=cursorX

    pygame.display.update()

main(RLevel,GLevel,BLevel)