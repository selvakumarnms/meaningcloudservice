import csv
from pymongo import MongoClient

# Establish a connection to MongoDB
client = MongoClient('mongodb+srv://cluster0.hwcvkfj.mongodb.net', 
                     username='selvakumarnms',
                     password='*****'
                     )

# Select the database and collection
db = client['playstore_scraped_data']
collection = db['reviews']
# Read and insert CSV data into MongoDB
with open("C:\\Users\\selva\\PhonePe_Rerun3.csv", 'r', encoding="utf8") as file:
    csv_data = csv.DictReader(file)
    print(csv_data)
    for row in csv_data:
        collection.insert_one(row)

# Close the connection
client.close()
