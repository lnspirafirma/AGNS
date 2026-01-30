from __future__ import annotations

from typing import Literal, Tuple
from enum import Enum
from pydantic import BaseModel, Field, confloat


# ==========================================================
# ENUMS (Closed World Assumption)
# ==========================================================

class DSLVersion(str, Enum):
    v1_0 = "1.0"


class IntentCategory(str, Enum):
    deep_analysis = "deep_analysis"
    exploration = "exploration"
    idle = "idle"


class LightLayer(str, Enum):
    flux = "flux"
    color = "color"
    crystal = "crystal"


class BaseShape(str, Enum):
    spiral_vortex = "spiral_vortex"
    nebula = "nebula"
    sphere = "sphere"


class MotionDynamics(str, Enum):
    centripetal_acceleration = "centripetal_acceleration"
    laminar_flow = "laminar_flow"
    static = "static"


# ==========================================================
# CORE BLOCKS
# ==========================================================

class Intent(BaseModel):
    category: IntentCategory
    confidence: confloat(ge=0.0, le=1.0)

    class Config:
        extra = "forbid"


class CognitiveState(BaseModel):
    thinking_level: confloat(ge=0.0, le=1.0)
    entropy: confloat(ge=0.0, le=1.0)
    coherence: confloat(ge=0.0, le=1.0)
    pulse_hz: confloat(gt=0.0, le=20.0)
    vector: Tuple[confloat(ge=-1.0, le=1.0), confloat(ge=-1.0, le=1.0)]
    temperature: confloat(ge=0.0, le=1.0)

    class Config:
        extra = "forbid"


class ColorPalette(BaseModel):
    primary: str = Field(..., pattern=r"^#[0-9A-Fa-f]{6}$")
    secondary: str = Field(..., pattern=r"^#[0-9A-Fa-f]{6}$")

    class Config:
        extra = "forbid"


class Manifestation(BaseModel):
    layer: LightLayer
    base_shape: BaseShape
    motion_dynamics: MotionDynamics
    color_palette: ColorPalette

    class Config:
        extra = "forbid"


class Telemetry(BaseModel):
    timestamp_ms: int
    source: Literal["agns_core"]
    deterministic_hash: str

    class Config:
        extra = "forbid"


# ==========================================================
# ROOT DSL OBJECT
# ==========================================================

class CognitiveDSL(BaseModel):
    dsl_version: DSLVersion
    intent: Intent
    cognitive_state: CognitiveState
    manifestation: Manifestation
    telemetry: Telemetry

    class Config:
        extra = "forbid"
