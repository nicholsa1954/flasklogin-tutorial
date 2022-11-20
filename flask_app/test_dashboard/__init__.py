import dash

from .layout import setup_layout, setup_layout2

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
        setup_layout2(app)
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
        setup_layout2(app)    
        return app
    
    
