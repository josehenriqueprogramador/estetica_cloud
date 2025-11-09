from fastapi import FastAPI
from app.routes import auth, clientes, dashboard, empresas, funcionarios, servicos

app = FastAPI()

# Incluir routers
app.include_router(auth.router)
app.include_router(clientes.router)
app.include_router(dashboard.router)
app.include_router(empresas.router)
app.include_router(funcionarios.router)
app.include_router(servicos.router)
