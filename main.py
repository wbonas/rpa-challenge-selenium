from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException
from time import sleep
import pandas as pd

def preencher_campos_x(driver:webdriver, selectors:dict, dataframe:pd):
    """Percorre todo o arquivo excel e preenche um formulário, o enviando em seguida.

    Args:
        driver (webdriver): Navegador usado no projeto.
        selectors (dict)  : Dicionário com o nome das colunas(keys) e os valores(values) com XPATH do site. 
        dataframe (pandas): Arquivo Excel.

    Returns:
        None
    """

    try: 
        for i in range(dataframe.shape[0]):
            print(f'--> \033[1mUser index\033[m: {i}')
            for c in selectors:
                print(f"{c:<15} | {dataframe[c][i]:<25} | {selectors[c]}")
                wait.until(EC.presence_of_element_located((By.XPATH, f'{selectors[c]}'))).send_keys(str(dataframe[c][i]))

            driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click() # SUBMIT / ENVIAR
            print()
        return None
        
    except AttributeError as erro:
        raise AttributeError('o atributo inserido não corresponde aos parâmetros da função.', erro)

    except NoSuchWindowException as erro:
        raise NoSuchWindowException('O Programa não encontrou o seletor usado.', erro)

    except KeyError as erro:
        raise KeyError('O XPATH do seletor não foi encontrado ou não existe. Verifique a linha do XPATH.', erro)


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
try:
    navegador = webdriver.Chrome()
    wait      = WebDriverWait(navegador, 5)
    navegador.get(URL)
    navegador.maximize_window()
    navegador.find_element(By.XPATH, "//*[@class='waves-effect col s12 m12 l12 btn-large uiColorButton']").click() # START / COMEÇAR
    preencher_campos_x(driver=navegador , selectors=CAMPOS, dataframe=TABELA)

except NoSuchWindowException:
    print("\033[31:1mNoSuchWindowException: A janela do navegador foi fechada.\033[m")

finally: # Mantém o site aberto para ver o resultado final e fecha o navegador corretamente.
    sleep(5) 
    print('\nPrograma finalizado com êxito!')
    navegador.quit()
