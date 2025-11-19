import pytz
import os
import config
import traceback
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.utils.system_utils import log_error
from app.dto.common import SoftwareVersionDto
from .routers import reports, users

app = FastAPI(
  debug=config.DEBUG, 
  title="Goose Portfolio API",
  dependencies=[],
)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(reports.router)
app.include_router(users.router)
@app.exception_handler(Exception)
def global_exception_handler(request: Request, exc: Exception):
  tb = traceback.format_exc()
  log_error([str(exc), "request %s" % request.url] + tb.split('\n'))
  return JSONResponse(
    status_code=500,
    content={ "detail": "Internal Server Error" },
  )

@app.get("/", response_model=SoftwareVersionDto)
def root():
  return {
    "apihost_ts": datetime.now(pytz.UTC),
    "api_version": "v1.25.1118"
  }

@app.get("/__env")
def list_env():
  return { k: v for k, v in os.environ.items()}
