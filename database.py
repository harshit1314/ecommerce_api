from pymongo import MongoClient
import os

# Your MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://user1234:myapplication123@cluster0.mnjmniw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "ecommerce_db"

# Establish a connection to the MongoDB server
client = MongoClient(MONGO_URI)

# Select your database
db = client[DB_NAME]

# Get a handle for your collections
product_collection = db["products"]
order_collection = db["orders"]

print(" Database connection established.")