import time
import hashlib
from fastapi import APIRouter, Response
from ..cognition.curriculum import load_lesson
from ..gateway.mock_reasoner import MockReasoner
from ..models.cognitive_dsl import Telemetry
from ..emitter.dsl_emitter import emit

router = APIRouter()
reasoner = MockReasoner()

@router.post("/think/{lesson_name}")
async def think(lesson_name: str, payload: dict):
    lesson = load_lesson(lesson_name)
    dsl = await reasoner.reason(lesson, payload)

    # Inject Telemetry
    # We generate a deterministic hash based on the content so far (excluding telemetry)
    content_hash = hashlib.sha256(dsl.model_dump_json(exclude={'telemetry'}).encode()).hexdigest()

    dsl.telemetry = Telemetry(
        timestamp=time.time(),
        source="agns-core",
        deterministic_hash=content_hash
    )

    return Response(content=emit(dsl.model_dump()), media_type="application/json")
