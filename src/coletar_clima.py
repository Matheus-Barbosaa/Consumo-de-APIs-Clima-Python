import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("HG_API_KEY")

cidades = [
    "São Paulo,SP",
    "Rio de Janeiro,RJ",
    "Curitiba,PR",
    "Florianópolis,SC",
    "Porto Alegre,RS"
]

url = "https://api.hgbrasil.com/weather"

dados_clima = []

for cidade in cidades:
    params = {
        "city_name": cidade,
        "locale": "pt",
        "key": api_key
    }

    print(f"\nConsultando: {cidade}")

    resposta = requests.get(url, params=params)
    print(resposta.status_code)

    dados = resposta.json()

    nome_cidade = dados["results"]["city"]
    temperatura = dados["results"]["temp"]
    condicao = dados["results"]["description"]
    umidade = dados["results"]["humidity"]
    vento = dados["results"]["wind_speedy"]
    probabilidade_chuva = dados["results"]["forecast"][0]["rain_probability"]

    registro = {
        "cidade": nome_cidade,
        "temperatura": temperatura,
        "condicao": condicao,
        "umidade": umidade,
        "vento": vento,
        "probabilidade_chuva": probabilidade_chuva
    }    

    dados_clima.append(registro)

    print(f"\nCidade: {cidade}")
    print(f"Temperatura: {temperatura} °C")
    print(f"Condição: {condicao}")
    print(f"Umidade: {umidade} %")
    print(f"Velocidade do vento: {vento}")
    print(f"Probabilidade de chuva: {probabilidade_chuva} %")

df = pd.DataFrame(dados_clima)

df.to_csv("data/raw/clima.csv", index=False)

print("\nDados salvos em data/raw/clima.csv")