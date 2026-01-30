from typing import List, Any
from .base import Reasoner
from ..cognition.lesson import LessonPack
from ..models.cognitive_dsl import (
    CognitiveDSL, Intent, IntentCategory, CognitiveState,
    Manifestation, ManifestationLayer, BaseShape, Motion, MotionType,
    ColorModel, ColorPalette, ColorMode, Constraints
)

class MockReasoner:
    def _hex_to_rgb(self, hex_color: str) -> List[int]:
        hex_color = hex_color.lstrip('#')
        return list(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    async def reason(self, lesson: LessonPack, payload: dict) -> CognitiveDSL:
        # Deterministic Logic

        # 1. Intent
        intent = Intent(
            category=IntentCategory(lesson.intent_category),
            confidence=0.82,
            activation_rule="morph_reasoning_01"
        )

        # 2. Cognitive State
        # Deterministic based on intent
        if lesson.intent_category == "deep_analysis":
            thinking_level = 0.87
            entropy = 0.62
            coherence = 0.74
            energy_level = 0.81
            pulse_hz = 3.2
            vector = [0.12, -0.44]
        else:
            # Default values for other intents
            thinking_level = 0.5
            entropy = 0.5
            coherence = 0.5
            energy_level = 0.5
            pulse_hz = 1.0
            vector = [0.0, 0.0]

        cognitive_state = CognitiveState(
            thinking_level=thinking_level,
            entropy=entropy,
            coherence=coherence,
            energy_level=energy_level,
            pulse_hz=pulse_hz,
            vector=vector
        )

        # 3. Manifestation
        base_shape_str = lesson.morphology_rules.get("base_shape", "sphere")
        motion_str = lesson.morphology_rules.get("motion", "radial")

        colors = lesson.morphology_rules.get("allowed_colors", ["#000000", "#FFFFFF"])
        if len(colors) < 2:
             colors = ["#000000", "#FFFFFF"]

        primary_rgb = self._hex_to_rgb(colors[0])
        secondary_rgb = self._hex_to_rgb(colors[1])

        manifestation = Manifestation(
            layer=ManifestationLayer.FLUX,
            base_shape=BaseShape(base_shape_str),
            motion=Motion(
                type=MotionType(motion_str),
                acceleration=0.7
            ),
            color_model=ColorModel(
                mode=ColorMode.ADDITIVE_LIGHT,
                palette=ColorPalette(
                    primary=primary_rgb,
                    secondary=secondary_rgb
                )
            )
        )

        # 4. Constraints
        guardrails = lesson.guardrails or {}
        # Mapping max_energy to max_brightness as a reasonable fallback
        max_brightness = guardrails.get("max_energy", 0.9)

        constraints = Constraints(
            allow_color=True,
            max_brightness=max_brightness,
            forbidden_shapes=None,
            resource_limits=None
        )

        # 5. Return DSL
        return CognitiveDSL(
            dsl_version="1.0",
            lesson_id=lesson.lesson_id,
            intent=intent,
            cognitive_state=cognitive_state,
            manifestation=manifestation,
            constraints=constraints,
            telemetry=None
        )
