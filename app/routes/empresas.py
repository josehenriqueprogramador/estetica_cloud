from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Empresa
from app.utils.security import hash_password

router = APIRouter(prefix="", tags=["empresas"])
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    """Página inicial: cadastro de novas empresas"""
    return templates.TemplateResponse("home.html", {"request": request})

@router.post("/empresas")
def criar_empresa(
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    db: Session = Depends(get_db)
):
    """Cria nova empresa armazenando senha hashed"""
    existing = db.query(Empresa).filter(Empresa.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    empresa = Empresa(nome=nome, email=email, senha=hash_password(senha))
    db.add(empresa)
    db.commit()
    db.refresh(empresa)
    # após criar, redireciona para login
    return RedirectResponse(url="/login", status_code=303)
