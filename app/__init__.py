from flask import Flask
from app.extensions import db, login_manager

def create_app():
    """Creates a configured app,
        can be used to test the application"""
    app = Flask(__name__)

    db.init_app(app)
    login_manager.init_app(app)

    from app.main import main #Inside function so python does not load it accidentally
    app.register_blueprint(main)

    return app