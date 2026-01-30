def validate_dsl(dsl: dict, lesson) -> None:
    forbidden = lesson.guardrails.get("forbid_colors", [])
    for color in dsl["manifestation"]["color_palette"]:
        if color in forbidden:
            raise ValueError(f"Forbidden color detected: {color}")
