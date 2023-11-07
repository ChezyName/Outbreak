import socketio
import time

with socketio.SimpleClient() as client:
    print("Connecting...")
    client.connect('http://localhost:7777', transports=['websocket'])
    while True:
        print("Sending Server MSG")
        client.emit('A', {'foo': 'bar'})
        time.sleep(500)