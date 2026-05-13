import asyncio
import json
import websockets

class WebSocketServer:
    def __init__(self, host="localhost", port=8765):
        self.host = host
        self.port = port
        self.latest_data = None  # tänne main.py kirjoittaa viimeisimmän datan

    def start(self):
        return websockets.serve(self.handler, self.host, self.port)

    async def handler(self, websocket, path):
        print("Client connected")

        try:
            while True:
                if self.latest_data is not None:
                    await websocket.send(json.dumps(self.latest_data))

                await asyncio.sleep(0.05)  # 20 FPS
        except websockets.exceptions.ConnectionClosed:
            print("Client disconnected")
