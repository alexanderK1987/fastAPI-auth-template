from datetime import datetime
from fastapi import APIRouter
import pytz
from typing import List
from app.dto.reports import PortionChartTickerDto
from app.services.reports import ReportService
router = APIRouter(
  prefix="/reports",
  tags=["Report"],
  dependencies=[],
  responses={404: {"description": "Not found"}},
)

report_svc = ReportService()

@router.get("/portion_chart", response_model=List[PortionChartTickerDto])
def get_portion_chart(portfolio_set_id):
  return report_svc.get_portion_chart_data()
