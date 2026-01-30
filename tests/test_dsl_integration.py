import sys
import json
import asyncio
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from agns_core.cognition.curriculum import load_lesson
from agns_core.gateway.mock_reasoner import MockReasoner
from agns_core.models.cognitive_dsl import CognitiveDSL

async def test_integration():
    print("Loading lesson...")
    lesson = load_lesson("deep_analysis")
    print(f"Lesson loaded: {lesson.lesson_id}")

    reasoner = MockReasoner()
    payload = {"energy": 0.8}

    print("Reasoning...")
    dsl = await reasoner.reason(lesson, payload)

    print("Validating model...")
    assert isinstance(dsl, CognitiveDSL)
    print("Model is valid CognitiveDSL instance.")

    json_output = dsl.model_dump(mode='json')
    print(json.dumps(json_output, indent=2))

    # Verify specific fields
    assert dsl.intent.category == "deep_analysis"
    assert dsl.manifestation.color_model.mode == "additive_light"
    assert len(dsl.manifestation.color_model.palette.primary) == 3

    print("Integration test passed!")

if __name__ == "__main__":
    asyncio.run(test_integration())
