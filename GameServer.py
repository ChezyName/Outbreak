from ServerClass import Server
from PlayerClass import Player

players = []

def getPlayer(UID=""):
    for i in range(0,len(players)):
        if(players[i].UID == UID):
            return players[i],i
    return "",-1

def onJoin(sid):
    player,index = getPlayer(str(sid))
    if index == -1:
        print("Creating New Player Class")
        plr = Player("BRAVO 0-"+str(len(players)),str(sid))
        players.append(plr)
        print(plr.name,"Has Joined The Game!")

server = Server(onConnectFunc=onJoin)
gameServer = server.getServer()
server.runServer()