from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional
from pydantic import BaseModel
from app.constants import TxActions
from app.schemae.common import PyObjectId

class PortfolioModel(BaseModel):
  id: Optional[PyObjectId] = Field(default=None, alias="_id")
  user_id: PyObjectId = Field(default=None)
  portfolio_name: str
  class Config:
    validate_by_name = True
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}

class PortfolioTxModel(BaseModel):
  id: Optional[PyObjectId] = Field(default=None, alias="_id")
  portfolio_id: PyObjectId = Field(default=None)
  ticker: str
  action: TxActions
  cost: float
  quantity: float
  price: float
  remark: str
  class Config:
    validate_by_name = True
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}
