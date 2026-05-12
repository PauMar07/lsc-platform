from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioRegistro
from app.core.security import hashear_password, verificar_password, crear_token_acceso

def registrar_usuario(db: Session, datos: UsuarioRegistro) -> Usuario:
    existe = db.query(Usuario).filter(Usuario.email == datos.email).first()
    if existe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un usuario con este correo institucional"
        )
    usuario = Usuario(
        nombre=datos.nombre,
        email=datos.email,
        institucion=datos.institucion,
        area=datos.area,
        hashed_password=hashear_password(datos.password)
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def login_usuario(db: Session, email: str, password: str):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario or not verificar_password(password, usuario.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas"
        )
    token = crear_token_acceso(data={"sub": usuario.email})
    return {"access_token": token, "token_type": "bearer", "usuario": usuario}
