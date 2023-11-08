import socketio
import time
from Game import initPygame, runOneLoop, initLobby, renderLobby
import pygame
from UI import Button

gameRunning = False

def CreateClient(name="BRAVO 0-1",ip="http://localhost",port="7777"):
    global gameRunning
    with socketio.SimpleClient() as client:
        players = [name]
        
        print("Connecting...")
        client.connect(ip+":"+port, transports=['websocket'])
        client.emit('onJoin', {'username': name})
        endGame = False

        #global pygame stuff
        window = initPygame()
        clock = pygame.time.Clock()
        font = pygame.font.Font('./Resources/Roboto-Regular.ttf',32)
        UI = initLobby(players,window,font,name)
        isNotReady = True

        def becomeReady():
            global isNotReady
            isNotReady = False
            print("Ready'd Up!")
            client.emit("Ready")
        Ready = Button(font,window,"Ready Up",onClick=becomeReady)
    
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
                runOneLoop(window)
                print("Game Loop!")
            else:
                renderLobby(UI,window)
                if(isNotReady): Ready.render(x=1280/2,y=600)
            pygame.display.update()
            pygame.display.flip()

        pygame.quit()
        exit()


if __name__ == "__main__":
    print("Loading Client as MAIN")
    CreateClient(name="Apha-Romeo-Charlie 0-7")