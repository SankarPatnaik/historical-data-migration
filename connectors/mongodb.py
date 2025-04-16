import pandas as pd
from pymongo import MongoClient

def read(config):
    uri = f"mongodb://{config['user']}:{config['password']}@{config['host']}:{config.get('port', 27017)}"
    client = MongoClient(uri)
    collection = client[config['database']][config['collection']]
    data = list(collection.find())
    return pd.DataFrame(data)
