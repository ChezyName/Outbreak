from ServerClass import Server
from PlayerClass import Player
import tornado.ioloop
from tornado.options import define, options, parse_command_line
import tornado.web
import socketio

players = []

server = socketio.AsyncServer(async_mode='tornado')

def getPlayer(UID=""):
    for i in range(0,len(players)):
        if(players[i].UID == UID):
            return players[i],i
    return "",-1

def CreateServer(port=7777,debug=False):
    global clients
    clients = []

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
def onJoin(sid,data):
    player,index = getPlayer(str(sid))
    print("Player Has Joined And Sent Their Username")
    print(data)
    if index == -1:
        print("Creating New Player Class")
        plr = Player("BRAVO 0-"+str(len(players)),str(sid))
        players.append(plr)
        print(plr.name,"Has Joined The Game!")

@server.on("move")
def changePosition(sid,data):
    print("Client Chaning Their Position!")
    print(data)

if __name__ == "__main__": CreateServer()