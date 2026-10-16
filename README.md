# Desafio RPA - Input forms

Esse projeto cumpre um desafio de preenchimento de formulário automático, do site [Rpa Challenge](https://www.rpachallenge.com). Onde os campos do formulário se alteram de maneira aleatória, a cada novo submit.

### Tecnologias Utilizadas

* Python 3.11

* [Selenium](https://pypi.org/project/selenium/)

* [Pandas](https://pypi.org/project/pandas/)

* [Openpyxl](https://pypi.org/project/openpyxl/)

## Funcionamento do programa | main.py

1. Lê o arquivo Excel challenge.xlsx fornecido pelo site e inicializa o navegador [Google Chrome](https://www.google.com/intl/pt-BR/chrome/).

2. Inicia o desafio clicando no botão de START.

3. Percorre os registros da planilha e preenche automaticamente os campos correspondentes aos dados de cada funcionário.

4. Envia cada formulário clicando no botão SUBMIT.

5. Ao concluir o preenchimento de todos os registros, finaliza o desafio e exibe os resultados da automação.

## Instalação e execução

Pré-requisitos: Python 3.11 ou compatível e Google Chrome instalado.

### Passo a passo

1. Clone o repositório e entre na pasta do projeto:

```

git clone URL_DO_REPOSITORIO

cd NOME_DO_PROJETO

```

2. Crie um ambiente virtual:

```

python -m venv .venv

```

3. Ative o ambiente virtual no Windows:

```

.venv\Scripts\activate

```

4. Instale as dependências:

```

python -m pip install -r requirements.txt

```

5. Execute o programa:

```

python main.py

```

O arquivo challenge.xlsx deve estar disponível na pasta do projeto para que o programa possa ler os dados.

Quando o desafio for concluído, os resultados da automação serão exibidos na página do site e no terminal.

## ✅ Resultados

![Resultado do desafio no site](/screenshots/Resultado_site.png)

![Resultado no terminal](/screenshots/Resultado_terminal.png)

## ⚠️ Problemas enfrentados

Esses foram alguns dos problemas que eu enfrentei durante esse projeto.

### Locators/Seletores:

No site do desafio, os localizadores de Id e Class são alterados a cada SUBMIT, Então tive de usar XPATH específico para concluir o desafio:

```

'//*[@ng-reflect-name="label..."]'

```

O mesmo problema se repetiu para a seleção dos botões de START e SUBMIT.

## ⏭️ Próximos passos

- [x] Organizar o código com função reutilizável.

- [ ] Adicionar esperas explícitas com WebDriveWait no lugar da função sleep.

- [ ] Adicionar tratamento de erros try/except/finally.

