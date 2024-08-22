import pymongo

#Provide the mangodb localhost url to connect python to mangodb
client = pymongo.MangoClient("mongodb://localhost:27017/neurolab")

#Database name
dataBase = client['neurolabdb']

#Collection Name
collection = dataBase['Products']

#Sample data
d= {'companyName':'ineuron',
    'product':'Affordable AI',
    'courseOffered':'Mechine learnign with deployment'}

#Insert above records into collection
rec =collection.insert_one(d)

all_record = collection.find()

#Printingall reccords
for idx, record in enumerate(all_record):
    print(f'{idx}:{record}')