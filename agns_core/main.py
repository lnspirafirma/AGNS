from fastapi import FastAPI
from .api.http import router
from .api.middleware import dsl_validation_middleware

app = FastAPI(
    title="AGNS-Core",
    description="Aetherium Genesis Neural Server",
    version="0.1.0",
)

app.middleware("http")(dsl_validation_middleware)
app.include_router(router)
