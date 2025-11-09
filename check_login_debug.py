from app.database import get_db
from app.models import Empresa
from app.utils.security import pwd_context
from sqlalchemy.orm import Session

EMAIL = "alessandracoimbraestetica@gmail.com"
SENHA_TESTE = "30134410"

def main():
    db: Session = next(get_db())
    empresa = db.query(Empresa).filter(Empresa.email == EMAIL).first()
    if not empresa:
        print("Nenhuma empresa encontrada com este email.")
        return
    
    # Debug do hash que chega no verify
    print("HASH RECEBIDO:", repr(empresa.senha))
    print("TIPO:", type(empresa.senha))

    try:
        resultado = pwd_context.verify(SENHA_TESTE, empresa.senha)
        print("Verificação da senha:", resultado)
    except Exception as e:
        print("Erro no verify:", e)

if __name__ == "__main__":
    main()
