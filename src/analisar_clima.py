import pandas as pd

# CARREGAMENTO DOS DADOS

df = pd.read_csv("data/raw/clima.csv")

# TRATAMENTO DOS DADOS

df["vento"] = df["vento"].str.replace(" km/h", "")
df["vento"] = df["vento"].astype(float)

df.info()

# ANÁLISES

print(df.describe())

# MAIOR TEMPERATURA

cidade_mais_quente = df.loc[df["temperatura"].idxmax()]

print(f"\nCidade mais quente: {cidade_mais_quente['cidade']}")
print(f"Temperatura: {cidade_mais_quente['temperatura']} °C")

# MAIOR PROBABILIDADE DE CHUVA

cidade_maior_chuva = df.loc[df["probabilidade_chuva"].idxmax()]

print(f"\nMaior probabilidade de chuva: {cidade_maior_chuva['cidade']}")
print(f"Probabilidade: {cidade_maior_chuva['probabilidade_chuva']} %")

# MAIOR UMIDADE

cidade_maior_umidade = df.loc[df["umidade"].idxmax()]

print(f"\nCidade com maior umidade: {cidade_maior_umidade['cidade']}")
print(f"Umidade: {cidade_maior_umidade['umidade']} %")

# MENOR TEMPERATURA

cidade_menor_temperatura = df.loc[df["temperatura"].idxmin()]

print(f"\nCidade com menor temperatura: {cidade_menor_temperatura['cidade']}")
print(f"Temperatura: {cidade_menor_temperatura['temperatura']} °C")

# TEMPERATURA MÉDIA

media_temperatura = df["temperatura"].mean()
print(f"\nTemperatura média das cidades: {media_temperatura:.1f} °C")

# DIFERENÇA ENTRE MAIOR E MENOR TEMPERATURA

maior_temperatura = df["temperatura"].max()
menor_temperatura = df["temperatura"].min()

diferenca_temperatura = maior_temperatura - menor_temperatura

print(f"\nDiferença entre maior e menor temperatura: {diferenca_temperatura} °C")

# MENOR PROBABILIDADE DE CHUVA

cidade_menor_chuva = df.loc[df["probabilidade_chuva"].idxmin()]

print(f"\nMenor probabilidade de chuva: {cidade_menor_chuva['cidade']}")
print(f"Probabilidade: {cidade_menor_chuva['probabilidade_chuva']} %")

# MAIOR VELOCIDADE DO VENTO

cidade_maior_vento = df.loc[df["vento"].idxmax()]

print(f"\nMaior velocidade do vento: {cidade_maior_vento['cidade']}")
print(f"Velocidade: {cidade_maior_vento['vento']:.2f} km/h")

# CIDADES COM PROBABILIDADE DE CHUVA

cidades_com_chuva = df[df["probabilidade_chuva"] > 0]

print(f"\nCidades com probabilidade de chuva: {len(cidades_com_chuva)}")

# VELOCIDADE MÉDIA DO VENTO

media_vento = df["vento"].mean()

print(f"\nVelocidade média do vento: {media_vento:.2f} km/h")

# CONCLUSÕES

print("\n==============================")
print("CONCLUSÕES")
print("==============================")

print(f"- {cidade_mais_quente['cidade']} apresentou a maior temperatura, com {cidade_mais_quente['temperatura']} °C.")

print(f"- {cidade_menor_temperatura['cidade']} apresentou a menor temperatura, com {cidade_menor_temperatura['temperatura']} °C.")

print(f"- A temperatura média entre as cidades analisadas foi de {media_temperatura:.1f} °C.")

print(f"- {cidade_maior_chuva['cidade']} apresentou a maior probabilidade de chuva, com {cidade_maior_chuva['probabilidade_chuva']}%.")

print(f"- {len(cidades_com_chuva)} das {len(df)} cidades apresentaram alguma probabilidade de chuva.")

print(f"- {cidade_maior_umidade['cidade']} apresentou a maior umidade, com {cidade_maior_umidade['umidade']}%.")

print(f"- {cidade_maior_vento['cidade']} apresentou a maior velocidade do vento, com {cidade_maior_vento['vento']:.2f} km/h.")