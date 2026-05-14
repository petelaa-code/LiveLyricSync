# Architecture

## 🇬🇧 English — System Architecture

LiveLyricSync is built as a multi‑device, real‑time rehearsal system.  
The architecture is designed to keep all tablets synchronized while allowing different roles (vocals, bass, guitar, drums, control) to receive customized data.

---

## 1. High‑Level Overview

The system consists of three main components:

1. **WebSocket Server**
   - Central authority for timing, section changes, and shared annotations.
   - Broadcasts synchronized data to all connected clients.
   - Receives commands from control tablets.

2. **Display Clients (Tablets)**
   - Show lyrics, chords, notation, cues, or other role‑specific information.
   - Render shared drawing annotations.
   - Stay synchronized with the server’s timeline.

3. **Control Clients**
   - Can jump between song sections.
   - Can loop time ranges.
   - Can draw annotations.
   - Can receive input from page‑turner pedals.

---

## 2. Data Flow

### Server → Clients
- Timestamp updates
- Section changes
- Role‑specific content (lyrics, chords, tabs, cues)
- Drawing strokes
- Loop start/end notifications

Example:
{
  "type": "lyrics",
  "time": 87.5,
  "text": "Sample lyric line"
}

### Clients → Server
- Jump commands
- Loop commands
- Drawing strokes
- Role registration
- Page‑turner pedal events

Example:
{ "command": "jump", "section": "chorus" }

---

## 3. Role‑Based Views

Each client registers its role:

{ "role": "vocals" }
{ "role": "bass" }
{ "role": "guitar" }
{ "role": "drums" }
{ "role": "lyrics" }
{ "role": "control" }

The server sends different data streams depending on the role.

---

## 4. Timing and Synchronization

The server maintains a master timeline:

- Current playback time (in seconds)
- Current section (intro, verse, chorus…)
- Loop mode (on/off)
- Loop boundaries (start/end)

Clients do not calculate timing themselves — they follow the server.

---

## 5. Annotation Layer

All drawing data is broadcast to every device:

{
  "command": "draw",
  "points": [...],
  "color": "#ff0000",
  "width": 3
}

Each client renders the drawing on top of its own view.

---

## 6. Page‑Turner Integration

A control tablet interprets pedal input as:

- Next section
- Previous section
- Loop toggle
- Optional custom actions

Pedal events are sent to the server as commands.

---

## 7. File Structure (Recommended)

