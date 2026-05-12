# LSC Platform

Plataforma de cualificación docente en inclusión auditiva para instituciones educativas, apoyada en cocreación de contenidos interactivos en Lengua de Señas Colombiana (LSC).

## Stack Tecnológico

- Frontend: Next.js 14 + TypeScript + Tailwind CSS
- Backend: Python 3.11 + FastAPI
- Base de datos: PostgreSQL 15
- Infraestructura: Docker + Docker Compose

## Equipo

Grupo 1 - Universidad Tecnológica de Bolívar
Juan Salas - Natalia Pérez - Paula Márquez - Alain Medina

---

## Requisitos previos

- Python 3.11
- PostgreSQL 15 (instalado con Homebrew)
- Node.js 20

---

## 1. Base de datos

Iniciar PostgreSQL:
```bash
brew services start postgresql@15
```

Detener PostgreSQL:
```bash
brew services stop postgresql@15
```

Primera vez - crear la base de datos:
```bash
psql postgres -c "CREATE USER lsc_user WITH PASSWORD 'lsc_password';"
psql postgres -c "CREATE DATABASE lsc_platform OWNER lsc_user;"
psql postgres -c "GRANT ALL PRIVILEGES ON DATABASE lsc_platform TO lsc_user;"
```

---

## 2. Backend (FastAPI)

Entrar a la carpeta e iniciar el entorno virtual:
```bash
cd backend
source venv/bin/activate
```

Instalar dependencias (solo la primera vez):
```bash
pip install -r requirements.txt
```

Correr el servidor:
```bash
uvicorn app.main:app --reload
```

El servidor queda disponible en:
- API: http://localhost:8000
- Documentacion interactiva: http://localhost:8000/docs
- Health check: http://localhost:8000/health

Detener el servidor:
Salir del entorno virtual:
```bash
deactivate
```

---

## 3. Frontend (Next.js) - proximamente

```bash
cd frontend
npm install
npm run dev
```

Disponible en: http://localhost:3000

---

## Endpoints disponibles

| Metodo | Endpoint | Descripcion |
|--------|----------|-------------|
| GET | / | Estado de la API |
| GET | /health | Health check |
| POST | /api/v1/auth/registro | Registro de docente (RF-01) |
| POST | /api/v1/auth/login | Login con JWT (RF-02) |

---

## Autenticacion

La API usa JWT (JSON Web Tokens). Para endpoints protegidos:

1. Haz login en POST /api/v1/auth/login
2. Copia el access_token de la respuesta
3. Incluyelo en el header: Authorization: Bearer <token>

---

## Flujo de desarrollo con Git

Siempre trabajar desde develop:
```bash
git checkout develop
```

Crear rama para nueva funcionalidad:
```bash
git checkout -b feature/nombre-feature
```

Hacer commit:
```bash
git add .
git commit -m "feat: descripcion del cambio"
```

Subir al repo:
```bash
git push origin feature/nombre-feature
```
