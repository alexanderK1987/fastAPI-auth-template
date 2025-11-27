import pytz
from bson import ObjectId
from datetime import datetime
from pydantic import EmailStr, Field
from typing import Optional
from app.schemae.common import MongoBaseModel, PyObjectId

class UserInfoModel(MongoBaseModel):
  id: PyObjectId = None
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
