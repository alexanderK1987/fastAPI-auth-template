from typing import Optional
from pydantic import BaseModel, EmailStr
from app.dto.common import ServerTSTemplateDto

class UserAuthResultDto(ServerTSTemplateDto):
  access_token: str
  refresh_token: str

class UserCredentialDto(BaseModel):
  email: EmailStr
  password: str

class UserRegisterDto(UserCredentialDto):
  pass # same

class QueryUserDto(BaseModel):
  email: Optional[str]
  