# LiveLyricSync – Roadmap

This roadmap outlines the development path for the LiveLyricSync project, from the initial MVP to the full 1.0 release.

---

## 🎯 MVP (Minimum Viable Product)

### Core Features
- WebSocket server running on the PC
- Basic web client that displays a single lyric line
- Ability to load lyrics from:
  - ChordPro files
  - Ultimate Guitar–style text
  - Plain text
- Manual line switching (for testing and debugging)

### Goals
- Establish the communication pipeline (server → client)
- Validate that the UI updates reliably
- Prepare the structure for real-time alignment

---

## 🚀 Beta Release

### Audio & Alignment
- Audio input from mixer monitor out (WASAPI / ASIO)
- Audio fingerprinting using:
  - Chromaprint
  - Essentia
- Real-time alignment using DTW (Dynamic Time Warping)
- Automatic lyric line switching based on alignment

### UI Improvements
- Karaoke-style lyric highlighting
- Basic chord rendering
- Responsive layout for tablets and phones

---

## 🟦 Version 1.0 Release

### Advanced Features
- Tempo compensation and drift correction
- Multiple display modes:
  - Singer view
  - Guitarist view
  - Drummer view
- Full ChordPro support (colors, diagrams, formatting)
- Configurable UI themes
- Multi-client synchronization

### Stability & Deployment
- Windows installer for the server
- Local configuration UI
- Logging and diagnostics tools

---

## 📌 Long-Term Ideas (Post‑1.0)

- AI-assisted chord extraction
- AI-assisted lyric alignment
- Offline fingerprint generation tool
- Multi-song setlist mode
- MIDI clock sync
- OSC integration for lighting consoles

---

## ✔ Status

The project is in the **initial setup phase**.  
Next steps:
1. Architecture documentation  
2. WebSocket server skeleton  
3. Basic client UI  
