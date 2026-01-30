from dataclasses import dataclass
from typing import Dict, Any

@dataclass(frozen=True)
class LessonPack:
    lesson_id: str
    intent_category: str
    description: str

    principles: Dict[str, str]
    morphology_rules: Dict[str, Any]
    guardrails: Dict[str, Any]
