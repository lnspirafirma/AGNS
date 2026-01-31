from enum import Enum
from typing import List
from pydantic import BaseModel, ConfigDict


class LessonTone(str, Enum):
    FORMAL = "Formal"
    EMPATHETIC = "Empathetic"
    DIRECT = "Direct"
    OBJECTIVE = "Objective"


class LessonHeader(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    version: str
    title: str
    author: str


class LessonCurriculum(BaseModel):
    model_config = ConfigDict(extra="forbid")

    objective: str
    domain_knowledge: List[str]
    anti_patterns: List[str]


class LessonMorphology(BaseModel):
    model_config = ConfigDict(extra="forbid")

    required_components: List[str]
    prohibited_components: List[str]
    output_format: str  # e.g. "CognitiveDSL_v1"


class LessonChromatics(BaseModel):
    model_config = ConfigDict(extra="forbid")

    tone: LessonTone
    verbosity: str  # e.g. "Concise", "TokenLimit: 100"
    language: str   # e.g. "en-US"


class LessonPackV1(BaseModel):
    """
    LessonPack Specification (v1.0)
    The standard unit of instruction passed to the Reasoner.
    """
    model_config = ConfigDict(extra="forbid")

    header: LessonHeader
    curriculum: LessonCurriculum
    morphology: LessonMorphology
    chromatics: LessonChromatics
