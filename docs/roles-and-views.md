# Roles and Views

## 🇬🇧 English — Roles and Display Views

LiveLyricSync supports multiple musician roles, each with a customized display view.  
All devices stay synchronized through the WebSocket server, but each role receives different data depending on its needs.

---

## 1. Display Roles

### Vocals (Lead / Backing)
Shows:
- Lyrics
- Section markers (Intro, Verse, Chorus, Bridge)
- Optional harmony/stem color coding
- Shared annotations (drawings, notes)

Receives:
{
  "type": "lyrics",
  "time": 87.5,
  "text": "Sample lyric line"
}

---

### Bass
Shows:
- Bass notation or tablature
- Song structure
- Cues (e.g., “Chorus in 2 bars”)
- Shared annotations

Receives:
{
  "type": "bass",
  "time": 87.5,
  "notes": [...]
}

---

### Guitar
Shows:
- Chord symbols
- Strumming patterns
- Section transitions
- Shared annotations

Receives:
{
  "type": "guitar",
  "time": 87.5,
  "chords": [...]
}

---

### Drums
Shows:
- Visual click / tempo indicator
- Section cues
- Fill markers
- Shared annotations

Receives:
{
  "type": "drums",
  "time": 87.5,
  "cue": "Fill in 1 bar"
}

---

## 2. Control Roles

### Control Tablet (Primary)
Can:
- Jump to sections (intro, verse, chorus…)
- Loop a time range
- Start/stop playback
- Send annotations (drawing strokes)
- Handle page‑turner pedal input

Sends:
{ "command": "jump", "section": "chorus" }
{ "command": "loop", "start": 45.0, "end": 52.0 }
{
  "command": "draw",
  "points": [...],
  "color": "#ff0000"
}

---

### Control Tablet (Secondary)
Same capabilities as primary, but optional.  
Useful for conductor, band leader, or sound engineer.

---

## 3. Shared Annotation Layer

All devices display the same drawing layer on top of their role‑specific view.

Example stroke:
{
  "command": "draw",
  "points": [
    { "x": 120, "y": 80 },
    { "x": 122, "y": 82 },
    { "x": 125, "y": 85 }
  ],
  "color": "#ff0000",
  "width": 3
}

---

## 4. Role Registration

Each device identifies itself to the server:

{ "role": "vocals" }
{ "role": "bass" }
{ "role": "guitar" }
{ "role": "drums" }
{ "role": "lyrics" }
{ "role": "control" }

The server responds with the appropriate data stream.

---

## 🇫🇮 Suomi — Roolit ja näkymät

LiveLyricSync tukee useita muusikkoroolia, joilla jokaisella on oma räätälöity näkymä.  
Kaikki laitteet pysyvät synkassa WebSocket‑serverin kautta, mutta jokainen rooli saa erilaista dataa tarpeidensa mukaan.

---

## 1. Näyttöroolit

### Laulajat (Lead / Taustat)
Näyttää:
- Lyriikit
- Osamerkinnät (Intro, Säkeistö, Kertsi, Bridge)
- Stemmojen värikoodit
- Jaetut piirrosmerkinnät

---

### Basisti
Näyttää:
- Nuotit tai tabit
- Rakenne
- Cue‑merkinnät
- Jaetut piirrokset

---

### Kitaristi
Näyttää:
- Sointumerkit
- Komppikaavat
- Osasiirtymät
- Jaetut piirrokset

---

### Rumpali
Näyttää:
- Klikki / tempo
- Cue‑tekstit
- Fill‑kohdat
- Jaetut piirrokset

---

## 2. Ohjausroolit

### Ohjaintabletti (Pääohjain)
Voi:
- Hypätä biisin osiin
- Loopata aikavälin
- Aloittaa/pysäyttää toiston
- Piirtää merkintöjä
- Vastaanottaa page turner ‑polkimen komennot

---

### Ohjaintabletti (Toissijainen)
Samat ominaisuudet, mutta vapaaehtoinen.

---

## 3. Jaettu piirtokerros

Kaikki laitteet näyttävät saman piirroskerroksen roolista riippumatta.

---

## 4. Roolin rekisteröinti

Jokainen laite ilmoittaa roolinsa serverille:

{ "role": "vocals" }
{ "role": "bass" }
{ "role": "guitar" }
{ "role": "drums" }
{ "role": "lyrics" }
{ "role": "control" }

Serveri lähettää oikean datavirran roolin mukaan.
