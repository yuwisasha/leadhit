import os

from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(os.getenv("MONGO_DB_URL"))
db = client.get_database(os.getenv("MONGO_INITDB_DATABASE"))
forms_collection = db.get_collection(os.getenv("MONGO_DB_COLLECTION"))
