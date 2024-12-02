from pymongo import MongoClient

MONGO_URI = "mongodb+srv://yashkshrivas1234:Exp1bMcnjjhZ61lT@cluster0.k7fadbx.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client['studentdb']

def get_students_collection():
    return db['students']
