from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from flask import request

from dash import dash_table
from dash import dcc
from dash import html


### Docs on "Location": https://dash.plotly.com/dash-core-components/location
### More on templates: http://exploreflask.com/en/latest/templates.html
import urllib
from urllib.parse import urlparse, parse_qs, parse_qsl

import pandas as pd
import sqlite3

from .html_layout import html_layout

credentials = ['OWNER', 'ADMIN', 'STAFF']
query = """ SELECT * FROM 'flasklogin-users' """


# Load DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv')

def test_user_in_db(user_name):
    try:
        conn = sqlite3.connect('./app2.db')
    except: 
        return 'BARFED!'
    df = pd.read_sql_query( query , conn)
    row = df.loc[df['name'] == user_name]
    if not row.empty:
        return row['credential'].values[0]
    else: 
        print(f'user {user_name} not found')
        return 'NONE'

def setup_layout(app):
    # Custom HTML layout
    app.index_string = html_layout
    
    # Create Layout
    app.layout = html.Div(
        children=[
            dcc.Location(id='url', refresh=False),
            html.H1('Stock Tickers'),
            html.Div(id='description'),
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
    
    return app


def setup_callbacks(app):
    ### http://127.0.0.1:5005/testdashapp/user?name=foo
    ### Parsed: ParseResult(scheme='http', netloc='127.0.0.1:5005', path='/testdashapp/user', params='', query='name=foo', fragment='')
    
    @app.callback(Output('description', 'children'),
                  [Input('url', 'href'), Input('url', 'pathname'), Input('url', 'search')])    
    def display_page(href, pathname, search):

        parsed = urlparse(href)   
        parsed_dict = parse_qs(parsed.query)        
        user_name = parsed_dict['name'][0]
        
        credential = test_user_in_db(user_name)
        if credential in credentials:  
            my_string = f'User: {user_name} -- credential: {credential}'
            return html.H3(my_string)
        else:
            return html.H3(f'Failed finding credential for {user_name}')    
    
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
