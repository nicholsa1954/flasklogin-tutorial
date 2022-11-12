from flask import Blueprint

errors_bp = Blueprint(
    "errors_bp", __name__, template_folder="templates", static_folder="static"
)

from . import handlers
