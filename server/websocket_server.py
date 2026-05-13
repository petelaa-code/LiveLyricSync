# WebSocket server (placeholder)
# Tämä moduuli tulee myöhemmin:
# - lähettämään synkronointidataa frontille
# - vastaanottamaan komentoja frontilta
# - pitämään yhteyden auki reaaliajassa

import asyncio
import websockets

class WebSocketServer:
    def __init__(self, host="localhost", port=8765):
        self.host = host
        self.port = port

    async def handler(self, websocket, path):
        print("Client connected")

        try:
            while True:
                # TODO: lähetä synkronointidataa
                await asyncio.sleep(0.1)
        except websockets.exceptions.ConnectionClosed:
            print("Client disconnected")

    def start(self):
        print(f"Starting WebSocket server on ws://{self.host}:{self.port}")
        return websockets.serve(self.handler, self.host, self.port)

