from datetime import datetime
import pytz

def ensure_utc(dt: datetime) -> datetime:
  if not dt:
    return dt
  if dt.tzinfo is None or dt.utcoffset() is None:
    # Assume this naive datetime is UTC
    return dt.replace(tzinfo=pytz.UTC)
  return dt
