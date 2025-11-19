import pytz
from datetime import datetime
from app.auth.jwt import create_access_token, create_refresh_token
from app.database import get_mongo_db
from app.dto.common import JWTPayloadDto
from app.schemae.users import UserAuthModel
from app.dto.users import UserRegisterDto, UserCredentialDto, UserAuthResultDto
from passlib.hash import pbkdf2_sha256
from fastapi import HTTPException, status

class UserService:
  db = get_mongo_db()
  def __init__(self):
    self.col_user = self.db.users
    return

  def register(self, dto: UserRegisterDto):
    new_user = UserAuthModel(
      nickname=dto.email.split('@')[0],
      email=dto.email.lower(),
      created_at=datetime.now(pytz.UTC),
      pw_hash=pbkdf2_sha256.hash(dto.password),
      is_active=False,
      is_admin=False,
    )
    if self.col_user.find_one({ 'email': new_user.email }):
      raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    new_doc = self.col_user.insert_one(new_user.model_dump())
    new_user.id = new_doc.inserted_id
    return new_user
  
  def login(self, dto: UserCredentialDto):
    target_user_doc = self.col_user.find_one({ 'email': dto.email.lower() })
    if not target_user_doc:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    target_user = UserAuthModel(**target_user_doc)
    if not pbkdf2_sha256.verify(dto.password, target_user.pw_hash):
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    jwt_payload = JWTPayloadDto(
      user_id=str(target_user.id),
      is_admin=bool(target_user.is_admin),
      is_active=bool(target_user.is_active),
    )
    return UserAuthResultDto(
      access_token=create_access_token(jwt_payload.model_dump()),
      refresh_token=create_refresh_token(jwt_payload.model_dump()),
      apihost_ts=datetime.now(pytz.UTC),
    )
