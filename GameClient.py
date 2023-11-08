import socketio
import time

def CreateClient(name="BRAVO 0-1",ip="http://localhost",port="7777"):
    with socketio.SimpleClient() as client:
        print("Connecting...")
        client.connect(ip+":"+port, transports=['websocket'])
        client.emit('onJoin', {'username': name})
        while True:
            print("Updating Position -> Server")
            client.emit('move', {'x': 24, 'y': 51})
            time.sleep(1)
    

if __name__ == "__main__":
    CreateClient(name="Apha-Romeo-Charlie 0-7")