import os
from passlib.hash import bcrypt

# Simula recebimento da senha do banco ou formulário
senha = os.getenv("SENHA_TESTE", "30134410")

# Mostra o valor real da senha
print("[DEBUG] Valor da senha (repr):", repr(senha))
print("[DEBUG] Len caracteres:", len(senha))
print("[DEBUG] Len bytes UTF-8:", len(senha.encode('utf-8')))

# Gera hash
try:
    hash_senha = bcrypt.hash(senha)
    print("[DEBUG] Hash gerado com sucesso:", hash_senha)
except Exception as e:
    print("[ERROR] Ocorreu um erro ao gerar o hash:", e)
