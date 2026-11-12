from flask import Blueprint

main = Blueprint('main', __name__)
# creates the blueprint for the main page

from app.main import routes

