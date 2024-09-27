import csv
from utils import convert_to_float
from economia import expenses_product_calculation
import pandas as pd

possible_months = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro", "total"]

class Data:
    def __init__(self, path):
        self.df = pd.read_csv(path)
        
    def getLucro(self, month="total"):
        """
        Get the profit of the dataset (parameters: month)
        :month: get the expenses of the month selected. the standard is "total" (the profit of all the year)
        """
        error_month(month)
        
        lucro_str = self.df.loc[self.df['RESULTADO'] == 'LUCROPREJUIZO', month].values[0] # acess the row LUCROPREJUIZO and the column month selected
        print(lucro_str)
        lucro = convert_to_float(lucro_str)
        return lucro
    
    def getReceitas(self, month="total"):
        """
        Get the revenue of the dataset (parameters: month)
        
        :month: get the revenue of the month selected. the standard is "total" (the revenue of all the year)
        """
        error_month(month)
        
        receita_str = self.df.loc[self.df['RESULTADO'] == 'RECEITAS', month].values[0]
        receita = convert_to_float(receita_str)
        return receita

    def getReceitaExames(self, month="total"):
        """
        Get the exams revenue of the dataset (parameters: month)

        :month: get the revenue of the month selected. the standard is "total" (the exams revenue of all the year)
        """
        error_month(month)
        
        receita_exames_str = self.df.loc[self.df['RESULTADO'] == 'ReceitaExames', month].values[0]
        receita_exames = convert_to_float(receita_exames_str)
        return receita_exames
    
    def getReceitaAnestesia(self, month="total"):
        """
        Get the anesthesia revenue of the dataset (parameters: month)

        :month: get the revenue of the month selected. the standard is "total" (the anesthesia revenue of all the year)
        """
        error_month(month)
        
        receita_anestesia_str = self.df.loc[self.df['RESULTADO'] == 'ReceitaAnestesia', month].values[0]
        receita_anestesia = convert_to_float(receita_anestesia_str)
        return receita_anestesia

    def getReceitaDinheiro(self, month="total"):
        """ 
        Get the cash revenue of the dataset (parameters: month)

        :month: get the revenue of the month selected. the standard is "total" (the cash revenue of all the year)
        """
        error_month(month)
        
        receita_dinheiro_str = self.df.loc[self.df['RESULTADO'] == 'ReceitasDinheiro', month].values[0]
        receita_dinheiro = convert_to_float(receita_dinheiro_str)
        return receita_dinheiro
    

    def getDespesas(self, month="total"):
        """
        Get the expenses of the dataset (parameters: month)
        
        :month: get the expenses of the month selected. the standard is "total" (the expenses of all the year)
        """
        error_month(month)
        
        despesa_str = self.df.loc[self.df['RESULTADO'] == 'DESPESASTOTAIS', month].values[0]
        despesa = convert_to_float(despesa_str)
        return despesa

    
    def getDespesaAluguel(self, month="total"):
        """
        Get the rent expenses of the dataset (parameters: month)
        :month: get the expenses of the month selected. the standard is "total" (the rent expenses of all the year)
        """
        error_month(month)
        
        despesa_aluguel_str = self.df.loc[self.df['RESULTADO'] == 'DESPESAALUGUEL', month].values[0]
        despesa_aluguel = convert_to_float(despesa_aluguel_str)
        return despesa_aluguel

    def getDespesaAnestesia(self, month="total"):
        """
        Get the anesthesia expenses of the dataset (parameters: month)
        :month: get the expenses of the month selected. the standard is "total" (the anesthesia expenses of all the year)
        """
        error_month(month)
        
        despesa_anestesia_str = self.df.loc[self.df['RESULTADO'] == 'DESPESACOMANESTESIA', month].values[0]
        despesa_anestesia = convert_to_float(despesa_anestesia_str)
        return despesa_anestesia

    def getDespesaTim(self, month="total"):
        """
        Get the TIM expenses of the dataset (parameters: month)
        """
        error_month(month)

        despesa_tim_str = self.df.loc[self.df['RESULTADO'] == 'DESPESATIM', month].values[0]
        despesa_tim = convert_to_float(despesa_tim_str)
        return despesa_tim
    
    def getDespesaEnergia(self, month="total"):
        """
        Get the energy expenses of the dataset (parameters: month)
        """
        error_month(month)

        despesa_energy_str = self.df.loc[self.df['RESULTADO'] == 'DESPESAENERGIA', month].values[0]
        despesa_energy = convert_to_float(despesa_energy_str)
        return despesa_energy
    
    def getDespesaInternet(self, month="total"):
        """
        Get the internet expenses of the dataset (parameters: month)
        """
        error_month(month)

        despesa_internet_str = self.df.loc[self.df['RESULTADO'] == 'DESPESAINTERNET', month].values[0]
        despesa_internet = convert_to_float(despesa_internet_str)
        return despesa_internet
    
    def getDespesaCrmv(self, month="total"):
        """
        Get the CRMV expenses of the dataset (parameters: month)
        """
        error_month(month)

        despesa_crmv_str = self.df.loc[self.df['RESULTADO'] == 'DESPESACRMV', month].values[0]
        despesa_crmv = convert_to_float(despesa_crmv_str)  
        return despesa_crmv

    def getDespesaRemedios(self, month="total"):
        """
        Get the medicine expenses of the dataset (parameters: month)
        """
        error_month(month)

        despesa_medicine_str = self.df.loc[self.df['RESULTADO'] == 'DESPESAREMEDIOS', month].values[0]
        despesa_medicine = convert_to_float(despesa_medicine_str)
        return despesa_medicine

    def getDespesaComAlimentacao(self, month="total"):
        """
        Get the food expenses of the dataset (parameters: month)
        """
        error_month(month)

        despesa_com_alimentacao_str = self.df.loc[self.df['RESULTADO'] == 'DESPESACOMALIMENTACAO', month].values[0]
        despesa_com_alimentacao = convert_to_float(despesa_com_alimentacao_str)
        return despesa_com_alimentacao

    def getDespesaComCombustivel(self, month="total"):
        """
        Get the fuel expenses of the dataset (parameters: month)
        """
        error_month(month)

        despesa_com_combustivel_str = self.df.loc[self.df['RESULTADO'] == 'DESPESACOMCOMBUSTIVEL', month].values[0]
        despesa_com_combustivel = convert_to_float(despesa_com_combustivel_str)
        return despesa_com_combustivel

    def getDespesaComPos(self, month="total"):
        """
        Get the POS expenses of the dataset (parameters: month)
        """
        error_month(month)

        despesa_com_pos_str = self.df.loc[self.df['RESULTADO'] == 'DESPESACOMPOS', month].values[0]
        despesa_com_pos = convert_to_float(despesa_com_pos_str)
        return despesa_com_pos

    def getDespesaComPlanoDeSaude(self, month="total"):
        """
        Get the health plan expenses of the dataset (parameters: month)
        """
        error_month(month)

        despesa_com_plano_de_saude_str = self.df.loc[self.df['RESULTADO'] == 'DESPESACOMPLANODESAUDE', month].values[0]
        despesa_com_plano_de_saude = convert_to_float(despesa_com_plano_de_saude_str)
        return despesa_com_plano_de_saude

    def getDespesaComLazer(self, month="total"):
        """
        Get the leisure expenses of the dataset (parameters: month)
        """
        error_month(month)

        despesa_com_lazer_str = self.df.loc[self.df['RESULTADO'] == 'DESPESACOMLAZER', month].values[0]
        despesa_com_lazer = convert_to_float(despesa_com_lazer_str)
        return despesa_com_lazer

    def getImposto(self, month="total"):
        """
        Get the tax expenses of the dataset (parameters: month)
        """
        error_month(month)

        imposto_str = self.df.loc[self.df['RESULTADO'] == 'IMPOSTO', month].values[0]
        imposto = convert_to_float(imposto_str)
        return imposto

    def getContador(self, month="total"):
        """
        Get the accountant expenses of the dataset (parameters: month)
        """
        error_month(month)

        contador_str = self.df.loc[self.df['RESULTADO'] == 'CONTADOR', month].values[0]
        contador = convert_to_float(contador_str)
        return contador

    def getInvestimento(self, month="total"):
        """
        Get the investment expenses of the dataset (parameters: month)
        """
        error_month(month)

        investimento_str = self.df.loc[self.df['RESULTADO'] == 'INVESTIMENTO', month].values[0]
        investimento = convert_to_float(investimento_str)
        return investimento




    def getAllData(self):
        """
        Get all data from the dataset
        """
        data = self.df.to_dict(orient='records')
        return data


class CompanyData:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.data = self.load_data()
    
    def load_data(self):
        data = []
        with open(self.csv_file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['receita_bruta'] = float(row['receita_bruta'])
                data.append(row)
        return data
    
    def get_company_data(self, company_name):
        for record in self.data:
            if record['nome_da_empresa'] == company_name:
                return record
        raise ValueError(f"Company '{company_name}' not found.")
    
    def get_all_companies(self):
        return self.data


def error_month(month):
    if month not in possible_months:
        raise ValueError(f"Month '{month}' is not valid. Choose from {possible_months}.")