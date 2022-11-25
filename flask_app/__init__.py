"""Initialize app."""
import os
from flask import Flask
from flask import flash, redirect,  url_for, session
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
import logging
from logging.handlers import RotatingFileHandler
from werkzeug.debug import DebuggedApplication

db = SQLAlchemy()
login_manager = LoginManager()

from .models import User

def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)
    moment = Moment(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        """Check if user is logged-in upon page load."""
        if user_id is not None:
            return User.query.get(user_id)
        return None

    @login_manager.unauthorized_handler
    def unauthorized():
        """Redirect unauthorized users to Login page."""
        flash("You must be logged in to view that page.")
        return redirect(url_for("auth_bp.login"))

    with app.app_context():
        from .auth import auth_bp
        from .main import main_bp
        from .errors import errors_bp
        from .assets import compile_static_assets
 
        # Register Blueprints
        app.register_blueprint(auth_bp)
        app.register_blueprint(errors_bp)
        app.register_blueprint(main_bp)        

        # Create Database Models
        db.create_all()
        
        # Import Dash application
        from .dashboard import init_dashboard, init_callbacks
        # from .test_dashboard import init_dashboard
        dash_app1, app = init_dashboard(app)
        init_callbacks(dash_app1)
        
        from .user_list import init_userlist, init_callbacks
        dash_app2, app = init_userlist(app)
        init_callbacks(dash_app2)

        # Compile static assets
        if True:
            compile_static_assets(app)
            
        if app.debug:
            app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)
            
        if not app.debug and not app.testing:
            if not os.path.exists('logs'):
                    os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/flask_app.log', maxBytes=10240,
                                               backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)
        
            app.logger.setLevel(logging.INFO)
            app.logger.info('Flask_app startup')           
            
        @app.route("/", methods=["GET"])
        def dashboard():
            """Logged-in User Dashboard."""
            dashboard_id = 2002
            session['dashboard_id'] = dashboard_id
            return redirect('/testdashapp/')
        
        @app.route("/", methods=["GET"])
        def userlist():
            """Logged-in User list."""
            list_id = 2005
            session['list_id'] = list_id
            return redirect('/usertable/')
 
            
        return app
