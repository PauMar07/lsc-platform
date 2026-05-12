from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from app.models.usuario import NivelDocente, EstadoDocente

class UsuarioRegistro(BaseModel):
    nombre: str
    email: EmailStr
    institucion: str
    area: str
    password: str

class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str

class UsuarioRespuesta(BaseModel):
    id: int
    nombre: str
    email: str
    institucion: str
    area: str
    nivel: Optional[NivelDocente]
    estado: EstadoDocente
    es_admin: bool
    creado_en: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
    usuario: UsuarioRespuesta
