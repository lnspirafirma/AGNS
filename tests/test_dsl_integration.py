import sys
import json
import asyncio
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from agns_core.gateway.mock_reasoner import MockReasoner
from agns_core.models.cognitive_dsl import CognitiveDSL, IntentCategory

async def test_integration():
    print("Testing MockReasoner with new Cognitive DSL...")

    reasoner = MockReasoner()

    # Test valid intent
    print("Reasoning for DEEP_ANALYSIS...")
    dsl = await reasoner.reason(IntentCategory.deep_analysis)

    print("Validating model...")
    assert isinstance(dsl, CognitiveDSL)
    print("Model is valid CognitiveDSL instance.")

    json_output = dsl.model_dump(mode='json')
    print(json.dumps(json_output, indent=2))

    # Verify specific fields
    assert dsl.intent.category == IntentCategory.deep_analysis
    assert dsl.manifestation.color_palette.primary == "#800080"
    assert dsl.telemetry.source == "agns_core"

    print("Integration test passed!")

if __name__ == "__main__":
    asyncio.run(test_integration())
