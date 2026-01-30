from .base import Reasoner
from ..cognition.lesson import LessonPack

class MockReasoner:
    async def reason(self, lesson: LessonPack, payload: dict) -> dict:
        # Deterministic, rule-abiding output
        return {
            "rule_id": "morph_reasoning_01",
            "intent": lesson.intent_category,
            "manifestation": {
                "shape": lesson.morphology_rules["base_shape"],
                "motion": lesson.morphology_rules["motion"],
                "energy": min(payload.get("energy", 0.7), lesson.guardrails["max_energy"]),
                "color_palette": lesson.morphology_rules["allowed_colors"],
            },
            "reasoning": {
                "principle": lesson.principles["core"],
                "explanation": lesson.principles["logic"],
            }
        }
