from ServerClass import Server
from PlayerClass import Player
import tornado.ioloop
from tornado.options import define, options, parse_command_line
import tornado.web
import socketio

players = []
gameStarted = False
server = socketio.AsyncServer(async_mode='tornado')

def getPlayer(UID=""):
    for i in range(0,len(players)):
        if(players[i].UID == UID):
            return players[i],i
    return "",-1

def getReadyPlayers():
    readyPlrs = 0
    for i in range(0,len(players)):
        if(players[i].isReady): readyPlrs += 1
    return readyPlrs

def CreateServer(port=7777,debug=False):
    global clients
    clients = []

    print("Creating Server on port:",port)

    @server.event
    async def connect(sid, environ):
        clients.append(sid)
        print("Client ",clients.index(sid)+1 ," - ", sid, " Has Connected!")
        await server.emit('onConnected', {'data': 'OK'}, room=sid)
    @server.event
    def disconnect(sid):
        print("Client ",clients.index(sid)+1 ," - ", sid , ' Has Disconnected')
        clients.remove(sid)

    app = tornado.web.Application(
        [
            (r"/socket.io/", socketio.get_tornado_handler(server)),
        ],
        debug=debug,
    )
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()

@server.event
async def onJoin(sid,data):
    global gameStarted
    if(gameStarted):
        await server.disconnect(sid)
        return gameStarted
    player,index = getPlayer(str(sid))
    print("Player Has Joined And Sent Their Username")
    print(data)
    if index == -1:
        print("Creating New Player Class")
        plr = Player(data['username'],str(sid))
        players.append(plr)
        print(plr.name,"Has Joined The Game!")

        #send player list
        names = []
        for i in range(len(players)):
            names.append(players[i].name)
        await server.emit('StartGame',{'players': names})

@server.on("move")
def changePosition(sid,data):
    plr,indx = getPlayer(str(sid))
    if(indx != -1):
        plr.setLocation(data['x'],data['y'],data['r'])

@server.on("Start")
async def StartGame(sid):
    print("About to start game!!")
    gameStarted = True
    await server.emit('StartGame',{'plrCount': len(players)})

@server.on("Ready")
async def becomeReady(sid):
    global gameStarted
    if(gameStarted): return
    plr,indx = getPlayer(str(sid))
    if(indx != -1):
        plr.isReady = True
    readyCount = getReadyPlayers()
    print(readyCount,"/",len(players),"are ready.")
    if(readyCount >= len(players)):
        print("Starting Game Shortly...")
        gameStarted = True
        await server.emit('StartGame',{'plrCount': len(players)})

        

if __name__ == "__main__": CreateServer()