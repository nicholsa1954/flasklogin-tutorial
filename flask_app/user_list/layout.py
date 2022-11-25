from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from flask import request

from dash import dash_table
from dash import dcc
from dash import html

from .data import create_dataframe
from .html_layout import html_layout

import pandas as pd
import pytz

def GetTable(heading, id, style):
    card = dbc.Card(
        children=[
            dbc.CardBody(children=[
                html.H4(heading, className="card-title",style=style),                            
                dbc.Table(
                    children = [],
                    bordered=True,
                    dark=True,
                    hover=True,
                    responsive=True,
                    striped=True,
                    id=id
                )
            ], style=style)
        ] 
    )
    return card

def UpdateTable(df):
    assert not df.empty, "df is empty!"
    return dbc.Table.from_dataframe(df)


def setup_layout(app):
    # Custom HTML layout
    app.index_string = html_layout
    app.layout = dbc.Container([
        html.Br(),
    
        # dummy input to trigger update callbacks for static displays
        html.Div(id='none2', children=[], style={'display': 'none'}),
    
        dbc.Row(
            [   
                dbc.Col([
                    GetTable('Users:', 'table-users', style = {}),                    
                ], width={'size': 12}),
            ]),
    
    ],  fluid=True)
    
    return app

def setup_callbacks(app):
    @app.callback(
        Output('table-users', 'children'),
        Input('none2', 'children')
    )
    def update_table(none):
        df = create_dataframe()
        df['created_on'] = pd.to_datetime(df['created_on'], utc = True)
        df['last_login'] = pd.to_datetime(df['last_login'], utc = True)     
        df['created_on'] = df['created_on'].dt.tz_convert('US/Central').dt.strftime('%m-%d-%Y %I:%M:%S')
        df['last_login'] = df['last_login'].dt.tz_convert('US/Central').dt.strftime('%m-%d-%Y %I:%M:%S') 
        
        return UpdateTable(df)
    