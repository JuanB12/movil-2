from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.historial_ejercicios import HistorialEjercicios, HistorialEjercicioSchema

ruta_HistorialEjercicios = Blueprint("ruta_historial_ejercicio", __name__)

historial_ejercicio_schema = HistorialEjercicioSchema()
historial_ejercicios_schema = HistorialEjercicioSchema(many=True)


@ruta_HistorialEjercicios.route("/historial_ejercicio", methods=["GET"])
def formulario():
    historial = HistorialEjercicios.query.all()  # Select * from Pasajeros
    resultado_historial = historial_ejercicios_schema.dump(historial)
    return jsonify(resultado_historial)


@ruta_HistorialEjercicios.route("/save_historial_ejercicio", methods=["POST"])
def save():
    # id = request.json["id"]
    nombre = request.json["fecha_ejercico"]
    rept = request.json["repeticiones"]
    caloriasQ = request.json["calorias_quemadas"]
    dur = request.json["duracion"]
    fk_ej = request.json["fk_ejercicio"]

    new_ejercicio = HistorialEjercicios(
        nombre,
        rept,
        caloriasQ,
        dur,
        fk_ej,
    )

    db.session.add(new_ejercicio)
    db.session.commit()
    return "Datos guardados con éxito"


@ruta_HistorialEjercicios.route("/update_historial_ejercicio", methods=["PUT"])
def Update():
    id = request.json["id"]
    nombre = request.json["fecha_ejercico"]
    rept = request.json["repeticiones"]
    caloriasQ = request.json["calorias_quemadas"]
    dur = request.json["duracion"]
    fk_ej = request.json["fk_ejercicio"]

    ejercicio = HistorialEjercicios.query.get(id)
    if ejercicio:
        print(ejercicio)
        ejercicio.fecha_ejercico = nombre
        ejercicio.repeticiones = rept
        ejercicio.calorias_quemadas = caloriasQ
        ejercicio.duracion = dur
        ejercicio.fk_ejercicio = fk_ej

        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"


@ruta_HistorialEjercicios.route("/delete_historial_ejercicio/<id>", methods=["DELETE"])
def eliminar(id):
    ejercicio = HistorialEjercicios.query.get(id)
    db.session.delete(ejercicio)
    db.session.commit()
    return jsonify(
        HistorialEjercicioSchema.dump(HistorialEjercicioSchema),
    )
