import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash, callback, Output, Input
import dash

from api.api import tiktok_data

df_tiktok = tiktok_data()

# Registrando a página
dash.register_page(__name__, path="/tiktok", name="Tiktok", svg="icons/tiktok.svg")

# Função de callback para armazenar o DataFrame
@callback(
    Output('data-store11', 'data'),
    Input('data-store11', 'id')
)
def store_data(id11):
    # Criando um DataFrame do zero
    values = df_tiktok
    return values.to_dict('records')  # Convertendo o DataFrame para um dicionário
#print('hello', df_tiktok)
@callback(
    Output('data-store12', 'data'),
    Input('data-store12', 'id')
)
def store_data(id12):
    # Criando um DataFrame do zero
    values = df_tiktok
    return values.to_dict('records')

@callback(
    Output('data-store13', 'data'),
    Input('data-store13', 'id')
)
def store_data(id13):
    # Criando um DataFrame do zero
    values = df_tiktok
    return values.to_dict('records')

# Função de callback para atualizar o gráfico
@callback(
    Output('grafico_seguidores_tiktok', 'figure'),
    Input('data-store11', 'data')
)
def update_graph(data):
    values = pd.DataFrame(data)  # Convertendo o dicionário de volta para um DataFrame
    # Criando um gráfico com Plotly Express
    fig = px.bar(values, x='MESES', y='SEGUIDORES', color_discrete_sequence=['#01D8B6'])
    fig.update_layout(
        plot_bgcolor= "#000000",
        paper_bgcolor = "#000000",
        legend=dict(font=dict(color="white")),
        font=dict(color="white")
    )
    return fig

@callback(
    Output('grafico_engajamento_tiktok', 'figure'),
    Input('data-store12', 'data')
)
def update_graph(data):
    values = pd.DataFrame(data)  # Convertendo o dicionário de volta para um DataFrame
    # Criando um gráfico com Plotly Express
    fig = px.line(values, x='MESES', y=['COMENTÁRIOS','CURTIDAS'], color_discrete_sequence=['#61FF2B','#01D8B6'])
    fig.update_layout(
        plot_bgcolor= "#000000",
        paper_bgcolor = "#000000",
        legend=dict(font=dict(color="white")),
        font=dict(color="white")
    )
    return fig

@callback(
    Output('grafico_alcance_tiktok', 'figure'),
    Input('data-store13', 'data')
)
def update_graph(data):
    values = pd.DataFrame(data)  # Convertendo o dicionário de volta para um DataFrame
    # Criando um gráfico com Plotly Express
    fig = px.bar(values, x='MESES', y='ALCANCE', color_discrete_sequence=['#01D8B6'])
    fig.update_layout(
        plot_bgcolor= "#000000",
        paper_bgcolor = "#000000",
        legend=dict(font=dict(color="white")),
        font=dict(color="white")
    )
    return fig

# Layout do dashboard
layout = html.Div([
    html.H1("TikTok",style={"text-align":"center","color": "white", "background-color":"#000000", "border-radius": "20px", "overflow": "hidden"}),
    html.Div(
        style={"display": "flex","flex-direction":"column", "align-items": "center", "background-color": "#141414"},
        children=[
            # Divs de cima
            html.Div(
                style={"display": "flex", "justify-content": "space-around", "width": "100%",'height': '450px', "margin-bottom":"20px", "margin-top":"20px"},
                children=[
                    html.Div(
                        children=[
                            html.H3("Seguidores", style={"color": "white", "text-align":"center"}),
                            dcc.Graph(id="grafico_seguidores_tiktok", style={'width': '600px', 'height': '400px', "border-radius": "20px", "overflow": "hidden", "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.2)"})],
                        style={"background-color": "black", "border-radius": "20px", "overflow": "hidden"}
                    ),
                    html.Div(
                        children=[
                            html.H3("Engajamento", style={"color": "white",  "text-align":"center"}),
                            dcc.Graph(id='grafico_engajamento_tiktok', style={'width': '600px', 'height': '400px', "border-radius": "20px", "overflow": "hidden"})],
                            style={"background-color": "black", "border-radius": "20px", "overflow": "hidden"}
                    ),
                ]
            ),
            # Divs de baixo
            html.Div(
                style={"display": "flex", "justify-content": "space-around", "width": "1500px", "height":"450px"},
                children=[
                    html.Div(
                        style={'display':'flex','flex-direction':'column',"justify-content": "space-around",'align-items': 'center', 'width': '600px',"height":"400px", "background-color":"#000000","border-radius": "20px", "overflow": "hidden"},
                        children=[
                            html.Div(
                                children=[
                                    html.H4("Seguidores", style={"text-align": "center", "color": "white"}),
                                    html.P("n°", style={"text-align": "center"})],
                                    style={"margin-top":"10px",'width':'500px',"background-color":"#141414", "border-radius": "20px", "overflow": "hidden"}
                            ),
                            html.Div(
                                style={"display": "flex", "align-items": "center", "margin-top":"10px"},
                                children=[
                                    html.Div(
                                        style={'width':'235px',"align-items":"center", "background-color":"#141414", "border-radius": "20px", "overflow": "hidden"},
                                        children=[
                                            html.H4("Alcance", style={"text-align":"center", "color":"white"}),
                                            html.P("n°", style={"text-align": "center", "color":"white"})],
                                    ),
                                    html.Div(
                                        children=[
                                            html.H4("Engajamento", style={"text-align": "center", "color":"white"}),
                                            html.P("n°", style={"text-align": "center", "color":"white"})],
                                            style={'width':'235px','margin-left': '30px', "background-color":"#141414", "border-radius": "20px", "overflow": "hidden"}
                                    )
                                ]
                            ),
                            html.Div(
                                style={"display": "flex", "justify-content": "space-around", "margin-top":"10px"},
                                children=[
                                    html.Div(
                                        style={'width':'235px',"align-items":"center", "background-color":"#141414", "border-radius": "20px", "overflow": "hidden"},
                                        children=[
                                            html.H4("Alcance", style={"text-align":"center", "color":"white"}),
                                            html.P("n°", style={"text-align": "center", "color":"white"})],
                                    ),
                                    html.Div(
                                        children=[
                                            html.H4("Engajamento", style={"text-align": "center", "color":"white"}),
                                            html.P("n°", style={"text-align": "center", "color":"white"})],
                                            style={'width':'235px','margin-left': '30px', "background-color":"#141414", "border-radius": "20px", "overflow": "hidden"}
                                    )
                                ]
                            )
                        ]
                    ),
                    html.Div(
                        children=[
                            html.H3("Alcance", style={"color": "white",  "text-align":"center"}),
                            dcc.Graph(id='grafico_alcance_tiktok', style={'width': '600px', 'height': '400px'})],
                            style={"background-color": "black", "border-radius": "20px", "overflow": "hidden"}
                    ),
                ]
            ),
        ]
    ),
    html.Div([
    ], className='row'),
    dcc.Store(id='data-store11'),
    dcc.Store(id='data-store12'),
    dcc.Store(id='data-store13')
])