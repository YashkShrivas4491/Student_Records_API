from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get MongoDB URI from the environment
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MONGO_URI is not set in the environment variables.")

# Initialize MongoDB client
client = MongoClient(MONGO_URI)
db = client['studentdb']

def get_students_collection():
    return db['students']
