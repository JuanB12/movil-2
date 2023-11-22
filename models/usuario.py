from config.db import db, ma, app


class Usuario(db.Model):
    __tablename__ = "tbl_usuario"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(100))
    contraseña = db.Column(db.String(100))
    genero = db.Column(db.String(100))
    telefono = db.Column(db.String(100))
    correo_electronico = db.Column(db.String(100))

    def __init__(
        self,
        nombre,
        apellido,
        contraseña,
        genero,
        telefono,
        correo_electronico,
    ):
        self.nombre = nombre
        self.apellido = apellido
        self.contraseña = contraseña
        self.genero = genero
        self.telefono = telefono
        self.correo_electronico = correo_electronico


with app.app_context():
    db.create_all()


class UsuarioSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "nombre",
            "apellido",
            "contraseña",
            "telefono",
            "correo_electronico",
        )
