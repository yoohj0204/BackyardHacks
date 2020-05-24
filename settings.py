import pymongo
import os

mongo = pymongo.MongoClient(os.getenv("MONGO_URI"))
