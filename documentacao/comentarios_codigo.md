# Comentários do Código

## `monitoramento.py`

- **Função `coletar_dados()`:** Coleta dados dos sensores IoT e os retorna como uma lista de dicionários.
- **Função `salvar_dados(dados)`:** Recebe os dados coletados e os salva no banco de dados SQLite.

## `controle_energia.py`

- **Função `ligar_equipamento(equipamento_id)`:** Envia uma solicitação para ligar um equipamento específico.
- **Função `desligar_equipamento(equipamento_id)`:** Envia uma solicitação para desligar um equipamento específico.

## `dashboard.py`

- **Configuração do Dash:** Cria um dashboard interativo para visualizar o consumo de energia.
- **Gráfico:** Exibe o consumo de energia ao longo do tempo usando a biblioteca Plotly.
