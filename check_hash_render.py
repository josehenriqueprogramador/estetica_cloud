import psycopg2

# Configurações do banco do Render
DB_HOST = "dpg-d47r22c9c44c73ccebcg-a.oregon-postgres.render.com"
DB_PORT = 5432
DB_NAME = "db_a3m8"
DB_USER = "db_a3m8_user"
DB_PASSWORD = "9Kkk9oPT6VRTounXRgpYdrueRxEa94fi"

EMPRESA_EMAIL = "alessandracoimbraestetica@gmail.com"  # ajuste se necessário

conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cur = conn.cursor()
cur.execute("SELECT id, email, senha FROM empresas WHERE email = %s", (EMPRESA_EMAIL,))
row = cur.fetchone()

if row:
    id, email, senha_hash = row
    print(f">>> Empresa encontrada: {id} {email}  repr(senha_hash): {repr(senha_hash)}")
    print(f"len caracteres: {len(senha_hash)}")
    print(f"len bytes UTF-8: {len(senha_hash.encode('utf-8'))}")
else:
    print("Nenhuma empresa encontrada com este email.")

cur.close()
conn.close()
