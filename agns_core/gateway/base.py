from typing import Protocol, Dict, Any
from ..cognition.lesson import LessonPack
from ..models.cognitive_dsl import CognitiveDSL

class Reasoner(Protocol):
    """
    Gateway Protocol Definition (Phase B / Target State).

    This interface defines the contract for a fully-fledged AGNS Reasoner.
    In the target architecture, a Reasoner must accept:
      1. LessonPack: The curriculum/governance rules to apply.
      2. Payload: The runtime context/input data.

    NOTE:
        Current implementations (e.g., MockReasoner) are in a transitional
        Phase A state and may use a simplified signature (e.g., just IntentCategory)
        to prioritize Schema locking and hallucination prevention over full context handling.
    """
    async def reason(self, lesson: LessonPack, payload: Dict[str, Any]) -> CognitiveDSL:
        ...
