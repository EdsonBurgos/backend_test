from flask import jsonify
from flask_cors import CORS, cross_origin
from app.models.stackoverflow_model import *

from app import app
CORS(app)


### Obtener el número de respuestas contestadas y no contestadas
@cross_origin()
@app.route('/answers/answered_and_no', methods=['GET'])
def get_answers():
    data = {}
    try:
        data['code'] = 200
        data['response'] = answered_and_no()
    except Exception as ex:
        data['code'] = 200
        data['msg'] = str(ex)
    return jsonify(data)


### Obtener la respuesta con mayor reputación
@cross_origin()
@app.route('/answers/reputation/greater', methods=['GET'])
def higher_reputation_answer():
    data = {}
    try:
        data['code'] = 200
        data['response'] = greater_reputation()
    except Exception as ex:
        data['code'] = 200
        data['msg'] = str(ex)
    return jsonify(data)


### Obtener la respuesta con menor número de vistas
@cross_origin()
@app.route('/answers/views/less', methods=['GET'])
def fewer_views_answer():
    data = {}
    try:
        data['code'] = 200
        data['response'] = less_views()
    except Exception as ex:
        data['code'] = 200
        data['msg'] = str(ex)
    return jsonify(data)


### Obtener la respuesta más vieja y más actual
@cross_origin()
@app.route('/answers/old_and_recent', methods=['GET'])
def old_recent_answer():
    data = {}
    try:
        data['code'] = 200
        data['response'] = old_and_recent()
    except Exception as ex:
        data['code'] = 400
        data['msg'] = str(ex)
    return jsonify(data)


## Imprimir en consola del punto 2 al 5
@app.route('/answers/services', methods=['GET'])
def previous_answers_services():
    data = {}
    try:
        data['code'] = 200
        data['response'] = previous_services()
    except Exception as ex:
        data['code'] = 400
        data['msg'] = str(ex)
    return jsonify(data)
