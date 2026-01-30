from fastapi import FastAPI
from .api.http import router

app = FastAPI(
    title="AGNS-Core",
    description="Aetherium Genesis Neural Server",
    version="0.1.0",
)

app.include_router(router)
