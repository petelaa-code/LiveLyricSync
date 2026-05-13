async def handler(self, websocket, path):
    print("Client connected")

    try:
        while True:
            await websocket.send("ping")  # lähetetään testiviesti
            await asyncio.sleep(0.1)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
