from flask import Blueprint
views = Blueprint('views', __name__)
@views.route('/')
def Home():
    return "<h1>Ahmed Sayed Elansary</h1>"