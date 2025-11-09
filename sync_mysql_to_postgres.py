#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de migração de dados MySQL -> PostgreSQL
Compatível com SQLAlchemy 2.x
Limita campo senha a 72 bytes para bcrypt
"""

from sqlalchemy import create_engine, MetaData, Table, insert
from sqlalchemy.exc import SQLAlchemyError

# Configuração MySQL
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_HOST = "localhost"
MYSQL_DB = "estetica_cloud"

# Configuração PostgreSQL
POSTGRES_USER = "db_a3m8_user"
POSTGRES_PASSWORD = "9Kkk9oPT6VRTounXRgpYdrueRxEa94fi"
POSTGRES_HOST = "dpg-d47r22c9c44c73ccebcg-a.oregon-postgres.render.com"
POSTGRES_DB = "db_a3m8"
POSTGRES_PORT = "5432"

# Conexões
mysql_engine = create_engine(f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}")
postgres_engine = create_engine(f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}")

# Tabelas que serão migradas
TABLES = ["empresas", "clientes", "funcionarios", "servicos"]

def migrate_table(table_name):
    try:
        # Metadados MySQL
        mysql_meta = MetaData()
        mysql_meta.reflect(bind=mysql_engine)
        table = mysql_meta.tables[table_name]

        # Ler dados do MySQL
        with mysql_engine.connect() as mysql_conn:
            results = mysql_conn.execute(table.select()).all()

        # Preparar dados (limitar senha a 72 bytes)
        records = []
        for row in results:
            row_dict = dict(row._mapping)  # SQLAlchemy 2.x
            if "senha" in row_dict and row_dict["senha"]:
                row_dict["senha"] = row_dict["senha"][:72]
            records.append(row_dict)

        if not records:
            print(f"[INFO] Nenhum registro na tabela {table_name}")
            return

        # Inserir no PostgreSQL
        postgres_meta = MetaData()
        postgres_meta.reflect(bind=postgres_engine)
        pg_table = postgres_meta.tables[table_name]

        with postgres_engine.begin() as pg_conn:
            pg_conn.execute(insert(pg_table), records)

        print(f"[OK] Migrada tabela {table_name} ({len(records)} registros)")

    except SQLAlchemyError as e:
        print(f"[ERRO] Falha ao migrar tabela {table_name}: {e}")

if __name__ == "__main__":
    for t in TABLES:
        migrate_table(t)
