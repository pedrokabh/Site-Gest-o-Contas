# ROTAS
#
# ESTUDAR escape() para fazer jinja ler comando inseridos na url como texto, para segurança do site.
# from markupsafe import escape
# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"
#

from flask import Blueprint

login = Blueprint('login',__name__)

@login.route('/')
def index():
    return "Hello Login!!"