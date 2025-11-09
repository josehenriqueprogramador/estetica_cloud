import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# -------------------------------
# Configuração do banco de dados
# -------------------------------
# Pegando variáveis de ambiente definidas no Render
DB_ENGINE = os.getenv("DB_ENGINE", "postgresql")
DB_USER = os.getenv("DB_USER", "db_a3m8_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "9Kkk9oPT6VRTounXRgpYdrueRxEa94fi")
DB_HOST = os.getenv("DB_HOST", "dpg-d47r22c9c44c73ccebcg-a.oregon-postgres.render.com")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "db_a3m8")

# -------------------------------
# Criando a URL de conexão
# -------------------------------
if DB_ENGINE == "postgresql":
    DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
else:
    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# -------------------------------
# Criando engine e sessão
# -------------------------------
engine = create_engine(
    DATABASE_URL,
    pool_recycle=280,  # recicla conexões antigas
    pool_pre_ping=True # reconecta automaticamente se cair
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# -------------------------------
# Função para obter sessão do banco
# -------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
