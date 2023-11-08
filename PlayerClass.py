import pygame

class Player:
    def __init__(self, name="OPERATOR",UID="",isClient=False):
        self.x = 0
        self.y = 0
        self.r = 0
        self.name = name
        self.UID = UID
        self.Client = isClient

        self.Sprite = pygame.image.load('./Resources/Tank.png')
        self.Sprite = pygame.transform.scale(self.Sprite,(80,80))
        self.rect = self.Sprite.get_rect()

    def getLocation(self):
        return (self.x,self.y)
    
    def setLocation(self,x,y):
        self.x = x
        self.y = y

    def addLocation(self,ax,ay,ar):
        self.x = ax * 1
        self.y = ay * 1
        self.r = ar

    def getLocationRotation(self):
        return (self.x,self.y,self.r)
    
    def DrawPlayer(self,screen):
        image = pygame.transform.rotate(self.Sprite, self.r)
        #self.r += 1 % 360  # Value will reapeat after 359. This prevents angle to overflow.
        x, y = self.rect.center  # Save its current center.
        self.rect = image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y) 
        self.rect.x += self.x
        self.rect.y += self.y
        screen.blit(image,self.rect)