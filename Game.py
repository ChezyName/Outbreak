import pygame
import math
from PlayerClass import Player

pygame.init()
window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Outbreak Survival")
clock = pygame.time.Clock()

#my player
plr = Player("A","A",True)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    x = (keys[pygame.K_d] - keys[pygame.K_a])
    y = (keys[pygame.K_s] - keys[pygame.K_w])

    plrX,plyY = plr.rect.x, plr.rect.y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    rel_x, rel_y = mouse_x - plrX, mouse_y - plyY
    angle = math.degrees(math.atan2(rel_y, rel_x))

    plr.addLocation(x,y,(-angle) - 90)
    print("MouseAngle:",(-angle) - 90)

    window.fill((0,255,0))
    plr.DrawPlayer(window)
    pygame.display.flip()

pygame.quit()
exit()