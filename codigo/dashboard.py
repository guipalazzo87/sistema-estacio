import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('energia.db')
df = pd.read_sql_query("SELECT * FROM consumo", conn)

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        id='grafico-consumo',
        figure=px.line(df, x='hora', y='consumo', title='Consumo de Energia')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
