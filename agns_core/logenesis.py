from typing import Dict
from .schemas import LessonPack

class LogenesisEngine:
    """
    4.2 Logenesis Engine (The Teacher)
    Role: Selects lesson, Assembles Lesson Pack, Creates System Prompt.
    """

    _LESSONS: Dict[str, LessonPack] = {
        "deep_analysis": LessonPack(
            persona="""You are a Photonic Engineer.
You translate intent into light, motion, and form.
You must obey the laws of Aetherium.""",
            curriculum=[
                "Deep analysis implies structured, high-energy cognitive load.",
                "Visuals should reflect complexity and depth.",
                "Use spiral or vortex shapes to signify drilling down into data."
            ],
            constraints=[
                "Do not use erratic or random motion.",
                "Colors must be coherent with the analysis intensity (e.g., Purple/Gold).",
                "Turbulence must be controlled (< 0.5)."
            ],
            examen={
                "task": "Generate a Cognitive DSL response reflecting deep analytical thought.",
                "required_fields": ["intent_vector", "visual_manifestation"]
            }
        )
    }

    @classmethod
    def get_lesson(cls, intent_key: str = "deep_analysis") -> LessonPack:
        # Default to deep_analysis for this prototype
        return cls._LESSONS.get(intent_key, cls._LESSONS["deep_analysis"])
