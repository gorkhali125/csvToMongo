from pymongo import MongoClient

# define some required configurations
mongo_user = 'yourMongoUserName'
mongo_password = 'yourMongoPassword'
host_url = 'yourMongoHostUrl'
mongo_host = 'mongodb+srv://' + mongo_user + ':' + mongo_password + '@' + host_url
mongo_port = 27017

client = MongoClient(mongo_host, mongo_port)