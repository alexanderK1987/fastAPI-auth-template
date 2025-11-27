from app.schemae.common import MongoBaseModel, PyObjectId

class PortfolioModel(MongoBaseModel):
  user_id: PyObjectId = None
  portfolio_name: str
