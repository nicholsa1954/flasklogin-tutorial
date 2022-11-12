"""Initialize app."""
from flask import Flask
from flask import flash, redirect,  url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

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
        from .dashboard import init_dashboard

        app = init_dashboard(app)        

        # Compile static assets
        if True:
            compile_static_assets(app)

        return app
