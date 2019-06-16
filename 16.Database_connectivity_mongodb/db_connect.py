import pymongo                     # Driver for connection
from pymongo import MongoClient    # method for creating mongo client instance
client=MongoClient(host='localhost',port=27017)


print(client.list_database_names())  # check for available databases

db=client.classinfo                  #getting database

print(db.collection_names())        # check for collections in database

col=db.studentinfo                  # getting collections
res=col.find()                      # getting all documents

print('--'*70)
for x in res:
    print(x)
print('--'*70)


