from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.models import Empresa, Servico
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/servicos/{empresa_id}")
def listar_servicos(request: Request, empresa_id: int):
    db: Session = SessionLocal()
    empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    servicos = db.query(Servico).filter(Servico.empresa_id == empresa_id).all()
    db.close()
    return templates.TemplateResponse(
        "servicos.html",
        {"request": request, "empresa": empresa, "servicos": servicos}
    )

@router.post("/servicos/{empresa_id}/novo")
def novo_servico(request: Request, empresa_id: int, nome: str = Form(...), preco: float = Form(...), descricao: str = Form("")):
    db: Session = SessionLocal()
    servico = Servico(nome=nome, preco=preco, descricao=descricao, empresa_id=empresa_id)
    db.add(servico)
    db.commit()
    db.close()
    return RedirectResponse(f"/servicos/{empresa_id}", status_code=303)

@router.get("/servicos/{empresa_id}/excluir/{servico_id}")
def excluir_servico(request: Request, empresa_id: int, servico_id: int):
    db: Session = SessionLocal()
    servico = db.query(Servico).filter(Servico.id == servico_id, Servico.empresa_id == empresa_id).first()
    if servico:
        db.delete(servico)
        db.commit()
    db.close()
    return RedirectResponse(f"/servicos/{empresa_id}", status_code=303)
