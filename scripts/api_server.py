from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS (for frontend later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["production_db"]
collection = db["machine_data"]

@app.get("/")
def read_root():
    return {"message": "API is running!"}

@app.get("/data")
def get_machine_data():
    # Fetch top 100 records
    data = list(collection.find({}, {"_id": 0}).limit(100))
    return {"machine_data": data}
