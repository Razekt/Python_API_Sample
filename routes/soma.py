import json
from flask import request
from . import routes

@routes.route('/soma', methods=["POST"])
def soma():
    if request.method == "POST":
        raw_data = json.loads(request.data)
        numero = raw_data['numero']
        segundo_numero = raw_data['segundo_numero']
        return str(numero + segundo_numero)