import yaml
import logging
from pathlib import Path
from pydantic import ValidationError
from .lesson import LessonPack

logger = logging.getLogger("AGNS.Curriculum")
LESSON_DIR = Path(__file__).parent.parent / "lessons"

def load_lesson(name: str) -> LessonPack:
    """
    Loads a LessonPack from a YAML file.
    Validates it against the strict Pydantic schema.
    """
    path = LESSON_DIR / f"{name}.yaml"

    if not path.exists():
        raise FileNotFoundError(f"Lesson file not found: {path}")

    try:
        data = yaml.safe_load(path.read_text())
        lesson = LessonPack(**data)
        logger.info(f"Loaded LessonPack: {lesson.header.id} (v{lesson.header.version})")
        return lesson
    except ValidationError as e:
        logger.error(f"Schema Validation Failed for lesson '{name}': {e}")
        raise
    except yaml.YAMLError as e:
        logger.error(f"YAML Parsing Failed for lesson '{name}': {e}")
        raise
