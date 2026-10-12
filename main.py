from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

URL    = "https://www.rpachallenge.com/?lang=EN"
tabela = pd.read_excel("challenge.xlsx")

# Programa Principal
navegador = webdriver.Chrome()
navegador.get(URL)
navegador.maximize_window()
navegador.find_element(By.XPATH, "//*[@class='waves-effect col s12 m12 l12 btn-large uiColorButton']").click()

# Preenchimento automatico do formulário
for i, email in enumerate(tabela["Email"]):
    
    # Email
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').send_keys(email)

    # First name - Primeiro nome
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys(f"{tabela.loc[i]["First Name"]}")

    # Last name - Sobrenome
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys(f"{tabela.loc[i]["Last Name "]}")

    # Role in the company - Papel na compania
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').send_keys(f"{tabela.loc[i]["Role in Company"]}")

    # Company name - Nome da compania
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').send_keys(f"{tabela.loc[i]["Company Name"]}")

    # Phone number - Número de telefone
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').send_keys(f"{tabela.loc[i]["Phone Number"]}")

    # Address - endereço
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').send_keys(f"{tabela.loc[i]["Address"]}")

    print(f"{i+1:<2} {email:<24} | {tabela.loc[i]["First Name"]:<10}{tabela.loc[i]["Last Name "]:<10}"
          f"| {tabela.loc[i]["Company Name"]:<13} | {tabela.loc[i]["Role in Company"]:<16}"
          f"| {tabela.loc[i]["Address"]:<22} | {tabela.loc[i]["Phone Number"]}")

    navegador.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

from time import sleep
sleep(5)
navegador.quit()
