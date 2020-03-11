from pymongo import MongoClient
from bson.json_util import dumps, loads

# Credentials
CLIENT = "url"
DB_NAME = "dbname"
COLLECTION = "collection"

# Add client URL
client = MongoClient(CLIENT)
# Get client code
db = client[DB_NAME]

# Get target collection
collection = db[COLLECTION]

# Load and dump
json_final = loads(dumps(collection.find({})))

# Print
print(json_final)
