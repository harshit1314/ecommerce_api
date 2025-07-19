from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Paste your connection string here
# Remember to replace <password> with your actual database user password
connection_string = "mongodb+srv://user1234:myapplication123@cluster0.mnjmniw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = None  # Initialize client to None

try:
    # Set a timeout to prevent it from hanging indefinitely
    client = MongoClient(connection_string, serverSelectionTimeoutMS=5000)
    
    # The ismaster command is cheap and does not require auth.
    client.admin.command('ismaster')
    print("Connection to MongoDB Atlas successful!")

except ConnectionFailure as e:
    print(f"Connection failed. Could not connect to MongoDB: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    # Ensure that the client is closed even if connection fails
    if client:
        client.close()