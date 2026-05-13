# Server main entry point

import asyncio

from audio.audio import AudioInput
from alignment.engine import AlignmentEngine
from websocket_server import WebSocketServer

async def main():
    print("Starting LiveLyricSync server...")

    # Luo audio-input
    audio = AudioInput()

    # Luo alignment engine
    engine = AlignmentEngine()

    # Luo WebSocket-palvelin
    ws_server = WebSocketServer()

    # Käynnistä WebSocket-palvelin
    server = ws_server.start()

    print("WebSocket server running.")
    print("Server initialized (placeholder).")

    # Aja WebSocket-palvelin asyncio-loopissa
    async with server:
        await asyncio.Future()  # pitää palvelimen käynnissä

if __name__ == "__main__":
    asyncio.run(main())


