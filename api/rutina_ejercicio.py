from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.rutina_ejercicio import RutinaEjercicio, RutinaEjercicioSchema

# from models.pasajero import Pasajero, PasajeroSchema

ruta_rutina_ejercicio = Blueprint("ruta_rutina_ejercicio", __name__)

ejercicio_fav = RutinaEjercicioSchema()
ejercicios_fav = RutinaEjercicioSchema(many=True)

@ruta_rutina_ejercicio.route("/rutina_ejercicio", methods=["GET"])
def formulario():
    notificaciones = RutinaEjercicio.query.all()  # Select * from Pasajeros
    resultado_notificaciones = ejercicios_fav.dump(notificaciones)
    return jsonify(resultado_notificaciones)


@ruta_rutina_ejercicio.route("/save_rutina_ejercicio", methods=["POST"])
def save():
    # id = request.json["id"]
    msj = request.json["nombre_rutina"]
    fcEn = request.json["descripcion_rutina"]
    fcCr = request.json["fk_usuario"]

    new_notificaciones = RutinaEjercicio(
        # id,
        msj,
        fcEn,
        fcCr,
    )

    db.session.add(new_notificaciones)
    db.session.commit()
    return "Datos guardados con éxito"


@ruta_rutina_ejercicio.route("/update_rutina_ejercicio", methods=["PUT"])
def Update():
    id = request.json["id"]
    msj = request.json["nombre_rutina"]
    fcEn = request.json["descripcion_rutina"]
    fcCr = request.json["fk_usuario"]

    ejercicio = RutinaEjercicio.query.get(id)
    if ejercicio:
        print(ejercicio)
        ejercicio.nombre_rutina = msj
        ejercicio.descripcion_rutina = fcEn
        ejercicio.fk_usuario = fcCr

        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_rutina_ejercicio.route("/delete_rutina_ejercicio/<id>", methods=["DELETE"])
def eliminar(id):
    usuario = RutinaEjercicio.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify(
        ejercicio_fav.dump(usuario),
    )
