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
        return jsonify({"month": month, "value": lucros})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# the route to the revenue, by months
@app.route('/api/receitas/<month>', methods=['GET'])
def get_receitas(month):
    try:
        receitas = data.getReceitas(month)
        return jsonify({"month": month, "value": receitas})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# the route to the exams revenue, by months
@app.route('/api/receitas/exames/<month>', methods=['GET'])
def get_receitas_exames(month):
    try:
        receitas_exames = data.getReceitaExames(month)
        return jsonify({"month": month, "value": receitas_exames})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
# the route to the anesthesia revenue, by months
@app.route('/api/receitas/anestesia/<month>', methods=['GET'])
def get_receitas_anestesia(month):
    try:
        receitas_anestesia = data.getReceitaAnestesia(month)
        return jsonify({"month": month, "value": receitas_anestesia})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# the route to the cash revenue, by months
@app.route('/api/receitas/dinheiro/<month>', methods=['GET'])
def get_receitas_dinheiro(month):
    try:
        receitas_dinheiro = data.getReceitaDinheiro(month)
        return jsonify({"month": month, "value": receitas_dinheiro})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# the route to the expenses, by months
@app.route('/api/despesas/<month>', methods=['GET'])
def get_despesas(month):
    try:
        despesas = data.getDespesas(month)
        return jsonify({"month": month, "value": despesas})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# the route to the rent expenses, by months
@app.route('/api/despesas/aluguel/<month>', methods=['GET'])
def get_despesas_aluguel(month):
    try:
        despesas_aluguel = data.getDespesaAluguel(month)
        return jsonify({"month": month, "value": despesas_aluguel})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
# the route to the anesthetist expenses, by months
@app.route('/api/despesas/anestesia/<month>', methods=['GET'])
def get_despesas_anestesia(month):
    try:
        despesas_anestesia = data.getDespesaAnestesia(month)
        return jsonify({"month": month, "value": despesas_anestesia})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# the route to all data 
@app.route('/api/all', methods=['GET'])
def get_all_data():
    all_data = data.getAllData()
    return jsonify(all_data)

if __name__ == '__main__':
    app.run(debug=True, port=3000)