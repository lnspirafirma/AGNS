import time
from .schemas import IngestedContext

class IngestionCortex:
    """
    4.1 Ingestion Cortex
    Role: Receives raw data -> Creates Context
    "Doesn't think, just prepares context for the teacher."
    """

    @staticmethod
    def ingest(data: dict) -> IngestedContext:
        # Defaults for missing fields
        return IngestedContext(
            user_id=data.get("user_id", "anonymous"),
            transcript=data.get("transcript", ""),
            prosody=data.get("prosody", {}),
            device_tier=data.get("device_tier", 1),
            timestamp=data.get("timestamp", time.time())
        )
