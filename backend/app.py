from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load data from CSV file
data = pd.read_csv('../app/fluxo.csv')

# Convert data to list of dictionaries
arr = data.to_dict(orient='records')

print(arr[0])
# GET request
@app.route('/api/items', methods=['GET'])
def get_data():
    return jsonify(arr)

if __name__ == '__main__':
    app.run(debug=True, port=3000)