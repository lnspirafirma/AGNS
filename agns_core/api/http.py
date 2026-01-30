from fastapi import APIRouter, Response
from ..gateway.mock_reasoner import MockReasoner
from ..models.cognitive_dsl import IntentCategory
from ..emitter.dsl_emitter import emit

router = APIRouter()
reasoner = MockReasoner()

@router.post("/think/{intent_category}")
async def think(intent_category: IntentCategory):
    # Simplified endpoint to match the new simplified MockReasoner logic
    # which now takes just an IntentCategory.
    # The original LessonPack logic is superseded by the "Lawkeeper" specific code
    # which hardcodes the mapping in MockReasoner for now.

    dsl = await reasoner.reason(intent_category)
    return Response(content=emit(dsl.model_dump()), media_type="application/json")
