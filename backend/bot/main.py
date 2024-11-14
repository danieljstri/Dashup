import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import traceback

# loading ambient variables from .env
load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# chrome config
chrome_options = Options()
chrome_options.add_argument('--headless')  # executing without UI
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# initializing the webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # go to login page
    driver.get('https://app.sittax.com.br/login')
    print("Navegou para a página de login")

    # wait until the email and password fields are present
    wait = WebDriverWait(driver, 20)
    email_field = wait.until(EC.presence_of_element_located((By.ID, 'emailUsuarioAuth')))
    password_field = driver.find_element(By.ID, 'passwordUsuarioAuth')
    login_button = driver.find_element(By.XPATH, '//button[@type="button" and contains(@class, "btn-login")]')
    print("Campos de email e senha encontrados")

    # insert credentials and press login button
    email_field.send_keys(EMAIL)
    password_field.send_keys(PASSWORD)
    login_button.click()
    print("Credenciais inseridas e login realizado")

    # wait until the login is successful and the navigation bar is present
    wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/apuracao")]')))
    print("Login bem-sucedido e barra de navegação presente")

    # navigate to the apuração page
    driver.get('https://app.sittax.com.br/apuracao/simplesNacional')
    print("Navegou para a página de apuração")

    # wait until the dropdown of companies is present
    wait.until(EC.presence_of_element_located((By.NAME, 'selectHeaderEmpresasInput')))
    print("Dropdown de empresas presente")

    # verify if there is a warning modal and close it
    try:
        modal_close_button = driver.find_element(By.XPATH, '//div[contains(@class, "swal2-popup")]//button[contains(@class, "swal2-confirm")]')
        modal_close_button.click()
        print("Modal de aviso fechado")
    except:
        print("Nenhum modal de aviso presente")

    # initialize the list to store the data
    data = []

    # open the dropdown and focus on the element of the companies
    dropdown = driver.find_element(By.NAME, 'selectHeaderEmpresasInput')
    dropdown.click()
    print("Dropdown de empresas aberto")

    # press ENTER to select the first company
    dropdown.send_keys(Keys.ENTER)
    print("Primeira empresa selecionada")

    # wait until the company name is visible
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ng-value')))
    company_name_element = driver.find_element(By.CSS_SELECTOR, '.ng-value')
    current_company = company_name_element.text.strip()
    print(f"Empresa atual: {current_company}")

    # initialize a set to store the processed companies
    processed_companies = set()
    processed_companies.add(current_company)

    while True:
        try:
            # wait until the RBT12 and RBA values are present
            wait.until(EC.text_to_be_present_in_element((By.XPATH, '//span[text()="Faturamento dos últimos 12 meses (RBT12)"]/preceding-sibling::div'), 'R$'))
            wait.until(EC.text_to_be_present_in_element((By.XPATH, '//span[text()="Receita do ano (RBA)"]/preceding-sibling::div'), 'R$'))

            # extract the RBT12 and RBA values
            rbt12_element = driver.find_element(By.XPATH, '//span[text()="Faturamento dos últimos 12 meses (RBT12)"]/preceding-sibling::div')
            rba_element = driver.find_element(By.XPATH, '//span[text()="Receita do ano (RBA)"]/preceding-sibling::div')

            rbt12 = rbt12_element.text.replace('R$', '').strip()
            rba = rba_element.text.replace('R$', '').strip()

            # add the data to the DF
            data.append({
                'empresa': current_company,
                'rbt12': rbt12,
                'rba': rba
            })
            print(f"Dados extraídos para {current_company}: RBT12={rbt12}, RBA={rba}")

            # open the dropdown again
            dropdown = driver.find_element(By.NAME, 'selectHeaderEmpresasInput')
            dropdown.click()
            time.sleep(0.5)  

            # press ARROW_DOWN to select the next company
            dropdown.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)  # little delay to avoid errors

            # pressing ENTER to select the company
            dropdown.send_keys(Keys.ENTER)
            print("Próxima empresa selecionada")

            # await the next company name to be visible
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ng-value')))
            company_name_element = driver.find_element(By.CSS_SELECTOR, '.ng-value')
            new_company = company_name_element.text.strip()

            # verify if all companies have been processed
            if new_company in processed_companies:
                print("Todas as empresas foram processadas.")
                break

            # update the current company
            current_company = new_company
            processed_companies.add(current_company)
            print(f"Empresa atual: {current_company}")

        except Exception as e:
            print(f"Erro ao processar a empresa {current_company}: {e}")
            traceback.print_exc()
            break

    # create a df and save to a csv
    df = pd.DataFrame(data)
    df.to_csv('sittax_data.csv', index=False)
    print("Dados salvos em sittax_data.csv")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    traceback.print_exc()

finally:
    # close the webdriver
    driver.quit()
