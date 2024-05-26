from pymongo import MongoClient
client = MongoClient('mongodb+srv://venugiperera11:1g9QTCYS1e2B1Tal@cluster0.6bodfn8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.test
collection_name = db['monthsummaries']
risk_collection = db['risksummaries']