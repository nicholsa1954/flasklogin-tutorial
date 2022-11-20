"""Application entry point."""
from flask_app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port = 5005, debug = True)


from flask_app import db
from flask_app.models import User

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}