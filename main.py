import json
import pymongo

def upload_to_db(file, collection_name):
    client = pymongo.MongoClient('your_mongo_db_connection_string')
    db = client['your_database_name']
    collection = db[collection_name]

    with open(file, 'r') as f:
        data = json.load(f)
    
    collection.insert_many(data)
    print(f'Data from {file} uploaded to {collection_name} collection.')

upload_to_db('quotes_processed.json', 'quotes')
upload_to_db('authors.json', 'authors')
