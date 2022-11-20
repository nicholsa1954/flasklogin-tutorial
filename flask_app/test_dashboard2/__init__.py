import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from dash import dash_table
from dash import dcc
from dash import html

import pandas as pd
import time
import os

from .html import html_layout

def setup_layout(app):
    
    # Custom HTML layout
    app.index_string = html_layout
    
    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])
    

    index_page = html.Div([
        html.H3('Lets go!'),
        dcc.Link('Go to Page 1', href='/page-1'),
        html.Br(),
        dcc.Link('Go to Page 2', href='/page-2')
    ])
    
    page_1_layout = html.Div([
        html.H3('Page 1'),
        dcc.Dropdown(['LA', 'NYC', 'MTL'], 'LA', id='page-1-dropdown'),
        html.Div(id='page-1-content'),
        html.Br(),
        dcc.Link('Go to Page 2', href='/page-2/bar'),
        html.Br(),
        dcc.Link('Go back to home', href='/'),
    ])
    
    @app.callback(Output('page-1-content', 'children'),
                  [Input('page-1-dropdown', 'value'), Input('url', 'pathname')])
    def page_1_dropdown(value, pathname):
        return f'You have selected {value} and path {pathname}'
    
    
    page_2_layout = html.Div([
        html.H3('Page 2'),
        dcc.RadioItems(['Orange', 'Blue', 'Red'], 'Orange', id='page-2-radios'),
        html.Div(id='page-2-content'),
        html.Br(),
        dcc.Link('Go to Page 1', href='/page-1/foo'),
        html.Br(),
        dcc.Link('Go back to home', href='/')
    ])
    
    @app.callback(Output('page-2-content', 'children'),
                  [Input('page-2-radios', 'value'), Input('url', 'pathname')])
    def page_2_radios(value, pathname):
        return f'You have selected {value} and path {pathname}'
    
    
    # Update the index
    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_page(pathname):
        if '/page-1' in pathname:
            return page_1_layout
        elif '/page-2' in pathname:
            return page_2_layout
        else:
            return index_page
        # You could also return a 404 "URL not found" page here    
    

def init_dashboard(server = None):

    external_stylesheets=[
        "/static/dist/css/styles.css",
        "https://fonts.googleapis.com/css?family=Lato",
    ]
    
    # external_stylesheets=[dbc.themes.SLATE]
   
    if server:     
        """Create a Plotly Dash dashboard piggybacked on a Flask server.""" 
        app = dash.Dash(
            __name__,
            server=server,
            routes_pathname_prefix="/testdashapp/",
            external_stylesheets=external_stylesheets
        )
        setup_layout(app)
        return app.server
            
     
    else:
        """Create a 'bare' Plotly Dash dashboard with its own server.""" 
        app = dash.Dash(
            __name__, 
            external_stylesheets=external_stylesheets,
            suppress_callback_exceptions = True,               
            meta_tags = [{'name':'viewport', 
                          'content':'width = device_width, initial-scale = 1.0, \
                          maximum-scale = 1.2, minimum-scale = 0.5'}]
            
            ) 
    
        server = app.server
        setup_layout(app)    
        return app
    
    
