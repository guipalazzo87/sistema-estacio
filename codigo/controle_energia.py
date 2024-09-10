import requests
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Endpoints para controle remoto
BASE_URL = "http://api.condominio.com/controle"

def ligar_equipamento(equipamento_id):
    if not isinstance(equipamento_id, int) or equipamento_id <= 0:
        logging.error("ID do equipamento inválido: %s", equipamento_id)
        return {"error": "ID do equipamento inválido"}

    try:
        response = requests.post(f"{BASE_URL}/ligar/{equipamento_id}")
        response.raise_for_status()
        logging.info("Equipamento %d ligado com sucesso.", equipamento_id)
        return response.json()
    except requests.RequestException as e:
        logging.error("Erro ao ligar o equipamento %d: %s", equipamento_id, e)
        return {"error": str(e)}

def desligar_equipamento(equipamento_id):
    if not isinstance(equipamento_id, int) or equipamento_id <= 0:
        logging.error("ID do equipamento inválido: %s", equipamento_id)
        return {"error": "ID do equipamento inválido"}

    try:
        response = requests.post(f"{BASE_URL}/desligar/{equipamento_id}")
        response.raise_for_status()
        logging.info("Equipamento %d desligado com sucesso.", equipamento_id)
        return response.json()
    except requests.RequestException as e:
        logging.error("Erro ao desligar o equipamento %d: %s", equipamento_id, e)
        return {"error": str(e)}

if __name__ == "__main__":
    # Exemplo de uso
    print(ligar_equipamento(1))
    print(desligar_equipamento(2))
