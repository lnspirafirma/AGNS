import orjson

def emit(dsl: dict) -> bytes:
    return orjson.dumps(dsl, option=orjson.OPT_INDENT_2)
