from pymongo import MongoClient
import config
__client__ = MongoClient(config.MONGODB_CONNECTION_STRING)
__db__ = __client__[config.MONGO_GOOSE_MAIN_DB]

def get_mongo_db():
  return __db__
