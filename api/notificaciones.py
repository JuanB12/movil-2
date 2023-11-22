from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.notificaciones import Notificaciones, NotificacionesSchema

ruta_notificaciones = Blueprint("ruta_notificaciones", __name__)

notificacion_schema = NotificacionesSchema()
notificaciones_schema = NotificacionesSchema(many=True)


@ruta_notificaciones.route("/notificaciones", methods=["GET"])
def formulario():
    notificaciones = Notificaciones.query.all()  # Select * from Pasajeros
    resultado_notificaciones = notificaciones_schema.dump(notificaciones)
    return jsonify(resultado_notificaciones)


@ruta_notificaciones.route("/save_notificaciones", methods=["POST"])
def save():
    # id = request.json["id"]
    msj = request.json["mensaje"]
    fcEn = request.json["fecha_envio"]
    fcCr = request.json["fecha_creacion"]
    fcVi = request.json["fecha_view"]
    fk_us = request.json["fk_usuario"]

    new_notificaciones = Notificaciones(
        msj,
        fcEn,
        fcCr,
        fcVi,
        fk_us,
    )

    db.session.add(new_notificaciones)
    db.session.commit()
    return "Datos guardados con éxito"


@ruta_notificaciones.route("/update_notificaciones", methods=["PUT"])
def Update():
    id = request.json["id"]
    msj = request.json["mensaje"]
    fcEn = request.json["fecha_envio"]
    fcCr = request.json["fecha_creacion"]
    fcVi = request.json["fecha_view"]
    fk_us = request.json["fk_usuario"]

    ejercicio = Notificaciones.query.get(id)
    if ejercicio:
        print(ejercicio)
        ejercicio.mensaje = msj
        ejercicio.fecha_envio = fcEn
        ejercicio.fecha_creacion = fcCr
        ejercicio.fecha_view = fcVi
        ejercicio.fk_usuario = fk_us

        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"


@ruta_notificaciones.route("/delete_notificaciones/<id>", methods=["DELETE"])
def eliminar(id):
    usuario = Notificaciones.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify(
        notificacion_schema.dump(usuario),
    )
