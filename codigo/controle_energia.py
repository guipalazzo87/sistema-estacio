import requests

# Endpoints para controle remoto
BASE_URL = "http://api.condominio.com/controle"

def ligar_equipamento(equipamento_id):
    response = requests.post(f"{BASE_URL}/ligar/{equipamento_id}")
    return response.json()

def desligar_equipamento(equipamento_id):
    response = requests.post(f"{BASE_URL}/desligar/{equipamento_id}")
    return response.json()

if __name__ == "__main__":
    # Exemplo de uso
    ligar_equipamento(1)
    desligar_equipamento(2)
