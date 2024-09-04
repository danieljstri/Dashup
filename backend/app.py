from flask import Flask, jsonify
from flask_cors import CORS
from data import Data

app = Flask(__name__)
CORS(app)

PATH = '../app/fluxo.csv'

data = Data(PATH)

# the route to the profit, by months
@app.route('/api/lucros/<month>', methods=['GET'])
def get_lucros(month):
    try:
        lucros = data.getLucro(month)
        return jsonify({"month": month, "lucros": lucros})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# the route to the revenue, by months
@app.route('/api/receitas/<month>', methods=['GET'])
def get_receitas(month):
    try:
        receitas = data.getReceitas(month)
        return jsonify({"month": month, "receitas": receitas})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# the route to the expenses, by months
@app.route('/api/despesas/<month>', methods=['GET'])
def get_despesas(month):
    try:
        despesas = data.getDespesas(month)
        return jsonify({"month": month, "despesas": despesas})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# the route to all data 
@app.route('/api/all', methods=['GET'])
def get_all_data():
    all_data = data.getAllData()
    return jsonify(all_data)

if __name__ == '__main__':
    app.run(debug=True, port=3000)