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

from .layout import setup_layout

external_stylesheets=[
    "/static/dist/css/styles.css",
    "https://fonts.googleapis.com/css?family=Lato",
]

### For explanation of "routes_pathname_prefix" see 
### https://community.plotly.com/t/host-dash-under-alternate-path/21237
### and the Plotly documentation: https://dash.plotly.com/reference.
### The prefix shows up again in the .jinga2 files.

def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    app = dash.Dash(
        server=server,
        routes_pathname_prefix="/testdashapp/",
        external_stylesheets=external_stylesheets
    )
    
    setup_layout(app)
    return app.server