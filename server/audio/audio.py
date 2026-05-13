import time

# Audio Input Layer (placeholder)
# Tämä moduuli tulee myöhemmin käsittelemään:
# - WASAPI / ASIO audio capture
# - Puskurointi
# - Downmix mono
# - Normalisointi
# - Kehysten generointi alignment engineä varten

class AudioInput:
    def __init__(self):
        self.frame_index = 0

    def start(self):
        # TODO: Initialize audio device
        pass

    def read_frame(self):
        # TODO: Return PCM audio frame
        return None

    def get_frame(self):
        # Testikehys, jotta pipeline voidaan rakentaa
        frame = {
            "index": self.frame_index,
            "timestamp": time.time(),
            "data": None  # ei vielä oikeaa audiota
        }
        self.frame_index += 1
        return frame
