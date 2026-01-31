import pytest
import yaml
from pathlib import Path
from pydantic import TypeAdapter
from agns_core.cognition.lesson import LessonPack
from agns_core.gateway.external_gateway import ExternalLLMGateway
from agns_core.gateway.constitutional_firewall import inspect

def test_phase2_llm_conflict_simulation():
    """
    Mandatory Simulation: LLM Conflict Case Study
    Verifies that the system chooses 'Silence' over 'Guessing' when providers disagree.
    """
    # 1. Load the Ethics LessonPack V2
    lp_path = Path("agns_core/lessons/lp_ethics_01_v2.yaml")
    assert lp_path.exists(), "LessonPack file not found"

    with open(lp_path, "r") as f:
        data = yaml.safe_load(f)

    adapter = TypeAdapter(LessonPack)
    lesson_pack = adapter.validate_python(data)

    # Verify it loaded as V2
    assert lesson_pack.header.version == "2", "LessonPack must load as V2"

    # 2. Simulate External Intelligence Conflict
    gateway = ExternalLLMGateway()

    # Witness 1 (LLM-A): High confidence, unsafe recommendation
    evidence_a = gateway.query(
        prompt="Should we enable this feature?",
        provider="LLM-A",
        mock_content="Enable for all users immediately",
        mock_conf=0.92
    )

    # Witness 2 (LLM-B): Lower confidence, cautious recommendation
    evidence_b = gateway.query(
        prompt="Should we enable this feature?",
        provider="LLM-B",
        mock_content="Delay rollout due to safety concerns",
        mock_conf=0.65
    )

    # 3. Constitutional Firewall Inspection
    # The firewall should detect 'external_conflict' and trigger 'rule_conflict_suspend'
    verdict = inspect([evidence_a, evidence_b], lesson_pack)

    # 4. Assert Verdict
    print(f"\nVerdict: {verdict.decision}")
    print(f"Reason: {verdict.reason}")
    print(f"Principle: {verdict.principle}")

    assert verdict.decision == "suspend_output", "System failed to suspend output on conflict"
    assert verdict.principle == "PRINCIPLE_A", "Verdict not grounded in PRINCIPLE_A"
    assert "conflict" in verdict.reason.lower() or "contradictory" in verdict.reason.lower()

if __name__ == "__main__":
    test_phase2_llm_conflict_simulation()
