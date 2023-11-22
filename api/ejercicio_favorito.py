from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.ejercicio_favorito import EjercicioFavorito, EjercicioFavoritoSchema

# from models.pasajero import Pasajero, PasajeroSchema

ruta_ejercicio_favorito = Blueprint("ruta_ejercicio_favorito", __name__)

ejercicio_fav = EjercicioFavoritoSchema()
ejercicios_fav = EjercicioFavoritoSchema(many=True)


@ruta_ejercicio_favorito.route("/ejerciciof", methods=["GET"])
def formulario():
    resultall = EjercicioFavorito.query.all()  # Select * from Pasajeros
    resultado_ejerciciof = ejercicios_fav.dump(resultall)
    return jsonify(resultado_ejerciciof)


@ruta_ejercicio_favorito.route("/save_ejerciciof", methods=["POST"])
def save():
    # id = request.json["id"]
    fkUsuario = request.json["fk_usuario"]
    fjEjercicio = request.json["fk_ejercicio"]

    new_ejercicioF = EjercicioFavorito(
        fkUsuario,
        fjEjercicio,
    )

    db.session.add(new_ejercicioF)
    db.session.commit()
    return "Datos guardados con éxito"


@ruta_ejercicio_favorito.route("/delete_ejerciciof/<id>", methods=["DELETE"])
def eliminar(id):
    ejercicioF = EjercicioFavorito.query.get(id)
    db.session.delete(ejercicioF)
    db.session.commit()
    return jsonify(
        EjercicioFavoritoSchema.dump(EjercicioFavoritoSchema),
    )
