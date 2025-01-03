from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.core.config import Settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(
    data: dict,
    settings: Settings,
    expires_delta: Optional[timedelta] = None
):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm="HS256"
    )
    return encoded_jwt