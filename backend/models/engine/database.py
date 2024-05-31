from pymongo import MongoClient

class Database:
    def __init__(self, db_name, uri='mongodb://localhost:27017/'):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def insert_one(self, collection_name, data):
        collection = self.db[collection_name]
        result = collection.insert_one(data)
        return result.inserted_id

    def find_one(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find_one(query)

    def find(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find(query)

    def update_one(self, collection_name, query, update_data):
        collection = self.db[collection_name]
        return collection.update_one(query, {'$set': update_data})

    def delete_one(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.delete_one(query)







