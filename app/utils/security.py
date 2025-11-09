from passlib.context import CryptContext

# Define o algoritmo de hash
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    """
    Gera o hash da senha com bcrypt.
    bcrypt suporta no máximo 72 bytes, então
    truncamos senhas maiores para evitar erro.
    """
    if not password:
        raise ValueError("A senha não pode estar vazia.")
    
    # Garante que não ultrapasse 72 bytes (limite do bcrypt)
    safe_password = password[:72]
    return pwd_context.hash(safe_password)

def verify_password(plain_password: str, hashed_password: str):
    """
    Verifica se a senha está correta.
    Também aplica truncagem antes da verificação.
    """
    if not plain_password or not hashed_password:
        return False
    
    safe_password = plain_password[:72]
    return pwd_context.verify(safe_password, hashed_password)

