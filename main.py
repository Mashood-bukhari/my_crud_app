from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017')
db = client['school']
collection = db['Student']

# Add data to MongoDB
@app.route('/add', methods=['POST'])
def add():

    data = request.json  # Assuming JSON data is sent in the request body
    print(data)
    collection.insert_one(data)
    return 'Data added successfully!'

# Read data from MongoDB
@app.route('/read', methods=['GET'])
def read():
    data = collection.find({}, {'_id': False})
    data_list = list(data)

    return jsonify(data_list)

# Update data in MongoDB
@app.route('/update/<name>', methods=['PUT'])
def update(name):
    new_data = request.json
    query = {'name': name}
    new_values = {"$set": new_data}
    collection.update_one(query, new_values)
    return 'Data updated successfully!'

# Delete data from MongoDB
@app.route('/delete/<name>', methods=['DELETE'])
def delete(name):
    query = {'name': name}
    collection.delete_one(query)
    return 'Data deleted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
