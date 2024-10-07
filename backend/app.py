"""
Flask API for accessing financial data and company information.

This application provides endpoints to retrieve profits, revenues, expenses, and economia results
for different companies on a monthly basis.
"""

from flask import Flask, jsonify
from flask_cors import CORS
from backend.data import Data, CompanyData
from backend.economia import economia

app = Flask(__name__)
CORS(app)

PATH = './app/fluxo.csv'
COMPANY_DATA_PATH = './app/empresas.csv'

data = Data(PATH)
company_data = CompanyData(COMPANY_DATA_PATH)


@app.route('/api/lucros/<month>', methods=['GET'])
def get_lucros(month):
    """
    Retrieves the profit for a specified month.

    Args:
        month (str): The month for which to retrieve the profit. Should be one of the possible_months.

    Returns:
        flask.Response: A JSON response containing the month and its corresponding profit.
                        If an error occurs, returns a JSON response with the error message and a 400 status code.
    """
    try:
        lucros = data.getLucro(month)
        return jsonify({"month": month, "value": lucros})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/receitas/<month>', methods=['GET'])
def get_receitas(month):
    """
    Retrieves the revenue for a specified month.

    Args:
        month (str): The month for which to retrieve the revenue. Should be one of the possible_months.

    Returns:
        flask.Response: A JSON response containing the month and its corresponding revenue.
                        If an error occurs, returns a JSON response with the error message and a 400 status code.
    """
    try:
        receitas = data.getReceitas(month)
        return jsonify({"month": month, "value": receitas})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/receitas/exames/<month>', methods=['GET'])
def get_receitas_exames(month):
    """
    Retrieves the exams revenue for a specified month.

    Args:
        month (str): The month for which to retrieve the exams revenue. Should be one of the possible_months.

    Returns:
        flask.Response: A JSON response containing the month and its corresponding exams revenue.
                        If an error occurs, returns a JSON response with the error message and a 400 status code.
    """
    try:
        receitas_exames = data.getReceitaExames(month)
        return jsonify({"month": month, "value": receitas_exames})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/markup/anestesia/<month>', methods=['GET'])
def get_markup_anestesia(month):
    """
    Retrieves the markup information for anesthesia for a specified month.

    Args:
        month (str): The month for which to retrieve the markup information. Should be one of the possible_months.

    Returns:
        flask.Response: A JSON response containing the month and its corresponding markup information.
                        If an error occurs, returns a JSON response with the error message and a 400 status code.
    """
    try:
        markup_anestesia = data.getMarkupAnestesia(month)
        return jsonify({"month": month, "value": markup_anestesia})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/receitas/anestesia/<month>', methods=['GET'])
def get_receitas_anestesia(month):
    """
    Retrieves the anesthesia revenue for a specified month.

    Args:
        month (str): The month for which to retrieve the anesthesia revenue. Should be one of the possible_months.

    Returns:
        flask.Response: A JSON response containing the month and its corresponding anesthesia revenue.
                        If an error occurs, returns a JSON response with the error message and a 400 status code.
    """
    try:
        receitas_anestesia = data.getReceitaAnestesia(month)
        return jsonify({"month": month, "value": receitas_anestesia})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/receitas/consulta/<month>', methods=['GET'])
def get_receitas_consulta(month):
    """
    Retrieves the cash revenue for a specified month.

    Args:
        month (str): The month for which to retrieve the cash revenue. Should be one of the possible_months.

    Returns:
        flask.Response: A JSON response containing the month and its corresponding cash revenue.
                        If an error occurs, returns a JSON response with the error message and a 400 status code.
    """
    try:
        receitas_dinheiro = data.getReceitaConsulta(month)
        return jsonify({"month": month, "value": receitas_dinheiro})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/despesas/<month>', methods=['GET'])
def get_despesas(month):
    """
    Retrieves the expenses for a specified month.

    Args:
        month (str): The month for which to retrieve the expenses. Should be one of the possible_months.

    Returns:
        flask.Response: A JSON response containing the month and its corresponding expenses.
                        If an error occurs, returns a JSON response with the error message and a 400 status code.
    """
    try:
        despesas = data.getDespesas(month)
        return jsonify({"month": month, "value": despesas})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/despesas/aluguel/<month>', methods=['GET'])
def get_despesas_aluguel(month):
    """
    Retrieves the rent expenses for a specified month.

    Args:
        month (str): The month for which to retrieve the rent expenses. Should be one of the possible_months.

    Returns:
        flask.Response: A JSON response containing the month and its corresponding rent expenses.
                        If an error occurs, returns a JSON response with the error message and a 400 status code.
    """
    try:
        despesas_aluguel = data.getDespesaAluguel(month)
        return jsonify({"month": month, "value": despesas_aluguel})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/despesas/anestesia/<month>', methods=['GET'])
def get_despesas_anestesia(month):
    """
    Retrieves the anesthesia expenses for a specified month.

    Args:
        month (str): The month for which to retrieve the anesthesia expenses. Should be one of the possible_months.

    Returns:
        flask.Response: A JSON response containing the month and its corresponding anesthesia expenses.
                        If an error occurs, returns a JSON response with the error message and a 400 status code.
    """
    try:
        despesas_anestesia = data.getDespesaAnestesia(month)
        return jsonify({"month": month, "value": despesas_anestesia})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/all', methods=['GET'])
def get_all_data():
    """
    Retrieves all data from the dataset.

    Returns:
        flask.Response: A JSON response containing all records from the dataset.
    """
    all_data = data.getAllData()
    return jsonify(all_data)


@app.route('/api/company/<company_name>', methods=['GET'])
def get_company_data(company_name):
    """
    Retrieves data for a specific company.

    Args:
        company_name (str): The name of the company to retrieve data for.

    Returns:
        flask.Response: A JSON response containing the company's data.
                        If the company is not found, returns a JSON response with the error message and a 400 status code.
    """
    try:
        company = company_data.get_company_data(company_name)
        return jsonify(company)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/economia/<company_name>', methods=['GET'])
def get_economia_data(company_name):
    """
    Retrieves the economia results for a specific company.

    Args:
        company_name (str): The name of the company to retrieve economia data for.

    Returns:
        flask.Response: A JSON response containing the company's name, receita_bruta, and economia results.
                        If the company is not found, returns a JSON response with the error message and a 400 status code.
    """
    try:
        company = company_data.get_company_data(company_name)
        receita_bruta = company['receita_bruta']
        economia_result = economia(receita_bruta)
        return jsonify({
            "company_name": company_name,
            "receita_bruta": receita_bruta,
            "economia": economia_result
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/companies', methods=['GET'])
def get_all_companies():
    """
    Retrieves data for all companies.

    Returns:
        flask.Response: A JSON response containing data for all companies.
    """
    companies = company_data.get_all_companies()
    return jsonify(companies)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
