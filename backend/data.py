"""
Data Module

This module provides classes to access and manipulate data from the dataset and
company records. It includes a class to access the dataset and retrieve economic
metrics such as profit, revenue, and expenses. Additionally, it offers a class
to access company records and retrieve gross revenue data.
"""

__docformat__ = "google"

import csv
from backend.utils import convert_to_float
from backend.economia import expenses_product_calculation
import pandas as pd

possible_months = [
    "janeiro", "fevereiro", "marco", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro", "total"
]


class Data:
    """
    Class to access the data of the dataset.
    """

    def __init__(self, path):
        """
        Initializes the Data class with the path of the dataset.

        Args:
            path (str): The path of the dataset.
        """
        self.df = pd.read_csv(path)

    def getLucro(self, month="total"):
        """
        Retrieves the profit of the dataset for a specified month or the total annual profit.

        Args:
            month (str, optional): The month for which to retrieve the profit. Defaults to "total".

        Returns:
            float: The profit value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        lucro_str = self.df.loc[self.df['RESULTADO'] == 'LUCROPREJUIZO', month].values[0]
        print(lucro_str)
        lucro = convert_to_float(lucro_str)
        return lucro

    def getReceitas(self, month="total"):
        """
        Retrieves the revenue of the dataset for a specified month or the total annual revenue.

        Args:
            month (str, optional): The month for which to retrieve the revenue. Defaults to "total".

        Returns:
            float: The revenue value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        receita_str = self.df.loc[self.df['RESULTADO'] == 'RECEITAS', month].values[0]
        receita = convert_to_float(receita_str)
        return receita

    def getReceitaExames(self, month="total"):
        """
        Retrieves the exams revenue of the dataset for a specified month or the total annual exams revenue.

        Args:
            month (str, optional): The month for which to retrieve the exams revenue. Defaults to "total".

        Returns:
            float: The exams revenue value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        receita_exames_str = self.df.loc[self.df['RESULTADO'] == 'ReceitaExames', month].values[0]
        receita_exames = convert_to_float(receita_exames_str)
        return receita_exames

    def getReceitaAnestesia(self, month="total"):
        """
        Retrieves the anesthesia revenue of the dataset for a specified month or the total annual anesthesia revenue.

        Args:
            month (str, optional): The month for which to retrieve the anesthesia revenue. Defaults to "total".

        Returns:
            float: The anesthesia revenue value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        receita_anestesia_str = self.df.loc[self.df['RESULTADO'] == 'ReceitaAnestesia', month].values[0]
        receita_anestesia = convert_to_float(receita_anestesia_str)
        return receita_anestesia

    def getReceitaConsulta(self, month="total"):
        """
        Retrieves the consult revenue of the dataset for a specified month or the total annual cash revenue.

        Args:
            month (str, optional): The month for which to retrieve the cash revenue. Defaults to "total".

        Returns:
            float: The cash revenue value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        receita_dinheiro_str = self.df.loc[self.df['RESULTADO'] == 'ReceitasConsulta', month].values[0]
        receita_dinheiro = convert_to_float(receita_dinheiro_str)
        return receita_dinheiro

    def getDespesas(self, month="total"):
        """
        Retrieves the expenses of the dataset for a specified month or the total annual expenses.

        Args:
            month (str, optional): The month for which to retrieve the expenses. Defaults to "total".

        Returns:
            float: The expenses value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        despesa_str = self.df.loc[self.df['RESULTADO'] == 'DESPESASTOTAIS', month].values[0]
        despesa = convert_to_float(despesa_str)
        return despesa

    def getDespesaAluguel(self, month="total"):
        """
        Retrieves the rent expenses of the dataset for a specified month or the total annual rent expenses.

        Args:
            month (str, optional): The month for which to retrieve the rent expenses. Defaults to "total".

        Returns:
            float: The rent expenses value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        despesa_aluguel_str = self.df.loc[self.df['RESULTADO'] == 'DESPESAALUGUEL', month].values[0]
        despesa_aluguel = convert_to_float(despesa_aluguel_str)
        return despesa_aluguel

    def getDespesaAnestesia(self, month="total"):
        """
        Retrieves the anesthesia expenses of the dataset for a specified month or the total annual anesthesia expenses.

        Args:
            month (str, optional): The month for which to retrieve the anesthesia expenses. Defaults to "total".

        Returns:
            float: The anesthesia expenses value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        despesa_anestesia_str = self.df.loc[self.df['RESULTADO'] == 'DESPESACOMANESTESIA', month].values[0]
        despesa_anestesia = convert_to_float(despesa_anestesia_str)
        return despesa_anestesia

    def getDespesaTim(self, month="total"):
        """
        Retrieves the TIM expenses of the dataset for a specified month or the total annual TIM expenses.

        Args:
            month (str, optional): The month for which to retrieve the TIM expenses. Defaults to "total".

        Returns:
            float: The TIM expenses value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        despesa_tim_str = self.df.loc[self.df['RESULTADO'] == 'DESPESATIM', month].values[0]
        despesa_tim = convert_to_float(despesa_tim_str)
        return despesa_tim

    def getDespesaEnergia(self, month="total"):
        """
        Retrieves the energy expenses of the dataset for a specified month or the total annual energy expenses.

        Args:
            month (str, optional): The month for which to retrieve the energy expenses. Defaults to "total".

        Returns:
            float: The energy expenses value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        despesa_energy_str = self.df.loc[self.df['RESULTADO'] == 'DESPESAENERGIA', month].values[0]
        despesa_energy = convert_to_float(despesa_energy_str)
        return despesa_energy

    def getDespesaInternet(self, month="total"):
        """
        Retrieves the internet expenses of the dataset for a specified month or the total annual internet expenses.

        Args:
            month (str, optional): The month for which to retrieve the internet expenses. Defaults to "total".

        Returns:
            float: The internet expenses value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        despesa_internet_str = self.df.loc[self.df['RESULTADO'] == 'DESPESAINTERNET', month].values[0]
        despesa_internet = convert_to_float(despesa_internet_str)
        return despesa_internet

    def getDespesaCrmv(self, month="total"):
        """
        Retrieves the CRMV expenses of the dataset for a specified month or the total annual CRMV expenses.

        Args:
            month (str, optional): The month for which to retrieve the CRMV expenses. Defaults to "total".

        Returns:
            float: The CRMV expenses value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        despesa_crmv_str = self.df.loc[self.df['RESULTADO'] == 'DESPESACOMCRMV', month].values[0]
        despesa_crmv = convert_to_float(despesa_crmv_str)
        return despesa_crmv

    def getDespesaRemedios(self, month="total"):
        """
        Retrieves the medicine expenses of the dataset for a specified month or the total annual medicine expenses.

        Args:
            month (str, optional): The month for which to retrieve the medicine expenses. Defaults to "total".

        Returns:
            float: The medicine expenses value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        despesa_medicine_str = self.df.loc[self.df['RESULTADO'] == 'DESPESAREMEDIOS', month].values[0]
        despesa_medicine = convert_to_float(despesa_medicine_str)
        return despesa_medicine

    def getDespesaComAlimentacao(self, month="total"):
        """
        Retrieves the food expenses of the dataset for a specified month or the total annual food expenses.

        Args:
            month (str, optional): The month for which to retrieve the food expenses. Defaults to "total".

        Returns:
            float: The food expenses value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        despesa_com_alimentacao_str = self.df.loc[self.df['RESULTADO'] == 'DESPESACOMALIMENTACAO', month].values[0]
        despesa_com_alimentacao = convert_to_float(despesa_com_alimentacao_str)
        return despesa_com_alimentacao

    def getDespesaComCombustivel(self, month="total"):
        """
        Retrieves the fuel expenses of the dataset for a specified month or the total annual fuel expenses.

        Args:
            month (str, optional): The month for which to retrieve the fuel expenses. Defaults to "total".

        Returns:
            float: The fuel expenses value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        despesa_com_combustivel_str = self.df.loc[self.df['RESULTADO'] == 'DESPESACOMCOMBUSTIVEL', month].values[0]
        despesa_com_combustivel = convert_to_float(despesa_com_combustivel_str)
        return despesa_com_combustivel

    def getDespesaComPos(self, month="total"):
        """
        Retrieves the POS expenses of the dataset for a specified month or the total annual POS expenses.

        Args:
            month (str, optional): The month for which to retrieve the POS expenses. Defaults to "total".

        Returns:
            float: The POS expenses value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        despesa_com_pos_str = self.df.loc[self.df['RESULTADO'] == 'DESPESACOMPOS', month].values[0]
        despesa_com_pos = convert_to_float(despesa_com_pos_str)
        return despesa_com_pos

    def getDespesaComPlanoDeSaude(self, month="total"):
        """
        Retrieves the health plan expenses of the dataset for a specified month or the total annual health plan expenses.

        Args:
            month (str, optional): The month for which to retrieve the health plan expenses. Defaults to "total".

        Returns:
            float: The health plan expenses value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        despesa_com_plano_de_saude_str = self.df.loc[self.df['RESULTADO'] == 'DESPESACOMPLANODESAUDE', month].values[0]
        despesa_com_plano_de_saude = convert_to_float(despesa_com_plano_de_saude_str)
        return despesa_com_plano_de_saude

    def getDespesaComLazer(self, month="total"):
        """
        Retrieves the leisure expenses of the dataset for a specified month or the total annual leisure expenses.

        Args:
            month (str, optional): The month for which to retrieve the leisure expenses. Defaults to "total".

        Returns:
            float: The leisure expenses value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        despesa_com_lazer_str = self.df.loc[self.df['RESULTADO'] == 'DESPESACOMLAZER', month].values[0]
        despesa_com_lazer = convert_to_float(despesa_com_lazer_str)
        return despesa_com_lazer

    def getImposto(self, month="total"):
        """
        Retrieves the tax expenses of the dataset for a specified month or the total annual tax expenses.

        Args:
            month (str, optional): The month for which to retrieve the tax expenses. Defaults to "total".

        Returns:
            float: The tax expenses value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        imposto_str = self.df.loc[self.df['RESULTADO'] == 'IMPOSTO', month].values[0]
        imposto = convert_to_float(imposto_str)
        return imposto

    def getContador(self, month="total"):
        """
        Retrieves the accountant expenses of the dataset for a specified month or the total annual accountant expenses.

        Args:
            month (str, optional): The month for which to retrieve the accountant expenses. Defaults to "total".

        Returns:
            float: The accountant expenses value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        contador_str = self.df.loc[self.df['RESULTADO'] == 'CONTADOR', month].values[0]
        contador = convert_to_float(contador_str)
        return contador

    def getInvestimento(self, month="total"):
        """
        Retrieves the investment expenses of the dataset for a specified month or the total annual investment expenses.

        Args:
            month (str, optional): The month for which to retrieve the investment expenses. Defaults to "total".

        Returns:
            float: The investment expenses value.

        Raises:
            ValueError: If the provided month is not valid.
        """
        error_month(month)

        investimento_str = self.df.loc[self.df['RESULTADO'] == 'INVESTIMENTO', month].values[0]
        investimento = convert_to_float(investimento_str)
        return investimento

    def getFixedExpenses(self, month="total"):
        """
        Calculates the fixed expenses of the company for a specified month or the total annual fixed expenses.

        This may vary between companies.

        Args:
            month (str, optional): The month for which to calculate the fixed expenses. Defaults to "total".

        Returns:
            float: The total fixed expenses.
        """
        fixed_expenses = (
            self.getDespesaAluguel(month) +
            self.getDespesaComPlanoDeSaude(month) +
            self.getDespesaComPos(month) +
            self.getDespesaCrmv(month) +
            self.getDespesaEnergia(month) +
            self.getDespesaInternet(month) +
            self.getDespesaTim(month)
        )
        return fixed_expenses

    def getVariablesExpenses(self, month="total"):
        """
        Calculates the variable expenses of the company for a specified month or the total annual variable expenses.

        This may vary between companies.

        Args:
            month (str, optional): The month for which to calculate the variable expenses. Defaults to "total".

        Returns:
            float: The total variable expenses.
        """
        variables_expenses = (
            self.getDespesaComAlimentacao(month) +
            self.getDespesaRemedios(month) +
            self.getDespesaComLazer(month) +
            self.getDespesaComCombustivel(month)
        )
        return variables_expenses


    def getMarkupAnestesia(self, month="total"):
        """
        Calculates the markup for anesthesia expenses based on fixed and variable expenses.

        Utilizes `economia.expenses_product_calculation` to adjust expenses.

        Args:
            month (str, optional): The month for which to calculate the markup. Defaults to "total".

        Returns:
            tuple:
                float: Adjusted fixed expenses.
                float: Adjusted variable expenses.
                float: Product revenue.

        Raises:
            ValueError: If the provided month is not valid.
        """
        fixed_expenses = self.getFixedExpenses(month)
        variable_expenses = self.getVariablesExpenses(month)
        total_revenue = self.getReceitas(month)
        product_revenue = self.getReceitaAnestesia(month)
        product_expenses = self.getDespesaAnestesia(month)
        product_fixed_expenses, product_variable_expenses = expenses_product_calculation(
            expenses_product=product_expenses,
            fixed_expenses=fixed_expenses,
            variable_expenses=variable_expenses,
            total_revenue=total_revenue,
            product_revenue=product_revenue
        )

        return product_fixed_expenses, product_variable_expenses, product_revenue


    def getMarkupConsulta(self, month="total"):
        """
        Calculates the markup for consult expenses based on fixed and variable expenses.

        Utilizes `economia.expenses_product_calculation` to adjust expenses.

        Args:
            month (str, optional): The month for which to calculate the markup. Defaults to "total".
        
        Returns:
            tuple:
                float: Adjusted fixed expenses.
                float: Adjusted variable expenses.
                float: Product revenue.
        
        Raises:
            ValueError: If the provided month is not valid.
        """
        fixed_expenses = self.getFixedExpenses(month)
        variable_expenses = self.getVariablesExpenses(month)
        total_revenue = self.getReceitas(month)
        product_revenue = self.getReceitaConsulta(month)
        product_expenses = 0 # No specific expenses for consult
        product_fixed_expenses, product_variable_expenses = expenses_product_calculation(
            expenses_product=product_expenses,
            fixed_expenses=fixed_expenses,
            variable_expenses=variable_expenses,
            total_revenue=total_revenue,
            product_revenue=product_revenue
        )

        return product_fixed_expenses, product_variable_expenses, product_revenue

    def getMarkupExames(self, month="total"):
        """
        Calculates the markup for exams expenses based on fixed and variable expenses.

        Utilizes `economia.expenses_product_calculation` to adjust expenses.

        Args:
            month (str, optional): The month for which to calculate the markup. Defaults to "total".
        
        Returns:
            tuple:
                float: Adjusted fixed expenses.
                float: Adjusted variable expenses.
                float: Product revenue.
        
        Raises:
            ValueError: If the provided month is not valid.
        """
        fixed_expenses = self.getFixedExpenses(month)
        variable_expenses = self.getVariablesExpenses(month)
        total_revenue = self.getReceitas(month)
        product_revenue = self.getReceitaExames(month)
        product_expenses = 0 # No specific expenses for exams
        product_fixed_expenses, product_variable_expenses = expenses_product_calculation(
            expenses_product=product_expenses,
            fixed_expenses=fixed_expenses,
            variable_expenses=variable_expenses,
            total_revenue=total_revenue,
            product_revenue=product_revenue
        )

        return product_fixed_expenses, product_variable_expenses, product_revenue

    def getAllData(self):
        """
        Retrieves all data from the dataset.

        Returns:
            list of dict: A list of records representing the dataset.
        """
        data = self.df.to_dict(orient='records')
        return data


class CompanyData:
    """
    Class to access the data of a specific company. This data only has 2 columns: 'nome_da_empresa' and 'receita_bruta'.
    """

    def __init__(self, csv_file_path):
        """
        Initializes the CompanyData class with the path of the CSV file.

        Args:
            csv_file_path (str): The path of the CSV file.
        """
        self.csv_file_path = csv_file_path
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the data from the CSV file.

        Returns:
            list of dict: A list of company records with 'nome_da_empresa' and 'receita_bruta'.
        """
        data = []
        with open(self.csv_file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['receita_bruta'] = float(row['receita_bruta'])
                data.append(row)
        return data

    def get_company_data(self, company_name):
        """
        Retrieves the data of a specific company.

        Args:
            company_name (str): The name of the company.

        Returns:
            dict: The company's data containing 'nome_da_empresa' and 'receita_bruta'.

        Raises:
            ValueError: If the company is not found.
        """
        for record in self.data:
            if record['nome_da_empresa'] == company_name:
                return record
        raise ValueError(f"Company '{company_name}' not found.")

    def get_all_companies(self):
        """
        Retrieves the data of all companies.

        Returns:
            list of dict: A list of all company records.
        """
        return self.data


def error_month(month):
    """
    Verifies if the selected month is valid.

    Args:
        month (str): The month to verify.

    Raises:
        ValueError: If the month is not in the list of possible months.
    """
    if month not in possible_months:
        raise ValueError(f"Month '{month}' is not valid. Choose from {possible_months}.")
