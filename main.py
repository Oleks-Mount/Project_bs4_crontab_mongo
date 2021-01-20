from pymongo import MongoClient

client = MongoClient('localhost', 27017)

my_db = client['News']

mycollection = my_db['Soccer']

for t in mycollection:
    print(t)
