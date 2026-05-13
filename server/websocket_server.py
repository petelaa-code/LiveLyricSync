import json

async def handler(self, websocket, path):
    print("Client connected")

    try:
        while True:
            data = {
                "type": "sync",
                "position": 0.0,   # testiarvo
                "word": None       # ei vielä oikeaa sanaa
            }

            await websocket.send(json.dumps(data))
            await asyncio.sleep(0.1)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
