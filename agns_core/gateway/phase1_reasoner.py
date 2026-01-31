import time
import hashlib
from typing import Dict, Any
from ..cognition.lesson import LessonPack, LessonTone
from ..models.cognitive_dsl import (
    CognitiveDSL,
    DSLVersion,
    Intent,
    IntentCategory,
    CognitiveState,
    Manifestation,
    LightLayer,
    BaseShape,
    MotionDynamics,
    ColorPalette,
    Telemetry,
)

class Phase1Reasoner:
    """
    Phase 1 Target Implementation of the Reasoner.

    Adheres strictly to the AGNS Protocol:
    reason(lesson: LessonPack, payload: Dict) -> CognitiveDSL

    It operates deterministically (simulated cognition) based on the LessonPack curriculum.
    """

    async def reason(self, lesson: LessonPack, payload: Dict[str, Any]) -> CognitiveDSL:
        now_ms = int(time.time() * 1000)

        # 1. Intent Derivation
        # Map lesson objective to IntentCategory
        intent_category = IntentCategory.exploration # default
        obj_lower = lesson.curriculum.objective.lower()
        if "analy" in obj_lower:
            intent_category = IntentCategory.deep_analysis
        elif "idle" in obj_lower:
            intent_category = IntentCategory.idle

        # 2. Cognitive State Derivation
        # Map Chromatics to State
        temperature = 0.5
        if lesson.chromatics.tone == LessonTone.OBJECTIVE:
            temperature = 0.1
        elif lesson.chromatics.tone == LessonTone.DIRECT:
            temperature = 0.3
        elif lesson.chromatics.tone == LessonTone.EMPATHETIC:
            temperature = 0.7

        # 3. Deterministic Hash (Ground Truth)
        # Combine lesson ID + payload content to create a unique fingerprint
        payload_str = str(sorted(payload.items()))
        fingerprint = f"{lesson.header.id}:{lesson.header.version}:{payload_str}"
        digest = hashlib.sha256(fingerprint.encode()).hexdigest()

        return CognitiveDSL(
            dsl_version=DSLVersion.v1_0,
            intent=Intent(
                category=intent_category,
                confidence=0.99, # High confidence because we obey the lesson
            ),
            cognitive_state=CognitiveState(
                thinking_level=0.9,
                entropy=0.1, # Low entropy (high order)
                coherence=0.95,
                pulse_hz=10.0,
                vector=(0.5, 0.5),
                temperature=temperature,
            ),
            manifestation=Manifestation(
                layer=LightLayer.crystal, # Phase 1 default
                base_shape=BaseShape.nebula,
                motion_dynamics=MotionDynamics.laminar_flow,
                color_palette=ColorPalette(
                    primary="#0000FF", # Blue for logic
                    secondary="#FFFFFF"
                ),
            ),
            telemetry=Telemetry(
                timestamp_ms=now_ms,
                source="agns_core",
                deterministic_hash=digest,
            ),
        )
