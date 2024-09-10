import pandas as pd
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('energia.db')

# Coletar dados do sensor
def coletar_dados():
    # Código para coletar dados dos sensores
    pass

# Salvar dados no banco de dados
def salvar_dados(dados):
    df = pd.DataFrame(dados)
    df.to_sql('consumo', conn, if_exists='append', index=False)

if __name__ == "__main__":
    dados = coletar_dados()
    salvar_dados(dados)
