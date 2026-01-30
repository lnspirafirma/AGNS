from enum import Enum
from typing import List, Optional, Literal
from pydantic import BaseModel, Field

class IntentCategory(str, Enum):
    IDLE = "idle"
    DEEP_ANALYSIS = "deep_analysis"
    REFLECTION = "reflection"
    DECISION = "decision"

class Intent(BaseModel):
    category: IntentCategory
    confidence: float = Field(..., ge=0.0, le=1.0)
    activation_rule: str

    model_config = {"extra": "forbid"}

class CognitiveState(BaseModel):
    thinking_level: float = Field(..., ge=0.0, le=1.0)
    entropy: float = Field(..., ge=0.0, le=1.0)
    coherence: float = Field(..., ge=0.0, le=1.0)
    energy_level: float = Field(..., ge=0.0, le=1.0)
    pulse_hz: float = Field(..., ge=0.0)
    vector: List[float] = Field(..., min_length=2, max_length=2)

    model_config = {"extra": "forbid"}

class ManifestationLayer(str, Enum):
    FLUX = "flux"
    COLOR = "color"
    CRYSTAL = "crystal"

class BaseShape(str, Enum):
    SPIRAL_VORTEX = "spiral_vortex"
    NEBULA = "nebula"
    SPHERE = "sphere"
    WAVE = "wave"

class MotionType(str, Enum):
    CENTRIPETAL = "centripetal"
    RADIAL = "radial"
    OSCILLATORY = "oscillatory"

class Motion(BaseModel):
    type: MotionType
    acceleration: float

    model_config = {"extra": "forbid"}

class ColorMode(str, Enum):
    ADDITIVE_LIGHT = "additive_light"

class ColorPalette(BaseModel):
    primary: List[int] = Field(..., min_length=3, max_length=3)
    secondary: List[int] = Field(..., min_length=3, max_length=3)

    model_config = {"extra": "forbid"}

class ColorModel(BaseModel):
    mode: ColorMode
    palette: ColorPalette

    model_config = {"extra": "forbid"}

class Manifestation(BaseModel):
    layer: ManifestationLayer
    base_shape: BaseShape
    motion: Motion
    color_model: ColorModel

    model_config = {"extra": "forbid"}

class ResourceLimits(BaseModel):
    cpu_ms: int
    gpu_ms: int

    model_config = {"extra": "forbid"}

class Constraints(BaseModel):
    allow_color: bool = True
    max_brightness: Optional[float] = Field(None, ge=0.0, le=1.0)
    forbidden_shapes: Optional[List[str]] = None
    resource_limits: Optional[ResourceLimits] = None

    model_config = {"extra": "forbid"}

class Telemetry(BaseModel):
    timestamp: float
    source: str
    deterministic_hash: str

    model_config = {"extra": "forbid"}

class CognitiveDSL(BaseModel):
    dsl_version: Literal["1.0"] = "1.0"
    lesson_id: str
    intent: Intent
    cognitive_state: CognitiveState
    manifestation: Manifestation
    constraints: Constraints
    telemetry: Optional[Telemetry] = None

    model_config = {"extra": "forbid"}
