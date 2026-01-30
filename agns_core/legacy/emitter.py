# LEGACY: Conceptual prototype, not part of AGNS-Core runtime
import orjson
from fastapi.responses import Response
from .schemas import CognitiveDSL

class CognitiveEmitter:
    """
    4.4 Cognitive Emitter
    Role: Final output transmission
    """

    @staticmethod
    def emit(dsl: CognitiveDSL) -> Response:
        # Dump using orjson for performance
        # OPT_NON_STR_KEYS is useful if dictionary keys are not strings,
        # though Pydantic usually ensures string keys for JSON.
        json_bytes = orjson.dumps(dsl.model_dump(), option=orjson.OPT_NON_STR_KEYS)

        return Response(content=json_bytes, media_type="application/json")
