# LiveLyricSync
### Real-time lyric display for live bands using audio alignment

LiveLyricSync is an open-source project that aims to create a system capable of:

- Listening to monitor output from a live mixer
- Detecting in real time where the band is in the song
- Displaying synchronized lyrics and chords on a tablet or phone
- Running entirely web-based (no mobile app required)
- Supporting Ultimate Guitar tabs, ChordPro, and plain text lyrics

The goal is to provide a practical, hands-free lyric display tool for bands, singers, and live engineers during performances.

---

## Project Goals

1. Import original song + lyrics
2. Generate an audio fingerprint from the studio track
3. Listen to live audio from the mixer’s monitor output
4. Detect the current song position in real time
5. Send the correct lyric line to connected web clients
6. Display lyrics in a karaoke-style interface
7. Support chords, ChordPro format, and UG-style tabs

---

## Architecture Overview

[ Mixer / Monitor Out ]
            ↓
        [ PC Server ]
  - Audio input (WASAPI/ASIO)
  - Fingerprinting (Essentia / Chromaprint)
  - Real-time alignment (DTW)
  - Lyric engine (ChordPro/LRC)
  - WebSocket server
            ↓
   [ Tablet / Phone / Browser ]
  - HTML/JS client
  - Karaoke-style lyric display

---

## Repository Structure

/server
    audio/
    alignment/
    lyrics/
    websocket/
    main.py

/client
    index.html
    style.css
    client.js

/docs
    architecture.md
    roadmap.md
    examples/

---

## Roadmap

### MVP
- WebSocket server (PC)
- Basic web client (single-line lyric display)
- Load UG tabs / ChordPro text
- Manual line switching (for testing)

### Beta
- Audio input from monitor out
- Audio fingerprinting (Chromaprint / Essentia)
- Real-time alignment (DTW)
- Automatic line switching
- Karaoke-style UI

### 1.0 Release
- Tempo compensation
- Multiple display modes (singer, guitarist, drummer)
- Chord display
- Mobile/tablet optimization
- Configurable UI

---

## Technologies

### Server (PC)
- Python (FastAPI / Flask)
- Essentia / Chromaprint
- NumPy / SciPy
- DTW algorithms
- WebSocket (aiohttp / websockets)

### Client (Browser)
- HTML / CSS / JavaScript
- WebSocket client
- Responsive karaoke UI

---

## Contributing

Contributions are welcome from:

- DSP developers
- Web developers
- Musicians
- Testers
- Documentation writers

Start by reading /docs/roadmap.md and opening an Issue or Pull Request.

---

## License

This project is licensed under the MIT License.
Free to use, modify, and distribute.

---

## Contact

To participate, open an Issue or Discussion on GitHub.
