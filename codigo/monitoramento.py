import pandas as pd
import sqlite3
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Conectar ao banco de dados
def conectar_banco():
    try:
        conn = sqlite3.connect('energia.db')
        return conn
    except sqlite3.Error as e:
        logging.error("Erro ao conectar ao banco de dados: %s", e)
        return None

# Coletar dados do sensor
def coletar_dados():
    # Código para coletar dados dos sensores
    # Exemplo de dados coletados
    dados = [
        {"hora": "2024-09-01 00:00:00", "consumo": 10.5},
        {"hora": "2024-09-01 01:00:00", "consumo": 12.3},
        # Adicione mais dados conforme necessário
    ]
    return dados

# Salvar dados no banco de dados
def salvar_dados(conn, dados):
    try:
        df = pd.DataFrame(dados)
        df.to_sql('consumo', conn, if_exists='append', index=False)
        logging.info("Dados salvos com sucesso.")
    except Exception as e:
        logging.error("Erro ao salvar dados: %s", e)

if __name__ == "__main__":
    conn = conectar_banco()
    if conn:
        dados = coletar_dados()
        salvar_dados(conn, dados)
        conn.close()
