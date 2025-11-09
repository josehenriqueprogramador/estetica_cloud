from passlib.context import CryptContext
from passlib.handlers.bcrypt import bcrypt

# Contexto global do Passlib (apenas schemes)
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
    """Cria hash bcrypt para a senha fornecida"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica se a senha fornecida corresponde ao hash armazenado"""
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception:
        # fallback direto caso a identificação falhe
        return bcrypt.verify(plain_password, hashed_password)
