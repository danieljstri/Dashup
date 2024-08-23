from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load data from JSON file
with open('../app/data.json') as f:
    data = json.load(f)

arr = []

# Append data to array
for item in data["transport"]:
    arr.append(item)

# GET request
@app.route('/api/items', methods=['GET'])
def get_data():
    return jsonify(arr)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
