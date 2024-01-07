from flask import Blueprint

bp = Blueprint('question', __name__)

from app.api.questions import routes