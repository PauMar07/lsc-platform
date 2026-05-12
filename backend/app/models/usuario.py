from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from sqlalchemy.sql import func
import enum
from app.core.database import Base

class NivelDocente(str, enum.Enum):
    basico = "basico"
    intermedio = "intermedio"
    avanzado = "avanzado"

class EstadoDocente(str, enum.Enum):
    activo = "activo"
    certificado = "certificado"
    inactivo = "inactivo"

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    institucion = Column(String, nullable=False)
    area = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    nivel = Column(Enum(NivelDocente), nullable=True)
    estado = Column(Enum(EstadoDocente), default=EstadoDocente.activo)
    es_admin = Column(Boolean, default=False)
    creado_en = Column(DateTime(timezone=True), server_default=func.now())
    actualizado_en = Column(DateTime(timezone=True), onupdate=func.now())
