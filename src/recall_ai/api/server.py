from fastapi import FastAPI
from pydantic import BaseModel

class IngestRequest(BaseModel):
    text: str

def create_app() -> FastAPI:
    app = FastAPI()

    @app.get("/health")
    async def health_check():
        return {"status": "ok"}
    
    @app.post("/ingest", status_code=202)
    async def ingest(payload: IngestRequest):
        print(f"Ingesting text: {payload.text}")
        return {"accepted": True}

    return app