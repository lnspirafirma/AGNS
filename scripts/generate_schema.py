import json
import sys
from pathlib import Path

# Add project root to path so we can import agns_core
sys.path.append(str(Path(__file__).parent.parent))

from agns_core.models.cognitive_dsl import CognitiveDSL

def generate_schema():
    schema = CognitiveDSL.model_json_schema()
    output_path = Path(__file__).parent.parent / "agns_core" / "schemas" / "cognitive_dsl_v1.json"

    with open(output_path, "w") as f:
        json.dump(schema, f, indent=2)

    print(f"Schema generated at {output_path}")

if __name__ == "__main__":
    generate_schema()
