from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from flask import request

from dash import dash_table
from dash import dcc
from dash import html

from .data import create_dataframe
from .html_layout import html_layout

df = create_dataframe()

def GetTable(heading, id, style):
    card = dbc.Card(
        children=[
            dbc.CardBody(children=[
                html.H5(heading, className="card-title",style=style),                            
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

    @app.callback(
        Output('table-users', 'children'),
        Input('none2', 'children')
    )
    def update_table(none):
        return UpdateTable(df)
    