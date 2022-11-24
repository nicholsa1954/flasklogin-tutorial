import dash
from .layout import setup_layout

external_stylesheets=[
    "/static/dist/css/styles.css",
    "https://fonts.googleapis.com/css?family=Lato",
]

### For explanation of "routes_pathname_prefix" see 
### https://community.plotly.com/t/host-dash-under-alternate-path/21237
### and the Plotly documentation: https://dash.plotly.com/reference.
### The prefix shows up again in the .jinga2 files.

def init_userlist(server):
    """Create a user table."""
    app = dash.Dash(
        server=server,
        routes_pathname_prefix="/usertable/",
        external_stylesheets=external_stylesheets
    )
    
    setup_layout(app)
    return app.server