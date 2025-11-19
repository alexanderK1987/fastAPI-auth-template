from datetime import datetime
import pytz
import sys

def log_error(texts, output_file=sys.stderr):
  now_str = datetime.now(pytz.UTC).isoformat()
  if type(texts) is str:
    texts = texts.split('\n')
  for i, text in enumerate(texts):
    print(
      now_str if i == 0 else (" " * len(now_str)), 
      text,
      file=output_file,
    )
