import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Lê o ambiente atual (local ou produção)
APP_ENV = os.getenv("APP_ENV", "local").lower()

# Monta a URL do banco de acordo com o ambiente
if APP_ENV == "production":
    DATABASE_URL = os.getenv("DATABASE_URL_PROD")
    print("🌐 Ambiente de produção detectado: Render (PostgreSQL)")
else:
    DATABASE_URL = os.getenv("DATABASE_URL_LOCAL")
    print("💻 Ambiente local detectado: Termux (MySQL)")

# Verifica se a URL foi configurada
if not DATABASE_URL:
    raise ValueError("❌ Nenhuma URL de banco de dados configurada no .env!")

# Cria o engine do SQLAlchemy
engine = create_engine(DATABASE_URL, echo=False)

# Cria sessão e base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependência de sessão para rotas FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
