#!/usr/bin/env python3

import os
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils.security import verify_password
from app.models.models import Empresa

# Configura a sessão do SQLAlchemy
db: Session = next(get_db())

# Email e senha de teste
email_teste = "alessandracoimbraestetica@gmail.com"
senha_teste = "30134410"

# Busca a empresa pelo email
empresa = db.query(Empresa).filter(Empresa.email == email_teste).first()

if empresa:
    print(f">>> Empresa encontrada: {empresa.id} {empresa.email}")
    print(f"repr(senha_hash): {repr(empresa.senha)}")
    print(f"len caracteres: {len(empresa.senha)}")
    print(f"len bytes UTF-8: {len(empresa.senha.encode('utf-8'))}")

    # Verifica a senha
    if verify_password(senha_teste, empresa.senha):
        print("✅ Senha verificada com sucesso!")
    else:
        print("❌ Senha incorreta!")
else:
    print("Nenhuma empresa encontrada com este email.")
