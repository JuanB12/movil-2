from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.usuario import Usuario, UsuarioSchema

# from models.pasajero import Pasajero, PasajeroSchema

ruta_usuario = Blueprint("ruta_usuario", __name__)

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)


@ruta_usuario.route("/usuario", methods=["GET"])
def formulario():
    notificaciones = Usuario.query.all()  # Select * from Pasajeros
    resultado_notificaciones = usuarios_schema.dump(notificaciones)
    return jsonify(resultado_notificaciones)


@ruta_usuario.route("/save_usuario", methods=["POST"])
def save():
    # id = request.json["id"]
    nombre = request.json["nombre"]
    apellido = request.json["apellido"]
    passs = request.json["contraseña"]
    genero = request.json["genero"]
    cel = request.json["telefono"]
    correo = request.json["correo_electronico"]

    new_notificaciones = Usuario(
        nombre,
        apellido,
        passs,
        genero,
        cel,
        correo,
    )

    db.session.add(new_notificaciones)
    db.session.commit()
    return "Datos guardados con éxito"


@ruta_usuario.route("/update_usuario", methods=["PUT"])
def Update():
    id = request.json["id"]
    nombre = request.json["nombre"]
    apellido = request.json["apellido"]
    passs = request.json["contraseña"]
    genero = request.json["genero"]
    cel = request.json["telefono"]
    correo = request.json["correo_electronico"]

    ejercicio = Usuario.query.get(id)
    if ejercicio:
        print(ejercicio)
        ejercicio.nombre = nombre
        ejercicio.apellido = apellido
        ejercicio.contraseña = passs
        ejercicio.genero = genero
        ejercicio.telefono = cel
        ejercicio.correo_electronico = correo

        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"


@ruta_usuario.route("/delete_usuario/<id>", methods=["DELETE"])
def eliminar(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify(
        usuario_schema.dump(usuario),
    )

