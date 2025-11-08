from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import empresas, auth, dashboard, clientes, funcionarios, servicos
from app.database import engine
from app.models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Estética Cloud")
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/templates"), name="static")

app.include_router(auth.router)
app.include_router(empresas.router)
app.include_router(dashboard.router)
app.include_router(clientes.router)
app.include_router(funcionarios.router)
app.include_router(servicos.router)

@app.get("/")
def home():
    return {"msg": "API Estética Cloud rodando com sucesso 🚀"}
