"""Instantiate a Dash app."""
import dash
from dash.dependencies import Input, Output
from dash import dash_table
from dash import dcc
from dash import html

from urllib.parse import urlparse,urlsplit,parse_qs
import sqlite3

import pandas as pd
import time
import os

from .layout import html_layout

### For explanation of "routes_pathname_prefix" see 
### https://community.plotly.com/t/host-dash-under-alternate-path/21237
### and the Plotly documentation: https://dash.plotly.com/reference.
### The prefix shows up again in the .jinga2 files.

def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    app = dash.Dash(
        server=server,
        routes_pathname_prefix="/testdashapp/",
        external_stylesheets=[
            "/static/dist/css/styles.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )
    
    # Custom HTML layout
    app.index_string = html_layout
    

    # Load DataFrame
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv')

    # Create Layout
    app.layout = html.Div(
        children=[
            html.H1('Stock Tickers'),
            dcc.Dropdown(
                id='my-dropdown',
                options=[
                    {'label': 'Tesla', 'value': 'TSLA'},
                    {'label': 'Apple', 'value': 'AAPL'},
                    {'label': 'Coke', 'value': 'COKE'}
                ],
                value='TSLA'
            ),
            dcc.Graph(id='my-graph')
        ],
        id="dash-container",
    )


    @app.callback(Output('my-graph', 'figure'),
                  [Input('my-dropdown', 'value')])
    def update_graph(selected_dropdown_value):
        dff = df[df['Stock'] == selected_dropdown_value]
        return {
            'data': [{
                'x': dff.Date,
                'y': dff.Close,
                'line': {
                    'width': 3,
                    'shape': 'spline'
                }
            }],
            'layout': {
                'margin': {
                    'l': 30,
                    'r': 20,
                    'b': 30,
                    't': 20
                }
            }
        }

    return app.server