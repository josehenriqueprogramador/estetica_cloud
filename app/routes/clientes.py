from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
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

@router.post("/clientes/{empresa_id}/novo")
def novo_cliente(
    request: Request,
    empresa_id: int,
    nome: str = Form(...),
    telefone: str = Form(...),
    db=Depends(get_db)
):
    cliente = Cliente(nome=nome, telefone=telefone, empresa_id=empresa_id)
    db.add(cliente)
    db.commit()
    return RedirectResponse(url=f"/clientes/{empresa_id}", status_code=303)
