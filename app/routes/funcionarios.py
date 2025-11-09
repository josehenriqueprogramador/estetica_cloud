from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from app.models.models import Funcionario, Empresa
from app.database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/funcionarios/{empresa_id}")
def listar_funcionarios(request: Request, empresa_id: int, db=Depends(get_db)):
    funcionarios = db.query(Funcionario).filter_by(empresa_id=empresa_id).all()
    empresa = db.query(Empresa).filter_by(id=empresa_id).first()
    return templates.TemplateResponse("funcionarios.html", {
        "request": request,
        "funcionarios": funcionarios,
        "empresa": empresa,
    })

@router.post("/funcionarios/{empresa_id}/novo")
def novo_funcionario(
    request: Request,
    empresa_id: int,
    nome: str = Form(...),
    cargo: str = Form(...),
    db=Depends(get_db)
):
    funcionario = Funcionario(nome=nome, cargo=cargo, empresa_id=empresa_id)
    db.add(funcionario)
    db.commit()
    return RedirectResponse(url=f"/funcionarios/{empresa_id}", status_code=303)
