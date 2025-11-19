from enum import Enum
import pytz

LocalTimezone = pytz.timezone("Asia/Taipei")

class PortfolioSetType(str, Enum):
  FIRSTRADE = 'firstrade'

class TickerDataInterval(str, Enum):
  DAILY = 'd'
  
class TxActions(str, Enum):
  BUY = 'buy'
  SELL = 'sell'
  DEPOSIT = 'deposit'
  WITHDRAW = 'withdraw'
  INTEREST = 'interest'
