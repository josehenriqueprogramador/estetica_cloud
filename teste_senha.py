from passlib.context import CryptContext

# Configuração do bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Simulação de senha que você quer cadastrar
senha = "30134410"  # troque por qualquer senha que queira testar

# Debug: mostrar senha e tamanho
print(f"[DEBUG] Senha recebida: '{senha}'")
print(f"[DEBUG] Len caracteres: {len(senha)}")
print(f"[DEBUG] Len bytes UTF-8: {len(senha.encode('utf-8'))}")

# Tentar gerar hash
try:
    hashed = pwd_context.hash(senha)
    print(f"[DEBUG] Hash gerado com sucesso: {hashed}")
except Exception as e:
    print(f"[ERROR] Problema ao gerar hash: {e}")
