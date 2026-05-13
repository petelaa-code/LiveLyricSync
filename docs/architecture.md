# LiveLyricSync – Architecture Overview

## 1. System Summary

LiveLyricSync is a real‑time lyric synchronization system designed for live bands.  
It listens to a monitor mix, detects the current position in a song using audio fingerprinting and alignment, and sends the correct lyric line to connected web clients.

The system consists of:

- PC Server (Python)
- Browser Client (HTML/JS)
- WebSocket communication layer
- Audio analysis pipeline
- Lyric/chord rendering engine

---

## 2. High‑Level Architecture

[ Mixer / Monitor Out ]
            ↓
        [ PC Server ]
  - Audio Input (WASAPI/ASIO)
  - Fingerprinting (Essentia / Chromaprint)
  - Real-Time Alignment (DTW)
  - Lyric Engine (ChordPro / UG / TXT)
  - WebSocket Server
            ↓
   [ Tablet / Phone / Browser ]
  - HTML/JS Client
  - Karaoke-style Lyric Display

---

## 3. Server Components

### 3.1 Audio Input Layer
Responsible for capturing live audio from the mixer.

- WASAPI (Windows)
- ASIO (low‑latency)
- Buffer size: 2048–8192 samples
- Output: PCM float32 frames

### 3.2 Fingerprinting
Used to match live audio to the studio track.

- Chromaprint (AcoustID)
- Essentia spectral features
- Precomputed fingerprint stored per song

### 3.3 Alignment Engine
Determines the current playback position.

- Dynamic Time Warping (DTW)
- Sliding window comparison
- Drift correction
- Output: timestamp in seconds

### 3.4 Lyric Engine
Loads and parses:

- ChordPro (.pro)
- Ultimate Guitar style tabs
- Plain text lyrics

Outputs:

- list of lyric lines
- optional chord lines
- timestamp mapping (future)

### 3.5 Sync Controller
Tracks:

- current lyric index
- next lyric
- alignment updates
- manual override (MVP)

### 3.6 WebSocket Server
Broadcasts JSON messages to all connected clients.

Example message:

{
  "current": "This is line 1",
  "next": "This is line 2"
}

---

## 4. Client Architecture

### 4.1 WebSocket Client
- Auto‑reconnect
- Receives JSON lyric updates
- Sends manual commands ("next")

### 4.2 UI Renderer
Displays:

- current line (large font)
- next line (dimmed)
- future: karaoke highlight

### 4.3 Input Handler
For testing:

- ArrowRight → next line

---

## 5. Data Flow

Live Audio → Fingerprint → DTW Alignment → Lyric Index → WebSocket → Browser UI

---

## 6. MVP Scope

- Manual line switching
- WebSocket server
- Basic client UI
- Static lyric loading

---

## 7. Future Features

- Automatic alignment
- Tempo drift compensation
- Multi‑view modes (singer, guitarist, drummer)
- Chord display
- Mobile optimization
- Song library
- Setlist mode
