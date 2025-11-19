import pytz
from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.schemae.common import PyObjectId

class UserInfoModel(BaseModel):
  id: Optional[PyObjectId] = Field(default=None, alias="_id")
  nickname: Optional[str]
  email: EmailStr
  created_at: datetime = Field(default_factory=lambda: datetime.now(pytz.UTC))
  class Config:
    validate_by_name = True
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}

class UserAuthModel(UserInfoModel):
  pw_hash: str
  is_active: bool = Field(default=False)
  is_admin: bool = Field(default=False)
