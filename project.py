import json
from pymongo import MongoClient 
from jsoncomment import JsonComment 
  
# Making Connection
myclient = MongoClient("mongodb://127.0.0.1:27017/") 
   
# database 
db = myclient["company"]
   

Collection = db["project_data"]
  
# Loading or Opening the json file
with open('C:/Users/surbh/Downloads/DB2/db2_project2/project_doc.json') as file:
    parser = JsonComment(json)
    file_data = parser.load(file)
      
if isinstance(file_data, list):
    Collection.insert_many(file_data)  
else:
    Collection.insert_one(file_data)