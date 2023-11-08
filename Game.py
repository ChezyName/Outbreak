import pygame
import math

def initPygame():
    pygame.init()
    window = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Outbreak Survival")
    return window

def runOneLoop(window):
    keys = pygame.key.get_pressed()
    '''
    x = (keys[pygame.K_d] - keys[pygame.K_a])
    y = (keys[pygame.K_s] - keys[pygame.K_w])

    plrX,plyY = plr.rect.x, plr.rect.y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    rel_x, rel_y = mouse_x - plrX, mouse_y - plyY
    angle = math.degrees(math.atan2(rel_y, rel_x))

    plr.addLocation(x,y,(-angle) - 90)
    print("MouseAngle:",(-angle) - 90)
    '''

    window.fill((0,255,0))
    #plr.DrawPlayer(window)

def initLobby(playerNames=[],window={},font={},myName=""):
    pygame.display.set_caption("Lobby - " + str(len(playerNames)) + " Players.")
    y = 32
    UIs = []
    for i in range(len(playerNames)):
        print("Displaying:", playerNames[i])
        xSize,ySize = window.get_size()
        text = font.render(playerNames[i], True, (255,255,255), (0,0,0))
        if(myName == playerNames[i]):
            text = font.render("ME> "+playerNames[i], True, (255,255,255), (0,0,0))
        textRect = text.get_rect()
        textRect.center = (xSize // 2, y)
        y += 50
        UIs.append([text,textRect])
    
    return UIs

def renderLobby(UIs,window):
    window.fill((0,0,0))
    for i in range(len(UIs)):
        text,rect = UIs[i]
        window.blit(text,rect)
