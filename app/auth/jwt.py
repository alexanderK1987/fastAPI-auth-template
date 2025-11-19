import pytz
import config
import jwt
from app.dto.common import JWTPayloadDto
from datetime import datetime, timedelta
from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def create_access_token(data: dict, expires_delta = timedelta(minutes=30)):
  to_encode = data.copy()
  expire = datetime.now(pytz.UTC) + expires_delta
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.JWT_AUTH_ALGORITHM)
  return encoded_jwt

def create_refresh_token(data: dict, expires_delta = timedelta(days=30)):
  to_encode = data.copy()
  to_encode["type"] = "refresh"
  expire = datetime.now(pytz.UTC) + expires_delta
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.JWT_AUTH_ALGORITHM)
  return encoded_jwt

def __decode_jwt_payload__(jwt_str) -> JWTPayloadDto:
  try:
    decoded_payload = jwt.decode(jwt_str, config.SECRET_KEY, algorithms=[config.JWT_AUTH_ALGORITHM])
    return JWTPayloadDto(**decoded_payload)
  except jwt.ExpiredSignatureError:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token expired")
  except jwt.InvalidTokenError:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token")

def get_current_jwt_payload(credentials: HTTPAuthorizationCredentials = Depends(security)) -> JWTPayloadDto:
  try:
    token = credentials.credentials
  except ValueError:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Authorization header")
  return __decode_jwt_payload__(token.strip())

def admin_only(user: JWTPayloadDto = Depends(get_current_jwt_payload)):
  if not getattr(user, "is_admin", False):
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Admin privileges required"
    )
  return user
