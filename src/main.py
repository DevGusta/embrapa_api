from fastapi import FastAPI
from src.routes.data_routes import router as data_router
from src.routes.auth_routes import router as auth_router
from src.database.database import init_db


init_db()
app = FastAPI(
    title="Tech Challenge Embrapa",
    description="API feita para o Tech Challenge Fase 1 da Pós Tech de Machine Learning Engineering",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.include_router(data_router)
app.include_router(auth_router)

@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Bem-vindo à API Tech Challenge Embrapa"}

