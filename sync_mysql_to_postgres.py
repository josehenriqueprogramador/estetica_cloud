import pandas as pd
from sqlalchemy import create_engine

# Conexões
mysql_engine = create_engine("mysql+pymysql://root:@localhost/estetica_cloud")
pg_engine = create_engine("postgresql+psycopg2://db_a3m8_user:9Kkk9oPT6VRTounXRgpYdrueRxEa94fi@dpg-d47r22c9c44c73ccebcg-a.oregon-postgres.render.com/db_a3m8")

# Tabelas que você quer copiar
tabelas = ["clientes", "empresas", "funcionarios", "reservas", "servicos"]

for tabela in tabelas:
    print(f"Copiando tabela {tabela}...")
    df = pd.read_sql_table(tabela, mysql_engine)
    df.to_sql(tabela, pg_engine, if_exists="replace", index=False)
    print(f"✅ {tabela} copiada com sucesso!")

print("🎉 Todas as tabelas foram copiadas para o PostgreSQL!")
