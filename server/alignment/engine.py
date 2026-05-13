import time

# Alignment Engine (placeholder)
# Tämä moduuli tulee myöhemmin tekemään:
# - Audio frame → tekstin kohdistus
# - Sanan tunnistus
# - Aikakoodien laskenta
# - Confidence-arvot

class AlignmentEngine:
    def __init__(self):
        self.start_time = time.time()

    def process_frame(self, frame):
        """
        Testilogiikka:
        - Laskee "position" ajan perusteella
        - Palauttaa sanan None (ei vielä oikeaa tunnistusta)
        """

        position = time.time() - self.start_time

        return {
            "position": position,
            "word": None
        }
