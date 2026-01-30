from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional

from .ingestion import IngestionCortex
from .logenesis import LogenesisEngine
from .gateway import SynapticGateway, MockReasoner
from .emitter import CognitiveEmitter

app = FastAPI(title="AGNS-Core", version="0.1.0")

# Dependency Injection (Simple for now)
gateway = SynapticGateway(reasoner=MockReasoner())

class CognitiveRequest(BaseModel):
    user_id: str = "anonymous"
    transcript: str
    prosody: Dict[str, Any] = {}
    device_tier: int = 1
    # Client might send intent hint, or we infer it.
    # For this prototype, we assume the system infers "deep_analysis"
    # or the client requests it implicitly.
    intent_hint: Optional[str] = "deep_analysis"

@app.post("/v1/cognition/process")
async def process_cognition(request: CognitiveRequest):
    """
    Main Cognitive Pipeline:
    1. Ingestion -> Context
    2. Logenesis -> Lesson Pack
    3. Gateway -> Reasoning -> Validated DSL
    4. Emitter -> JSON Response
    """
    try:
        # 1. Ingestion Cortex
        # Convert Pydantic model to dict for ingestion
        raw_data = request.model_dump()
        context = IngestionCortex.ingest(raw_data)

        # 2. Logenesis Engine
        # In a real system, intent classification happens here.
        # For now, we use the hint or default.
        lesson_pack = LogenesisEngine.get_lesson(request.intent_hint)

        # 3. Synaptic Gateway
        validated_dsl = await gateway.process(context, lesson_pack)

        # 4. Cognitive Emitter
        return CognitiveEmitter.emit(validated_dsl)

    except Exception as e:
        # In production, specific exception handling and logging required
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "active", "system": "AGNS-Core"}
