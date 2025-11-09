import os
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, text
from passlib.context import CryptContext

# Configuração do banco Render
DB_USER = "db_a3m8_user"
DB_PASSWORD = "9Kkk9oPT6VRTounXRgpYdrueRxEa94fi"
DB_HOST = "dpg-d47r22c9c44c73ccebcg-a.oregon-postgres.render.com"
DB_PORT = 5432
DB_NAME = "db_a3m8"
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Cria engine
engine = create_engine(DATABASE_URL)

# Cria contexto de hash
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Define metadata
metadata = MetaData()

# Define tabela empresas
empresas = Table(
    'empresas', metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String(255), nullable=False),
    Column('email', String(255), nullable=False, unique=True),
    Column('senha', String(255), nullable=False)
)

# Cria tabela se não existir
metadata.create_all(engine)

# Dados da empresa
nome = "Estetica Alessandra Coimbra"
email = "alessandracoimbraestetica@gmail.com"
senha = "30134410"
senha_trunc = senha[:72]
senha_hash = pwd_context.hash(senha_trunc)

with engine.connect() as conn:
    # Trunca a tabela e reinicia IDs
    conn.execute(text("TRUNCATE TABLE empresas RESTART IDENTITY CASCADE"))
    # Insere empresa
    conn.execute(empresas.insert().values(nome=nome, email=email, senha=senha_hash))
    print("Empresa criada com sucesso com id 1!")
    # Verifica hash
    assert pwd_context.verify(senha_trunc, senha_hash)
    print("Hash verificado com sucesso!")
