import yaml
from pathlib import Path
from .lesson import LessonPack

LESSON_DIR = Path(__file__).parent.parent / "lessons"

def load_lesson(name: str) -> LessonPack:
    path = LESSON_DIR / f"{name}.yaml"
    data = yaml.safe_load(path.read_text())
    return LessonPack(**data)
