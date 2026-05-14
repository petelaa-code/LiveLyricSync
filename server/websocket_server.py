import asyncio
import json
import websockets

class WebSocketServer:
    def __init__(self, host="localhost", port=8765):
        self.host = host
        self.port = port
        self.latest_data = "🎵 Tämä on testilyriikki – toimii!"

    async def start(self):
        async with websockets.serve(self.handler, self.host, self.port):
            print(f"WebSocket server running on ws://{self.host}:{self.port}")
            await asyncio.Future()  # pitää serverin käynnissä

    async def handler(self, websocket):
        print("Client connected")
        try:
            test_lines = [
                "🎵 Tämä on ensimmäinen rivi",
                "🎵 Ja tämä on toinen rivi",
                "🎵 Kolmas rivi tulee nyt",
                "🎵 Neljäs rivi – toimii edelleen!",
                "🎵 Viides rivi – kaikki ok!"
            ]

            for line in test_lines:
                await websocket.send(json.dumps(line))
                await asyncio.sleep(1.5)

        except websockets.exceptions.ConnectionClosed:
            print("Client disconnected")


if __name__ == "__main__":
    server = WebSocketServer()
    asyncio.run(server.start())
