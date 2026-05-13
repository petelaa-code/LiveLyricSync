# Server main entry point
# Tämä tiedosto yhdistää:
# - AudioInput (äänen kaappaus)
# - AlignmentEngine (synkronointi)
# - WebSocket-palvelin (tulee myöhemmin)

from audio.audio import AudioInput
from alignment.engine import AlignmentEngine

def main():
    print("Starting LiveLyricSync server...")

    # Luo audio-input
    audio = AudioInput()

    # Luo alignment engine
    engine = AlignmentEngine()

    # TODO: Käynnistä WebSocket-palvelin
    # TODO: Lataa lyriikat frontilta
    # TODO: Syötä audiokehyksiä engineen

    print("Server initialized (placeholder).")

if __name__ == "__main__":
    main()

