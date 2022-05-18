from fastapi import FastAPI
from src.main.routes import auth_routes

app = FastAPI()

# Configuração inicial do Projeto

app.include_router(auth_routes)
