import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash, callback, Output, Input
import dash

from api.api import youtube_data

df_youtube= youtube_data()
# Registrando a página
dash.register_page(__name__, path="/youtube", name="Youtube", svg="icons/youtube.svg")

# Função de callback para armazenar o DataFrame
@callback(
    Output('data-store31', 'data'),
    Input('data-store31', 'id')
)
def store_data(id):
    # Criando um DataFrame do zero
    values = df_youtube
    return values.to_dict('records')  # Convertendo o DataFrame para um dicionário

# Função de callback para atualizar o gráfico
@callback(
    Output('grafico_seguidores_youtube', 'figure'),
    Input('data-store31', 'data')
)
def update_graph(data):
    values = pd.DataFrame(data)
    values.apply(pd.to_numeric, errors='coerce')  # Convertendo o dicionário de volta para um DataFrame
    # Criando um gráfico com Plotly Express
    fig = px.bar(values, x='MESES', y='INSCRITOS', color_discrete_sequence=['#01D8B6'])
    fig.update_layout(
        plot_bgcolor= "#000000",
        paper_bgcolor = "#000000",
        legend=dict(font=dict(color="white")),
        font=dict(color="white")
    )
    return fig

# Layout do dashboard
layout = html.Div([
    html.H1("Youtube",style={"text-align":"center","color": "white", "background-color":"#000000", "border-radius": "20px", "overflow": "hidden"}),
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
                            dcc.Graph(id="grafico_seguidores_youtube", style={'width': '600px', 'height': '400px', "border-radius": "20px", "overflow": "hidden", "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.2)"})],
                        style={"background-color": "black", "border-radius": "20px", "overflow": "hidden"}
                    ),
                    html.Div(
                        children=[
                            html.H3("Engajamento", style={"color": "white",  "text-align":"center"}),
                            dcc.Graph(id='grafico_engajamento_youtube', style={'width': '600px', 'height': '400px', "border-radius": "20px", "overflow": "hidden"})],
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
                            dcc.Graph(id='grafico_alcance_youtube', style={'width': '600px', 'height': '400px'})],
                            style={"background-color": "black", "border-radius": "20px", "overflow": "hidden"}
                    ),
                ]
            ),
        ]
    ),
    html.Div([
    ], className='row'),
    dcc.Store(id='data-store31'),
    dcc.Store(id='data-store32'),
    dcc.Store(id='data-store33')
])