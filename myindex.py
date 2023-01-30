from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# import from folders
from app import *
from components import sidebar, dashboards, extratos, atual, geral

# =========  Layout  =========== #
content = html.Div(id="page-content")

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id="url"),
            sidebar.layout
        ], md=2),
# ], md=2, style={'background-color':  'red',  'height':'1080px'}),
        dbc.Col([
            html.Div(id="page-content")
        ], md=10),
# ], md=10, style={'background-color':  'blue',  'height':'1080px'}),
    ])
], fluid=True, style={"padding": "0px"}, className="dbc")

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/" or pathname == "/dashboards":
        return dashboards.layout

    if pathname == "/extratos":
        return extratos.layout
    
    if pathname == "/atual":
        return atual.layout
    
    if pathname == "/geral":
        return geral.layout
        
if __name__ == '__main__':
    app.run_server(port=8082, debug=True)