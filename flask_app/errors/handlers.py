from flask import render_template, request
from flask_app import db
from . import errors_bp

@errors_bp.app_errorhandler(401)
def unauthorized_error(error):
    path = request.full_path
    return render_template('401.jinja2', path=path), 401

@errors_bp.app_errorhandler(403)
def forbidden_error(error):
    path = request.full_path
    return render_template('403.jinja2', path=path), 403

@errors_bp.app_errorhandler(404)
def not_found_error(error):
    path = request.full_path
    return render_template('404.jinja2', path=path), 404

@errors_bp.app_errorhandler(405)
def method_not_allowed_error(error):
    path = request.full_path
    return render_template('405.jinja2', path=path), 405

@errors_bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.jinja2'), 500

@errors_bp.app_errorhandler(Exception)
def handle_exception(error):
    path = request.path 
    return render_template('exception.jinja2', path=path)
