from fastapi import Request, HTTPException
from pydantic import ValidationError
from agns_core.models.cognitive_dsl import CognitiveDSL
import orjson
from starlette.responses import Response

async def dsl_validation_middleware(request: Request, call_next):
    response = await call_next(request)

    path = request.url.path
    # Applying to /think as well since that is the implemented endpoint
    if path.startswith("/emit") or path.startswith("/think"):
        try:
            # Capture the response body
            body_chunks = []
            async for chunk in response.body_iterator:
                body_chunks.append(chunk)
            body = b"".join(body_chunks)

            if body:
                payload = orjson.loads(body)
                # Parse and validate against the Pydantic model
                CognitiveDSL.model_validate(payload)

            # Reconstruct the response
            return Response(
                content=body,
                status_code=response.status_code,
                headers=dict(response.headers),
                media_type=response.media_type
            )

        except ValidationError as e:
            # If validation fails, return a 500 error
            # Note: This overrides the original success response
            return Response(
                content=orjson.dumps({"detail": f"Cognitive DSL violation: {e}"}),
                status_code=500,
                media_type="application/json"
            )

    return response
