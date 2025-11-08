from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Empresa, Cliente, Funcionario, Servico

router = APIRouter(prefix="", tags=["dashboard"])
templates = Jinja2Templates(directory="app/templates")

@router.get("/dashboard/{empresa_id}", response_class=HTMLResponse)
def dashboard(request: Request, empresa_id: int, db: Session = Depends(get_db)):
    empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    if not empresa:
        return RedirectResponse(url="/login", status_code=303)

    total_clientes = db.query(Cliente).filter_by(empresa_id=empresa_id).count()
    total_funcionarios = db.query(Funcionario).filter_by(empresa_id=empresa_id).count()
    total_servicos = db.query(Servico).filter_by(empresa_id=empresa_id).count()

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "empresa": empresa,
        "clientes": total_clientes,
        "funcionarios": total_funcionarios,
        "servicos": total_servicos,
    })
