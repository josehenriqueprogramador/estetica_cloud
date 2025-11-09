from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

env = os.getenv("APP_ENV", "local")
DATABASE_URL = os.getenv("DATABASE_URL_LOCAL") if env == "local" else os.getenv("DATABASE_URL_PROD")

if not DATABASE_URL:
    raise ValueError(f"DATABASE_URL não definido para ambiente {env}")

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

