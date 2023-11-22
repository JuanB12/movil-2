from config.db import db, ma, app


class Ejercicio(db.Model):
    __tablename__ = "tbl_ejercicio"

    id = db.Column(db.Integer, primary_key=True)
    nombre_ejercicio = db.Column(db.String(100))
    descripcion_ejercicio = db.Column(db.String(200))
    repeticiones = db.Column(db.Integer())
    fk_rutinaEj = db.Column(db.Integer, db.ForeignKey("tbl_rutinaEjercicio.id"))

    def __init__(
        self,
        nombre_ejercicio,
        descripcion_ejercicio,
        repeticiones,
        fk_rutinaEj,
    ):
        self.nombre_ejercicio = nombre_ejercicio
        self.descripcion_ejercicio = descripcion_ejercicio
        self.repeticiones = repeticiones
        self.fk_rutinaEj = fk_rutinaEj


with app.app_context():
    db.create_all()


class EjercicioSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "nombre_ejercicio",
            "descripcion_ejercicio",
            "repeticiones",
            "fk_rutinaEj",
        )
