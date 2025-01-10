import sqlite3
import pandas as pd
from datetime import datetime
import os

# Caminho para o arquivo JSONL
json_path = "../datasets/mais_vendidos.jsonl"
if not os.path.exists(json_path):
    raise FileNotFoundError(f"Arquivo {json_path} não encontrado.")
# Ler o arquivo JSONL
df = pd.read_json(json_path, lines=True)
#print(df)
# Exibir todas as colunas
pd.options.display.max_columns = None
#print(df.columns)
# Adicionar colunas fixas
df["_source"] = "https://www.mercadolivre.com.br/mais-vendidos/"
df["_data_coleta"] = datetime.now()
#print(df)
# Tratar colunas numéricas (preencher valores ausentes e converter para float)
for column in [
    "old_price_reais",
    "old_price_centavos",
    "new_price_reais",
    "new_price_centavos",
    "reviews_rating_number",
]:
    if column in df.columns:
        df[column] = df[column].fillna(0).astype(float)
    else:
        df[column] = 0.0
#print(df)

# remover "Mais vendidos em  " da coluna Category
df['category'] = df['category'].str.replace("Mais vendidos em ", "", regex=False )
#print(df)

# Tratar a coluna reviews_amount
if "reviews_amount" in df.columns:
    df["reviews_amount"] = (
        df["reviews_amount"].fillna("0").str.replace(r"[\(\)]", "", regex=True)
    )
    df["reviews_amount"] = (
        pd.to_numeric(df["reviews_amount"], errors="coerce").fillna(0).astype(int)
    )
else:
    df["reviews_amount"] = 0
    
#print(df)

# Calcular preços totais
df["old_price"] = df["old_price_reais"] + df["old_price_centavos"] / 100
df["new_price"] = df["new_price_reais"] + df["new_price_centavos"] / 100

# Remover colunas de preços desnecessárias
df = df.drop(
    columns=[
        "old_price_reais",
        "old_price_centavos",
        "new_price_reais",
        "new_price_centavos",
    ]
)
#print(df)

# verificar NaN da coluna podio
nan_indices = df[df['podio'].isna()].index
#print(nan_indices)

# remover a linha Nan da coluna podio
df = df.dropna(subset=['podio'])
nan_indices = df[df["podio"].isna()].index
#print(nan_indices)

# Extrair o número do ranking da coluna 'podio' e criar uma nova coluna
df["ranking_number"] = df["podio"].str.extract(r"(\d+)")

# Converter a coluna 'ranking_number' para inteiro
df["ranking_number"] = df["ranking_number"].astype(int)

# Verificar o DataFrame final
#print(df.dtypes)
print(df["ranking_number"].unique())
# salvar o dataframe em uma arquivo csv
df.to_csv('../datasets/df_produtosmaisvendidos.csv', index=False, encoding="utf-8")

# Conectar ao banco de dados SQLite
conn = sqlite3.connect("../datasets/mlprodutosmaisvendidos.db")

# Salvar no banco de dados
df.to_sql("mercadolivre_maisvendidos", conn, if_exists="replace", index=False)

# Fechar conexão
conn.close()

# Exibir o DataFrame resultante
print("Banco de dados criado com sucesso!")
print(df.head())
