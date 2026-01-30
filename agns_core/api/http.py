from fastapi import APIRouter, Response
from ..cognition.curriculum import load_lesson
from ..gateway.mock_reasoner import MockReasoner
from ..cognition.validator import validate_dsl
from ..emitter.dsl_emitter import emit

router = APIRouter()
reasoner = MockReasoner()

@router.post("/think/{lesson_name}")
async def think(lesson_name: str, payload: dict):
    lesson = load_lesson(lesson_name)
    dsl = await reasoner.reason(lesson, payload)
    validate_dsl(dsl, lesson)
    return Response(content=emit(dsl), media_type="application/json")
