from pymongo import MongoClient

# define some required configurations
mongo_user = 'yourMongoUserName'
mongo_password = 'yourMongoPassword'
host_url = 'yourMongoHostUrl'
mongo_host = 'mongodb+srv://' + mongo_user + ':' + mongo_password + '@' + host_url
mongo_port = 27017

# define schema and collection name
db_name = 'yourDBName'
collection_name = 'yourCollectionName'

# define other required variables
batch_size = 100
timeout_seconds = 300
input_file_name = 'yourCSVFile.csv' # Note that this should be in the same directory as this script

# define mongo client, db and collection
client = MongoClient(mongo_host, mongo_port)
db = client[db_name]
collection = db[collection_name]