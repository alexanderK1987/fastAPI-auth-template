import pytz
from bson import ObjectId
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.constants import TickerDataInterval
from app.schemae.common import PyObjectId

class TickerPriceModel(BaseModel):
  id: Optional[PyObjectId] = Field(default=None, alias="_id")
  ticker: str
  data_interval: TickerDataInterval = Field(default=TickerDataInterval.DAILY.value)
  p_high: float = 0
  p_low: float = 0
  p_open: float = 0
  p_close: float = 0
  timestamp: datetime = Field(default_factory=lambda: datetime.now(pytz.UTC))

  class Config:
    validate_by_name = True
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}
