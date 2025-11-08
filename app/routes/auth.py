from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Empresa
from app.utils.security import verify_password

router = APIRouter(prefix="", tags=["auth"])
templates = Jinja2Templates(directory="app/templates")

@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
def login_empresa(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...),
    db: Session = Depends(get_db)
):
    empresa = db.query(Empresa).filter(Empresa.email == email).first()
    if not empresa:
        return templates.TemplateResponse("login.html", {"request": request, "erro": "Empresa não encontrada"})
    if not verify_password(senha, empresa.senha):
        return templates.TemplateResponse("login.html", {"request": request, "erro": "Senha incorreta"})
    return RedirectResponse(url=f"/dashboard/{empresa.id}", status_code=303)
