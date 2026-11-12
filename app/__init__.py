from flask import Flask

def create_app():
    """Creates a configured app,
        can be used to test the application"""
    app = Flask(__name__)

    from app.main import main #Inside function so python does not load it accidentally
    app.register_blueprint(main)

    return app