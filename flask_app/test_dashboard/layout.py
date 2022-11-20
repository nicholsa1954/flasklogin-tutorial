# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 07:15:48 2022

@author: nicho
"""
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from flask import request

from dash import dash_table
from dash import dcc
from dash import html

import pandas as pd
import time
import os

from .html_layout import html_layout

def setup_layout(app):
    
    # Custom HTML layout
    app.index_string = html_layout
    
    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])
    

    index_page = html.Div([
        html.H3('Lets go!'),
        html.Div( children = [ html.H3('Hello World ') ], id = 'index-content' ),
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
    
    @app.callback(Output('index-content', 'children'), 
                  Input('url', 'pathname'))
    def index_content(pathname):
        f'You have selected path {pathname}'
    
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



### Docs on "Location": https://dash.plotly.com/dash-core-components/location
### More on templates: http://exploreflask.com/en/latest/templates.html
import urllib
from urllib.parse import *
from flask import request, session
def setup_layout2(app):
    
    # Custom HTML layout
    app.index_string = html_layout
    
    app.layout = html.Div([
            dcc.Location(id='url', refresh=False),
            html.Div(id='description')
        ])

    # @app.callback(Output('description', 'children'),
    #               [Input('url', 'pathname'),  
    #                Input('url', 'searchdata')])
    
    @app.callback(Output('description', 'children'),
                  [Input('url', 'pathname')])    
    def display_page(pathname):
        # parse_url = urllib.parse.urlparse(pathname)
        foo, bar = pathname.split('/')
        
        my_string = 'Inputs: pathname {pathname}' \
                    .format(pathname = type(pathname))
        return html.Div([
            html.H1(my_string)
        ])