from utils import convert_to_float
import pandas as pd

possible_months = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro", "total"]

class Data:
    def __init__(self, path):
        self.df = pd.read_csv(path)
        self.df.columns = self.df.columns.str.lower()  # Convert columns to lowercase for consistency

    def getReceitas(self, month="total"):
        """
        Get the revenue of the dataset (parameters: month)
        
        :month: get the revenue of the month selected. the standard is "total" (the revenue of all the year)
        """
        if month not in possible_months:
            raise ValueError(f"Month '{month}' is not valid. Choose from {possible_months}.")
        
        receita_str = self.df.at[0, month]
        receita = convert_to_float(receita_str)
        return receita

    def getDespesas(self, month="total"):
        """
        Get the expenses of the dataset (parameters: month)
        
        :month: get the expenses of the month selected. the standard is "total" (the expenses of all the year)
        """
        if month not in possible_months:
            raise ValueError(f"Month '{month}' is not valid. Choose from {possible_months}.")
        
        despesa_str = self.df.at[5, month]  # row 5 is DESPESAS TOTAIS
        despesa = convert_to_float(despesa_str)
        return despesa

    def getLucro(self, month="total"):
        """
        Get the profit of the dataset (parameters: month)
        :month: get the expenses of the month selected. the standard is "total" (the profit of all the year)
        """
        if month not in possible_months:
            raise ValueError(f"Month '{month}' is not valid. Choose from {possible_months}.")
        
        lucro_str = self.df.at[12, month] # the |profit| is in the last row
        lucro = convert_to_float(lucro_str)
        return lucro
    
    def getAllData(self):
        """
        Get all data from the dataset
        """
        data = self.df.to_dict(orient='records')
        return data
