import pygame

class Button:
    def __init__(self,font,window,text,color=(255,255,255),backgroundColor=(150,150,150), hoverColor=(80,80,80)):
        self.font = font
        self.window = window

        self.color = color
        self.backgroundColor = backgroundColor
        self.hoverColor = hoverColor

        self.words = text

    def render(self,x=0,y=0):
        self.width, self.height = self.font.size(self.words)
        self.text = self.font.render(self.words, True , self.color)
        mouse = pygame.mouse.get_pos() 
        x -= self.width/2

        if (x) <= mouse[0] <= (self.width + x) and (y) <= mouse[1] <= (self.height + y): 
            pygame.draw.rect(self.window,self.hoverColor,[x,y,self.width,self.height]) 
        else: 
            pygame.draw.rect(self.window,self.backgroundColor,[x,y,self.width,self.height]) 

        self.window.blit(self.text , (x,y,self.width,self.height))
