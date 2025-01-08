# web_scrapy_produtos_mais_vendidos

## Configuração Inicial

- Criar o ambiente virtual

 '''python

    python -m venv venv
 '''
pip freeze > requirements.txt
pip install -r requirements.txt

- iniciar o projeto
scrapy startproject nome_do_projeto

cd coleta nome_do_projeto

## Extração dos dados
- Extrair os dados da página das categorias do mercado livre 
   realizado a verificação pelo terminal
scrapy shell
fetch('https://www.mercadolivre.com.br/categorias')
response.css('h2.categories__title')
seu tamanho



## Transformação dos dados

## Dashboard
