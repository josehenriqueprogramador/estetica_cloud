from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from app.models.models import Cliente, Empresa
from app.database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/clientes/{empresa_id}")
def listar_clientes(request: Request, empresa_id: int, db=Depends(get_db)):
    clientes = db.query(Cliente).filter_by(empresa_id=empresa_id).all()
    empresa = db.query(Empresa).filter_by(id=empresa_id).first()
    return templates.TemplateResponse("clientes.html", {
        "request": request,
        "clientes": clientes,
        "empresa": empresa,
    })
