import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import sqlite3
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Conectar ao banco de dados SQLite
def obter_dados():
    try:
        conn = sqlite3.connect('energia.db')
        query = "SELECT hora, consumo FROM consumo"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except sqlite3.Error as e:
        logging.error("Erro ao conectar ao banco de dados: %s", e)
        return pd.DataFrame(columns=['hora', 'consumo'])

# Inicializar o aplicativo Dash
app = dash.Dash(__name__)

# Layout do Dashboard
app.layout = html.Div([
    html.H1("Dashboard de Consumo de Energia"),
    dcc.Graph(
        id='grafico-consumo',
        figure={}
    ),
    html.Div([
        html.Label("Selecione o período:"),
        dcc.DatePickerRange(
            id='selecao-periodo',
            start_date='2024-09-01',
            end_date='2024-09-30',
            display_format='DD/MM/YYYY'
        )
    ]),
    html.Div(id='indicadores')
])

# Callback para atualizar o gráfico com base na seleção de período
@app.callback(
    dash.dependencies.Output('grafico-consumo', 'figure'),
    [dash.dependencies.Input('selecao-periodo', 'start_date'),
     dash.dependencies.Input('selecao-periodo', 'end_date')]
)
def atualizar_grafico(start_date, end_date):
    if not start_date or not end_date:
        return px.line(title='Consumo de Energia ao Longo do Tempo')

    df = obter_dados()
    df['hora'] = pd.to_datetime(df['hora'])
    df = df[(df['hora'] >= start_date) & (df['hora'] <= end_date)]

    fig = px.line(df, x='hora', y='consumo', title='Consumo de Energia ao Longo do Tempo')
    fig.update_layout(xaxis_title='Data e Hora', yaxis_title='Consumo (kWh)')
    return fig

# Iniciar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
