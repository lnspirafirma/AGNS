from typing import Protocol, Dict, Any
from ..cognition.lesson import LessonPack
from ..models.cognitive_dsl import CognitiveDSL

class Reasoner(Protocol):
    async def reason(self, lesson: LessonPack, payload: Dict[str, Any]) -> CognitiveDSL:
        ...
