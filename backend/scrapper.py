import requests
from bs4 import BeautifulSoup
import csv

def scrape_data_and_save_to_csv(url, csv_file_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    companies = soup.select('.company')
    revenues = soup.select('.revenue')
    
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['company_name', 'receita_bruta'])
        for company, revenue in zip(companies, revenues):
            company_name = company.get_text(strip=True)
            receita_bruta = revenue.get_text(strip=True)
            writer.writerow([company_name, receita_bruta])

scrape_data_and_save_to_csv('https://example.com/companies', 'companies.csv')
