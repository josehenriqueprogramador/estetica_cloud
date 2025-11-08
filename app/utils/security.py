from passlib.context import CryptContext

# Configura o esquema de hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Gera o hash da senha usando bcrypt"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica se a senha informada confere com o hash armazenado"""
    return pwd_context.verify(plain_password, hashed_password)
