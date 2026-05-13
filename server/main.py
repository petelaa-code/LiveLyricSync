import asyncio
import json
import websockets

# ---------------------------------------------------------
# Simple lyric loader (placeholder)
# Later this will load ChordPro / UG / plain text
# ---------------------------------------------------------
def load_lyrics():
    return [
        "This is line 1",
        "This is line 2",
        "This is line 3",
        "This is line 4"
    ]

# ---------------------------------------------------------
# Sync Controller (MVP)
# Keeps track of current lyric line
# ---------------------------------------------------------
class LyricSync:
    def __init__(self, lyrics):
        self.lyrics = lyrics
        self.index = 0

    def next_line(self):
        if self.index < len(self.lyrics) - 1:
            self.index += 1
        return self.current_state()

    def current_state(self):
        current = self.lyrics[self.index]
        next_line = self.lyrics[self.index + 1] if self.index + 1 < len(self.lyrics) else ""
        return {
            "current": current,
            "next": next_line
        }

# ---------------------------------------------------------
# WebSocket server
# ---------------------------------------------------------
connected_clients = set()
lyrics = load_lyrics()
sync = LyricSync(lyrics)

async def handler(websocket):
    connected_clients.add(websocket)
    print("Client connected")

    # Send initial state
    await websocket.send(json.dumps(sync.current_state()))

    try:
        async for message in websocket:
            print(f"Received: {message}")

            if message == "next":
                state = sync.next_line()
                await broadcast(state)

            else:
                # Echo fallback for debugging
                await websocket.send(f"Server received: {message}")

    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

    finally:
        connected_clients.remove(websocket)

async def broadcast(state):
    if connected_clients:
        msg = json.dumps(state)
        await asyncio.gather(*(client.send(msg) for client in connected_clients))

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("LiveLyricSync WebSocket server running on ws://localhost:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
