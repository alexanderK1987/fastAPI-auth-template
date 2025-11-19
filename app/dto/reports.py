from pydantic import BaseModel

class PortionChartTickerDto(BaseModel):
  ticker: str
  value: float
