from config.db import db, ma, app


class HistorialEjercicios(db.Model):
    __tablename__ = "tbl_historialEjercicio"

    id = db.Column(db.Integer, primary_key=True)
    fecha_ejercico = db.Column(db.String(255))
    repeticiones = db.Column(db.String(10))
    calorias_quemadas = db.Column(db.String(250))
    duracion = db.Column(db.String(255))
    fk_ejercicio = db.Column(db.Integer, db.ForeignKey("tbl_ejercicio.id"))

    def __init__(
        self,
        fecha_ejercicio,
        repeticiones,
        calorias_quemadas,
        duracion,
        fk_ejercicio,
    ):
        self.fecha_ejercico = fecha_ejercicio
        self.repeticiones = repeticiones
        self.calorias_quemadas = calorias_quemadas
        self.duracion = duracion
        self.fk_ejercicio = fk_ejercicio


with app.app_context():
    db.create_all()


class HistorialEjercicioSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "fecha_ejercicio",
            "repeticiones",
            "calorias_quemadas",
            "duracion",
            "fk_ejercicio",
        )
