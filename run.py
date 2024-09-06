import os

from flask import jsonify
from flask_cors import CORS, cross_origin

from app import app

CORS(app)

__author__ = "Edson Burgos"
__version__ = "1"
__email__ = "edsonburgosmacedo@gmail.com"


@cross_origin()
def not_found():
    data = {
        'code': 404,
        'message': 'Servicio no encontrado'
    }
    return jsonify(data), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.register_error_handler(404, not_found)
    app.run(debug=True, host='backend.test', port=80)
