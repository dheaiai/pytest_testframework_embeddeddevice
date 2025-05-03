import websocket

class WebSocketClient:
    def __init__(self, uri):
        self.uri = uri

    def connect(self):
        self.ws = websocket.create_connection(self.uri)

    def send(self, message):
        self.ws.send(message)

    def receive(self):
        return self.ws.recv()
