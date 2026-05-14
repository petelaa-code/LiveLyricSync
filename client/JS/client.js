const statusEl = document.getElementById("status");
const lyricEl = document.getElementById("lyric");

const ws = new WebSocket("ws://localhost:8765");

ws.onopen = () => {
    statusEl.textContent = "Connected to LiveLyricSync server";
    statusEl.style.color = "#4caf50";
};

ws.onmessage = (event) => {
    lyricEl.textContent = JSON.parse(event.data);

};

ws.onclose = () => {
    statusEl.textContent = "Disconnected";
    statusEl.style.color = "#f44336";
};
