import dash
from dash import dcc, html, Dash
import plotly.express as px
from threading import Thread
import sys
import webview
import os

from components.sidebar import sidebar

# Inicialize a aplicação Dash
app = dash.Dash(__name__)

DASH_TITLE = "Dashboard"

bootstrap_css = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
global_styles = os.path.join("dashboard/assets/styles", "styles.css")

px.defaults.template = "ggplot2"

app = Dash(
    __name__, 
    pages_folder="pages", 
    use_pages=True, 
    external_stylesheets=[bootstrap_css], 
    title=DASH_TITLE,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ]
)

#Layout do Dashboard
app.layout = html.Div(
    [
        dcc.Location(id="url", pathname="/instagram"), 

        sidebar(), 

        dash.page_container
    ],
    className="my_app",
    style={
        "width": "100vw",
        "height": "100vh",
        "display": "flex",
        "flexDirection": "row",
    },
)



if __name__ == '__main__':

    if True:
        # if sys.argv[1] == 'debug':
        app.run_server(debug=True)
    else:
        def run_app():
            app.run_server(debug=False)

        t = Thread(target=run_app)
        t.daemon = True
        t.start()


        window = webview.create_window(
            DASH_TITLE, 
            "http://127.0.0.1:8050/",
            maximized=True,
            zoomable=True
        )

        webview.start(
            debug=False,
        )