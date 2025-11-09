from passlib.context import CryptContext
from app.database import SessionLocal
from app.models.models import Empresa
import sys

pwd_context = CryptContext(schemes=["bcrypt","bcrypt_sha256"], deprecated="auto")

def main():
    db = SessionLocal()
    try:
        empresa = db.query(Empresa).order_by(Empresa.id).first()
        if not empresa:
            print("Nenhuma empresa encontrada no banco.", file=sys.stderr)
            return

        senha_hash = empresa.senha
        print(">>> Empresa encontrada:", empresa.id, empresa.email if hasattr(empresa, 'email') else "")
        print("repr(senha_hash):", repr(senha_hash))
        try:
            print("len caracteres:", len(senha_hash))
            print("len bytes UTF-8:", len(senha_hash.encode('utf-8')))
        except Exception as e:
            print("Erro ao medir tamanho:", e)

        # Tenta identificar/validar o hash sem conhecer a scheme
        try:
            # tenta verificar com uma senha de teste (adicione aqui a senha em texto se souber)
            exemplo_senha = "30134410"
            ok = pwd_context.verify(exemplo_senha, senha_hash)
            print("pwd_context.verify('30134410', hash) ->", ok)
        except Exception as e:
            print("Erro ao verificar hash com passlib:", type(e).__name__, e)

        # tentar identificar scheme/record (mais info de debug)
        try:
            rec = pwd_context._get_or_identify_record(senha_hash)
            print("Identified record:", rec)
        except Exception as e:
            print("Não foi possível identificar record com passlib:", type(e).__name__, e)

    finally:
        db.close()

if __name__ == "__main__":
    main()
