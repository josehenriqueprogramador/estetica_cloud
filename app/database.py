from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

# Define ambiente
env = os.getenv("APP_ENV", "local")

# Escolhe URL do banco e senha conforme ambiente
if env == "local":
    DATABASE_URL = os.getenv("DATABASE_URL_LOCAL")
    password = os.getenv("DB_PASSWORD_LOCAL", "")
else:
    DATABASE_URL = os.getenv("DATABASE_URL_PROD")
    password = os.getenv("DB_PASSWORD_PROD", "")

# Verifica se a URL foi realmente definida
if not DATABASE_URL:
    raise ValueError(f"DATABASE_URL não definido para ambiente '{env}'")

# Máscara da senha (opcional, apenas para logs)
masked_url = DATABASE_URL.replace(password, "***") if password else DATABASE_URL
print(f"[INFO] Conectando ao banco ({env}): {masked_url}")

# Cria engine
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Cria sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependência de sessão (FastAPI)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

