# Consumo de API de Clima com Python

## Sobre o projeto

Neste projeto, pratiquei o consumo de uma API de dados climáticos utilizando Python.

O objetivo foi buscar informações meteorológicas de cinco cidades brasileiras, organizar os dados, salvar em um arquivo CSV e realizar algumas análises utilizando Pandas.

## Tecnologias utilizadas

- Python
- Pandas
- Requests
- Python-dotenv
- API HG Brasil

## Cidades analisadas

- São Paulo - SP
- Rio de Janeiro - RJ
- Curitiba - PR
- Florianópolis - SC
- Porto Alegre - RS

## Como funciona

O projeto foi dividido em duas etapas principais.

### 1. Coleta dos dados

No arquivo `coletar_clima.py`, utilizei a biblioteca Requests para fazer as requisições à API HG Brasil.

Os dados coletados foram:

- Cidade
- Temperatura
- Condição do tempo
- Umidade
- Velocidade do vento
- Probabilidade de chuva

Depois da coleta, organizei os dados em uma lista de dicionários e transformei essa estrutura em um DataFrame utilizando Pandas.

Por fim, os dados foram salvos no arquivo `data/raw/clima.csv`.

### 2. Análise dos dados

No arquivo `analisar_clima.py`, carreguei o arquivo CSV utilizando Pandas.

Também fiz um tratamento na coluna de velocidade do vento, removendo o texto `km/h` e convertendo os valores para `float`.

Depois disso, realizei algumas análises:

- Cidade mais quente
- Cidade com menor temperatura
- Temperatura média
- Diferença entre maior e menor temperatura
- Maior probabilidade de chuva
- Menor probabilidade de chuva
- Cidade com maior umidade
- Maior velocidade do vento
- Velocidade média do vento
- Quantidade de cidades com probabilidade de chuva

## Uso da chave da API

A chave da API não foi colocada diretamente no código.

Utilizei um arquivo `.env` para armazenar a chave:

HG_API_KEY=sua_chave_aqui

No Python, utilizei `python-dotenv` para carregar essa variável de ambiente.

O arquivo `.env` está incluído no `.gitignore` para evitar que a chave seja enviada para o GitHub.

## Estrutura do projeto

O projeto está organizado em pastas para separar os dados dos códigos.

A pasta `data` contém o arquivo CSV com os dados coletados.

A pasta `src` contém os scripts Python utilizados para coletar e analisar os dados.

O arquivo `.env` armazena a chave da API, enquanto o `.gitignore` impede que esse arquivo seja enviado para o GitHub.

O `requirements.txt` contém as bibliotecas utilizadas no projeto e o `README.md` apresenta as informações e explicações sobre o projeto.

## Principais aprendizados

Neste projeto, pratiquei:

- Consumo de API utilizando Requests
- Uso de parâmetros em requisições HTTP
- Uso de chave de API através de variável de ambiente
- Organização dos dados em dicionários
- Criação de DataFrame com Pandas
- Exportação de dados para CSV
- Tratamento e conversão de tipos de dados
- Análise estatística básica
- Uso de `mean()`, `max()`, `min()`, `idxmax()` e `idxmin()`
- Filtragem de dados com Pandas
- Criação de conclusões a partir dos dados

## Conclusões

A partir dos dados coletados, foi possível identificar algumas diferenças entre as cidades analisadas.

O Rio de Janeiro apresentou a maior temperatura, com 21 °C, e também a maior probabilidade de chuva, com 100%.

Curitiba apresentou a menor temperatura, com 14 °C, e a maior umidade, com 85%.

A temperatura média das cinco cidades analisadas foi de 17 °C.

Florianópolis apresentou a maior velocidade do vento, com 20,38 km/h.

No momento da coleta, duas das cinco cidades apresentaram alguma probabilidade de chuva.

## Observação

Este projeto faz parte da minha formação em Análise de Dados e foi desenvolvido com foco em prática de Python, consumo de APIs, tratamento de dados e análise exploratória.