import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash, callback, Output, Input
import dash

from api.api import instagram_data

df_insta = instagram_data()

#print('ola:', df_insta)
# Registrando a página
dash.register_page(__name__, path="/instagram", name="Instagram", svg="icons/instagram.svg")

# Função de callback para armazenar o DataFrame
@callback(
    Output('data-store1', 'data'),
    Input('data-store1', 'data')
)
def store_data(id1):
    # Criando um DataFrame do zero
    values = df_insta  
    return values.to_dict()  # Convertendo o DataFrame para um dicionário

@callback(
    Output('data-store2', 'data'),
    Input('data-store2', 'id')
)
def store_data(id2):
    # Criando um DataFrame do zero
    values = df_insta
    return values.to_dict()

@callback(
    Output('data-store3', 'data'),
    Input('data-store3', 'id')
)
def store_data(id3):
    # Criando um DataFrame do zero
    values= df_insta
    return values.to_dict()

# Função de callback para atualizar o gráfico
@callback(
    Output('grafico_seguidores_instagram', 'figure'),
    Input('data-store1', 'data'),
)
def update_graph(data):
    values = pd.DataFrame(data)  # Convertendo o dicionário de volta para um DataFrame
    # Criando um gráfico com Plotly Express
    fig = px.bar(values, x='MESES', y='SEGUIDORES',color_discrete_sequence=['#01D8B6'])
    fig.update_layout(
        plot_bgcolor= "#000000",
        paper_bgcolor = "#000000",
        legend=dict(font=dict(color="white")),
        font=dict(color="white")
    )
    return fig

@callback(
    Output('grafico_alcance_instagram', 'figure'),
    Input('data-store2', 'data')
)
def update_graph(data):
    values = pd.DataFrame(data)  # Convertendo o dicionário de volta para um DataFrame
    # Criando um gráfico com Plotly Express
    fig = px.bar(values, x='MESES', y='ALCANCE GERAL', color_discrete_sequence=['#01D8B6'])
    fig.update_layout(
        plot_bgcolor= "#000000",
        paper_bgcolor = "#000000",
        legend=dict(font=dict(color="white")),
        font=dict(color="white")
    )

    return fig

@callback(
    Output('grafico_engajamento_instagram', 'figure'),
    Input('data-store3', 'data')
)
def update_graph(data):
    values = pd.DataFrame(data)  # Convertendo o dicionário de volta para um DataFrame    
    values_sorted = values.sort_values(by='MESES')       # Criando um gráfico com Plotly Express
    fig = px.line(values_sorted, x='MESES', y='ENGAJAMENTO GERAL', color_discrete_sequence=['#01D8B6'])
    fig.update_layout(
        plot_bgcolor= "#000000",
        paper_bgcolor = "#000000",
          legend=dict(font=dict(color="white")),
        font=dict(color="white")
    )
    return fig

# Layout do dashboard
layout = html.Div([
    html.H1("Instagram",style={"text-align":"center","color": "white", "background-color":"#000000", "border-radius": "20px", "overflow": "hidden"}),
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
                            dcc.Graph(id="grafico_seguidores_instagram", style={'width': '600px', 'height': '400px', "border-radius": "20px", "overflow": "hidden", "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.2)"})],
                        style={"background-color": "black", "border-radius": "20px", "overflow": "hidden"}
                    ),
                    html.Div(
                        children=[
                            html.H3("Engajamento", style={"color": "white",  "text-align":"center"}),
                            dcc.Graph(id='grafico_engajamento_instagram', style={'width': '600px', 'height': '400px', "border-radius": "20px", "overflow": "hidden"})],
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
                            dcc.Graph(id='grafico_alcance_instagram', style={'width': '600px', 'height': '400px'})],
                            style={"background-color": "black", "border-radius": "20px", "overflow": "hidden"}
                    ),
                ]
            ),
        ]
    ),
    html.Div([
    ], className='row'),
    dcc.Store(id='data-store1'),
    dcc.Store(id='data-store2'),
    dcc.Store(id='data-store3'),
])
