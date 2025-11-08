from fastapi import APIRouter, Request, Depends
from app.database import get_db
from app.models.models import Servico, Empresa
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

@router.get("/servicos/{empresa_id}")
def listar_servicos(request: Request, empresa_id: int, db=Depends(get_db)):
    servicos = db.query(Servico).filter_by(empresa_id=empresa_id).all()
    empresa = db.query(Empresa).filter_by(id=empresa_id).first()
    return templates.TemplateResponse("servicos.html", {
        "request": request,
        "servicos": servicos,
        "empresa": empresa
    })
