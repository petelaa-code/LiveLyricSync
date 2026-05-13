# Audio Input Layer (placeholder)
# This module will later handle:
# - WASAPI / ASIO audio capture
# - Buffering
# - Downmixing to mono
# - Normalization
# - Frame generator for alignment engine

class AudioInput:
    def __init__(self):
        pass

    def start(self):
        # TODO: Initialize audio device
        pass

    def read_frame(self):
        # TODO: Return PCM audio frame
        return None
