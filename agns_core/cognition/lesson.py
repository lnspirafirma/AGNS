from typing import Union

from agns_core.cognition.lesson_v1 import (
    LessonPackV1,
    LessonHeader,
    LessonCurriculum,
    LessonMorphology,
    LessonChromatics,
    LessonTone,
)
from agns_core.cognition.lesson_v2 import LessonPackV2

# Unified Type for LessonPack
# The system will automatically determine V1 vs V2 based on field structure
# V1 has 'morphology' and 'chromatics'
# V2 has 'decision_rules' and 'telemetry_hints'
LessonPack = Union[LessonPackV1, LessonPackV2]
