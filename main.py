from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

def preencher_campos_x(driver:webdriver, selectors:dict, dataframe:pd):
    """_summary_

    Args:
        driver (webdriver): Recebe o navegador usado no projeto.
        selectors (dict): Recebe um dicionário com o nome das colunas(keys) e os valores(values) com XPATH do site. 
        dataframe (pandas): Recebe o arquivo Excel.

    Returns:
        None
    """
    for i in range(dataframe.shape[0]):
        print(f'--> \033[1mUser index\033[m: {i}')
        for c in selectors:
            print(f"{c:<15} | {dataframe[c][i]:<25} | {selectors[c]}")
            driver.find_element(By.XPATH, f'{selectors[c]}').send_keys(str(dataframe[c][i]))
        driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click() # SUBMIT / ENVIAR
        print()
    return None


URL    = "https://www.rpachallenge.com/?lang=EN"
TABELA = pd.read_excel('challenge.xlsx')
CAMPOS = { # campos a serem preenchidos + locators/Seletores
    'Email'              :'//*[@ng-reflect-name="labelEmail"]',
    'First Name'         :'//*[@ng-reflect-name="labelFirstName"]',
    'Last Name'          :'//*[@ng-reflect-name="labelLastName"]',
    'Role in Company'    :'//*[@ng-reflect-name="labelRole"]',
    'Company Name'       :'//*[@ng-reflect-name="labelCompanyName"]',
    'Phone Number'       :'//*[@ng-reflect-name="labelPhone"]',
    'Address'            :'//*[@ng-reflect-name="labelAddress"]'
}


### Programa Principal 
navegador = webdriver.Chrome()
navegador.get(URL)
navegador.maximize_window()
navegador.find_element(By.XPATH, "//*[@class='waves-effect col s12 m12 l12 btn-large uiColorButton']").click() # START / COMEÇAR

preencher_campos_x(driver=navegador , selectors=CAMPOS, dataframe=TABELA)

sleep(5) 
navegador.quit()
