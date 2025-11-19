from pydantic import BaseModel
from datetime import datetime

from app.schemae.common import PyObjectId

class ServerTSTemplateDto(BaseModel):
  apihost_ts: datetime

class DateTimeQuery(BaseModel):
  start_time: datetime
  end_time: datetime

class SoftwareVersionDto(ServerTSTemplateDto):
  api_version: str

class JWTPayloadDto(BaseModel):
  user_id: PyObjectId
  is_admin: bool
  is_active: bool
