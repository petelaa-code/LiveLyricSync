import asyncio

from audio.audio import AudioInput
from alignment.engine import AlignmentEngine
from websocket_server import WebSocketServer

async def main():
    print("Starting LiveLyricSync server...")

    audio = AudioInput()
    engine = AlignmentEngine()
    ws_server = WebSocketServer()

    server = ws_server.start()

    async with server:
        while True:
            # 1) Hae audiokehys
            frame = audio.get_frame()

            # 2) Syötä se alignment-moottorille
            result = engine.process_frame(frame)

            # 3) Lähetä WebSocketin kautta
            ws_server.latest_data = result

            await asyncio.sleep(0.05)  # 20 FPS päivitys

if __name__ == "__main__":
    asyncio.run(main())



