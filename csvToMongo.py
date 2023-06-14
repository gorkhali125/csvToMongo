import csv
from pymongo import MongoClient
from datetime import datetime

# define mongo configurations
mongo_user = 'yourMongoUserName'
mongo_password = 'yourMongoPassword'
host_url = 'yourMongoHostUrl'
mongo_port = 27017
mongo_host = 'mongodb+srv://' + mongo_user + ':' + mongo_password + '@' + host_url

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

# begin the actual import process
with open(input_file_name) as file:
    reader = csv.DictReader(file)
    batch = []
    last_insert_time = datetime.now()
    for i, row in enumerate(reader):
        try:
            batch.append(row)
            if len(batch) == batch_size or (datetime.now() - last_insert_time).total_seconds() >= timeout_seconds:
                result = collection.insert_many(batch)
                if result.acknowledged:
                    batch = []
                    last_insert_time = datetime.now()
                    print(f'Processed {i+1} records')
        except Exception as e:
            print(f'Error on row {i+1}: {e}')
    if batch:
        try:
            result = collection.insert_many(batch)
            if result.acknowledged:
                print(f'Processed {i+1} records')
        except Exception as e:
            print(f'Error on row {i+1}: {e}')