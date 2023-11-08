import socketio
import time
from Game import initPygame, runOneLoop, initLobby, renderLobby
import pygame
from UI import Button

def CreateClient(name="BRAVO 0-1",ip="http://localhost",port="7777"):
    with socketio.SimpleClient() as client:
        players = [name]
        
        print("Connecting...")
        client.connect(ip+":"+port, transports=['websocket'])
        client.emit('onJoin', {'username': name})
        gameRunning = False
        endGame = False

        #global pygame stuff
        window = initPygame()
        clock = pygame.time.Clock()
        font = pygame.font.Font('./Resources/Roboto-Regular.ttf',32)
        UI = initLobby(players,window,font,name)
        Ready = Button(font,window,"Ready Up")
    
        @client.client.on('StartGame')
        def startGame(data):
            global gameRunning
            print("Starting Game",data)
            gameRunning = True

        @client.client.on('PlayerList')
        def playerList(data):
            global UI
            print("NewPlayerList",data['players'])
            UI = initLobby(data['players'],window,font)

        while not endGame:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameRunning = False
                    endGame = True
                    break
            if gameRunning:
                runOneLoop()
            else:
                renderLobby(UI,window)
                Ready.render(x=1280/2,y=600)
                pygame.display.update()
                pygame.display.flip()

        pygame.quit()
        exit()


if __name__ == "__main__":
    print("Loading Client as MAIN")
    CreateClient(name="Apha-Romeo-Charlie 0-7")