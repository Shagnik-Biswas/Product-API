import pymongo
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', '.env')  # CONFIGURING ENV PATH
load_dotenv()  # LOADING ENVIRONMENT

# MONGODB CREDENTIALS
mongo_username = os.getenv('mongo_username')
mongo_password = os.getenv('password')
mongo_cluster = os.getenv('cluster')
mongo_key = os.getenv('key')

# CONNECTING WITH MONGODB
conn_str = f'mongodb+srv://{mongo_username}:{mongo_password}' \
           f'@{mongo_cluster}.{mongo_key}.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(conn_str, server_Api=ServerApi('1'), serverSelectionTimeoutMS=5000)

# MONGODB DATABASE
db = client['ProductAPI']
Product_collection = db['Product']
