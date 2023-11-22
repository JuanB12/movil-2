from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.ejercicio import Ejercicio, EjercicioSchema

ruta_ejercicio = Blueprint("ruta_ejercicio", __name__)

ejercico_schema = EjercicioSchema()
ejercicios_schema = EjercicioSchema(many=True)


@ruta_ejercicio.route("/ejercicio", methods=["GET"])
def formulario():
    resultall = Ejercicio.query.all()  # Select * from Pasajeros
    resultado_ejerciciof = ejercicios_schema.dump(resultall)
    return jsonify(resultado_ejerciciof)


@ruta_ejercicio.route("/save_ejercicio", methods=["POST"])
def save():
    # id = request.json["id"]
    nombre = request.json["nombre_ejercicio"]
    descripcion = request.json["descripcion_ejercicio"]
    rep = request.json["repeticiones"]
    fk_rutina = request.json["fk_rutinaEj"]

    new_ejercicio = Ejercicio(nombre, descripcion, rep, fk_rutina)

    db.session.add(new_ejercicio)
    db.session.commit()
    return "Datos guardados con éxito"


@ruta_ejercicio.route("/update_ejercicio", methods=["PUT"])
def Update():
    id = request.json["id"]
    nombre = request.json["nombre_ejercicio"]
    descripcion = request.json["descripcion_ejercicio"]
    rep = request.json["repeticiones"]
    fk_rutina = request.json["fk_rutinaEj"]

    ejercicio = Ejercicio.query.get(id)
    if ejercicio:
        print(ejercicio)
        ejercicio.nombre_ejercicio = nombre
        ejercicio.descipcion_ejercicio = descripcion
        ejercicio.repeticiones = rep
        ejercicio.fk_rutinaEj = fk_rutina

        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"


@ruta_ejercicio.route("/delete_ejercicio/<id>", methods=["DELETE"])
def eliminar(id):
    pago = Ejercicio.query.get(id)
    db.session.delete(pago)
    db.session.commit()
    return jsonify(
        ejercico_schema.dump(pago),
    )
