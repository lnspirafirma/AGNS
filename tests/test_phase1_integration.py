import pytest
import asyncio
from agns_core.cognition.curriculum import load_lesson
from agns_core.gateway.phase1_reasoner import Phase1Reasoner
from agns_core.models.cognitive_dsl import CognitiveDSL, IntentCategory

@pytest.mark.asyncio
async def test_phase1_reasoner_integration():
    # 1. Load the LessonPack
    lesson = load_lesson("deep_analysis")
    assert lesson.header.id == "LP-002-DEEP-ANALYSIS"
    assert lesson.chromatics.tone == "Objective"

    # 2. Initialize Reasoner
    reasoner = Phase1Reasoner()

    # 3. Create Payload
    payload = {"input": "Analyze this data structure."}

    # 4. Execute Reasoner
    result = await reasoner.reason(lesson, payload)

    # 5. Assertions
    assert isinstance(result, CognitiveDSL)

    # Intent should be deep_analysis because lesson objective contains "analy"
    assert result.intent.category == IntentCategory.deep_analysis
    assert result.intent.confidence > 0.9

    # Temperature should be 0.1 because tone is Objective
    assert result.cognitive_state.temperature == 0.1

    # Check Determinism
    result2 = await reasoner.reason(lesson, payload)
    assert result.telemetry.deterministic_hash == result2.telemetry.deterministic_hash
    assert result.telemetry.timestamp_ms <= result2.telemetry.timestamp_ms
