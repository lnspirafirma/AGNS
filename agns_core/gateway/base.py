from typing import Protocol, Dict, Any
from ..cognition.lesson import LessonPack

class Reasoner(Protocol):
    async def reason(self, lesson: LessonPack, payload: Dict[str, Any]) -> Dict[str, Any]:
        ...
