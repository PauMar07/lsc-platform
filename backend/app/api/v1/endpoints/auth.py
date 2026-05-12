from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.usuario import UsuarioRegistro, UsuarioLogin, Token, UsuarioRespuesta
from app.services.auth_service import registrar_usuario, login_usuario

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/registro", response_model=UsuarioRespuesta, status_code=201)
def registro(datos: UsuarioRegistro, db: Session = Depends(get_db)):
    """RF-01: Registro de nuevo docente"""
    return registrar_usuario(db, datos)

@router.post("/login", response_model=Token)
def login(datos: UsuarioLogin, db: Session = Depends(get_db)):
    """RF-02: Autenticación de docente"""
    return login_usuario(db, datos.email, datos.password)
