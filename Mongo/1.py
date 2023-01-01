from pymongo import MongoClient
connection = "mongodb+srv://irp:irp2022@irpmongodb.26cuy7l.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection)

database = 'deepface'; collection = 'deepface'

db = client[database]