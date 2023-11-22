from flask import Flask, jsonify, json
from config.db import db, ma, app

# ----------------------------------------------------------------

from api.usuario import Usuario, ruta_usuario
from api.ejercicio import Ejercicio, ruta_ejercicio
from api.rutina_ejercicio import RutinaEjercicio, ruta_rutina_ejercicio
from api.notificaciones import Notificaciones, ruta_notificaciones
from api.ejercicio_favorito import EjercicioFavorito, ruta_ejercicio_favorito
from api.historial_ejercicios import HistorialEjercicios, ruta_HistorialEjercicios

# ----------------------------------------------------------------

app.register_blueprint(ruta_ejercicio_favorito, url_prefix="/parcial")
app.register_blueprint(ruta_ejercicio, url_prefix="/parcial")
app.register_blueprint(ruta_HistorialEjercicios, url_prefix="/parcial")
app.register_blueprint(ruta_notificaciones, url_prefix="/parcial")
app.register_blueprint(ruta_rutina_ejercicio, url_prefix="/parcial")
app.register_blueprint(ruta_usuario, url_prefix="/parcial")

# ----------------------------------------------------------------


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
