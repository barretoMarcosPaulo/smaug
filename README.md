# SMAUG
## _Ranking dos gastos dos Deputados_

[![N|Solid](https://www.pngitem.com/pimgs/m/83-831537_transparent-smaug-png-smaug-hobbit-png-png-download.png)](https://www.pngitem.com/pimgs/m/83-831537_transparent-smaug-png-smaug-hobbit-png-png-download.png)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

A Cota para o Exercício da Atividade Parlamentar, custeia as despesas do mandato, como passagens aéreas e conta de celular. Algumas são reembolsadas, como as com os Correios, e outras são pagas por débito automático, como a compra de passagens. Nos casos de reembolso, os deputados têm três meses para apresentar os recibos. O projeto em questão tem a finalidade de fornecer algumas opções de visualizações dessas despesas, onde todo o processamento é feito em cima de um arquivo .csv que pode ser baixado no portal da trasparência.

## Funcionalidades


- Listagem dos deputados, filtrados por estado, ordernados pelo somatório de gastos;
- Cálculo e exibição do somatório de todos os gastos de cada deputado;
- Exibição dos dados do arquivo csv contendo os campos data de emissão, fornecedor, valor e url do documento;
- Relatório da maior despesa de um deputado;
- Busca de dados de um deputado específico;
- Menu interativo.

O Smaug tem como base o excelente projeto chamdo Serenata de Amor, https://serenata.ai/

## Tecnologias

Dillinger uses a number of open source projects to work properly:

- Python3
- Pandas
- Python Virtual Enviroment
- Pytest
- GIT

## Utilização

É necessário seguir os seguintes passos para a execução do projeto:

1 - Clonar este repositório
2 - Instalar o Python na versão 3
3 - [Opcional] Instalar um ambiente virtual e ativar
```sh
pip3 install --user virtualenv
python3 -m venv my_env
source my_env/bin/activate
```
4 - Instalar as Dependências(Necessário estar na raiz do projeto)
```sh
pip3 install -r requirements.txt
```

5 - Executar o arquivo principal(O projeto já possui um csv carregado no diretorio /data)
```sh
python3 src/index.py
```


## Rodando os testes
Foram criados alguns casos de testes unitários utilizando o pytest, os mesmos podem ser executados da seguinte forma na raiz do projeto:
```sh
pytest
```
