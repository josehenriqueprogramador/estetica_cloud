import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Detecta se está no Render (variável de ambiente RENDER)
IS_RENDER = os.getenv("RENDER", "false").lower() == "true"

if IS_RENDER:
    # Configuração para PostgreSQL no Render
    DB_USER = os.getenv("DB_USER", "render_user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "render_password")
    DB_HOST = os.getenv("DB_HOST", "render_postgres_host")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "render_database")
    DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
else:
    # Configuração local com MySQL
    DATABASE_URL = "mysql+pymysql://root:toor@localhost:3306/estetica_cloud"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
