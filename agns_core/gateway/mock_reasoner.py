import time
import hashlib
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


class MockReasoner:
    """
    Deterministic cognitive teacher.
    Emits ONLY valid Cognitive DSL v1.0.
    """

    async def reason(self, intent_category: IntentCategory) -> CognitiveDSL:
        # Note: The original prompt had synchronous 'reason', but 'base.py' Protocol defines async.
        # I will keep it async to match the protocol and application architecture.
        now_ms = int(time.time() * 1000)

        payload_fingerprint = f"{intent_category}:{now_ms}"
        digest = hashlib.sha256(payload_fingerprint.encode()).hexdigest()

        return CognitiveDSL(
            dsl_version=DSLVersion.v1_0,
            intent=Intent(
                category=intent_category,
                confidence=0.85,
            ),
            cognitive_state=CognitiveState(
                thinking_level=0.9,
                entropy=0.6,
                coherence=0.8,
                pulse_hz=6.0,
                vector=(0.0, 1.0),
                temperature=0.7,
            ),
            manifestation=Manifestation(
                layer=LightLayer.flux,
                base_shape=BaseShape.spiral_vortex,
                motion_dynamics=MotionDynamics.centripetal_acceleration,
                color_palette=ColorPalette(
                    primary="#800080",
                    secondary="#FFD700",
                ),
            ),
            telemetry=Telemetry(
                timestamp_ms=now_ms,
                source="agns_core",
                deterministic_hash=digest,
            ),
        )
