import pandas as pd
from pymongo import MongoClient

# Load the CSV
df = pd.read_csv("../data/machine_data.csv")

# Convert DataFrame to dictionary format
data_dict = df.to_dict(orient="records")

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["production_db"]
collection = db["machine_data"]

# Insert data
collection.insert_many(data_dict)

print("✅ Data uploaded to MongoDB successfully!")
