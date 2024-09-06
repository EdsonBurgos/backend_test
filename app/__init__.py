from flask import Flask, jsonify
from flask_mysqldb import MySQL
from app.config.database import dbconfig

app = Flask(__name__)
app.config['MYSQL_HOST'] = dbconfig['host']
app.config['MYSQL_USER'] = dbconfig['username']
app.config['MYSQL_PASSWORD'] = dbconfig['password']
app.config['MYSQL_DB'] = dbconfig['database']

conn = MySQL(app)


@app.route("/")
def index():
    data = {
        "Services": {
            "API": {
                1: "Obtener el número de respuestas contestadas y no contestadas",
                2: "Obtener la respuesta con mayor reputación",
                3: "Obtener la respuesta con menor número de vistas",
                4: "Obtener la respuesta más vieja y más actual",
                5: "Imprimir en consola del punto 2 al 5",
            },
            "DB": {
                1: " ¿Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año?",
                2: "¿Cuál es el nombre aerolínea que ha realizado mayor número de vuelos durante el año?",
                3: "¿En qué día se han tenido mayor número de vuelos?",
                4: "¿Cuáles son las aerolíneas que tienen mas de 2 vuelos por día?",
            },
        }
    }
    return jsonify(data)


try:
    from app.controllers import *
except Exception as e:
    print(e)
