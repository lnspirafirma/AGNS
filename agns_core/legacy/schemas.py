# LEGACY: Conceptual prototype, not part of AGNS-Core runtime
from enum import Enum
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field, field_validator
from dataclasses import dataclass

# --- Ingestion Cortex Schemas ---

class IngestedContext(BaseModel):
    user_id: str
    transcript: str
    prosody: Dict[str, Any] = Field(default_factory=dict)
    device_tier: int = 1
    timestamp: float

# --- Logenesis Engine (Teacher) Schemas ---

@dataclass
class LessonPack:
    persona: str
    curriculum: List[str]
    constraints: List[str]
    examen: Dict[str, Any]

# --- Cognitive DSL (The Output Contract) ---

class ChromaticMode(str, Enum):
    BIT_24_RGB = "BIT_24_RGB"
    BIT_8_MONO = "BIT_8_MONO"
    HDR_LINEAR = "HDR_LINEAR"

class IntentVector(BaseModel):
    category: str
    energy_level: float = Field(ge=0.0, le=1.0)

class ColorPalette(BaseModel):
    primary: str
    secondary: str

class ParticlePhysics(BaseModel):
    turbulence: float = Field(ge=0.0, le=1.0)
    flow_direction: str

class VisualManifestation(BaseModel):
    base_shape: str
    color_palette: ColorPalette
    particle_physics: ParticlePhysics
    chromatic_mode: ChromaticMode

class CognitiveDSL(BaseModel):
    trace_id: str
    intent_vector: IntentVector
    visual_manifestation: VisualManifestation

    @field_validator("visual_manifestation")
    @classmethod
    def validate_physics(cls, v):
        if v.particle_physics.turbulence > 1.0:
            raise ValueError("Turbulence cannot exceed 1.0")
        return v
