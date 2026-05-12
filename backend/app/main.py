from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import api_router
from app.core.database import engine
from app.models import usuario

usuario.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LSC Platform API",
    description="API REST para la plataforma de cualificación docente en inclusión auditiva",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "LSC Platform API v1.0", "status": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}
