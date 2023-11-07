import os
import tornado.ioloop
from tornado.options import define, options, parse_command_line
import tornado.web
import socketio

class Server:
    def __init__(self, port=7777, debug=False,onConnectFunc=()):
        self.server = socketio.AsyncServer(async_mode='tornado')
        self.clients = []
        self.port = port
        self.debug = debug

        @self.server.event
        async def connect(sid, environ):
            self.clients.append(sid)
            onConnectFunc(sid)
            print("Client ",self.clients.index(sid)+1 ," - ", sid, " Has Connected!")
            await self.server.emit('onConnected', {'data': 'OK'}, room=sid)
        @self.server.event
        def disconnect(sid):
            print("Client ",self.clients.index(sid)+1 ," - ", sid , ' Has Disconnected')
            self.clients.remove(sid)

    def runServer(self):
        app = tornado.web.Application(
            [
                (r"/socket.io/", socketio.get_tornado_handler(self.server)),
            ],
            debug=self.debug,
        )
        app.listen(self.port)
        tornado.ioloop.IOLoop.current().start()

    def getServer(self):
        return self.server


if __name__ == "__main__":
    print("Creating Server on port 7777")
    server = Server()
    server.runServer()
