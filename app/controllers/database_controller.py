from flask import jsonify
from app import app
from flask_cors import CORS, cross_origin
from app.models.airports_model import *
from app.models.flights_model import *

CORS(app)

@cross_origin()
@app.route('/airport/movements/max', methods=['GET'])
def airport_movements():
    data = {}
    try:
        data['code'] = 200
        data['response'] = airport_movements_max()
    except Exception as ex:
        data['code'] = 400
        data['msg'] = str(ex)
    return jsonify(data)


@cross_origin()
@app.route('/airlines/flights/max', methods=['GET'])
def flights_per_airline():
    data = {}
    try:
        data['code'] = 200
        data['response'] = flights_per_airline_max()
    except Exception as ex:
        data['code'] = 400
        data['msg'] = str(ex)
    return jsonify(data)


@cross_origin()
@app.route('/flights/days/max', methods=['GET'])
def flights_day():
    data = {}
    try:
        data['code'] = 200
        data['response'] = flights_day_max()
    except Exception as ex:
        data['code'] = 400
        data['msg'] = str(ex)
    return jsonify(data)


@cross_origin()
@app.route('/flights/days/greater/2', methods=['GET'])
def airlines_daily_flights():
    data = {}
    try:
        data['code'] = 200
        data['response'] = airline_day_flights()
    except Exception as ex:
        data['code'] = 400
        data['msg'] = str(ex)
    return jsonify(data)
