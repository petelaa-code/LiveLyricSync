import asyncio
import websockets

# Basic WebSocket server skeleton for LiveLyricSync

connected_clients = set()

async def handler(websocket):
    connected_clients.add(websocket)
    print("Client connected")

    try:
        async for message in websocket:
            print(f"Received: {message}")
            # Echo back for now (placeholder)
            await websocket.send(f"Server received: {message}")

    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

    finally:
        connected_clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("WebSocket server running on ws://localhost:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
