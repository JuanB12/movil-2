from config.db import db, ma, app


class RutinaEjercicio(db.Model):
    __tablename__ = "tbl_rutinaEjercicio"

    id = db.Column(db.Integer, primary_key=True)
    nombre_rutina = db.Column(db.String(100))
    descripcion_rutina = db.Column(db.String(200))
    fk_usuario = db.Column(db.Integer, db.ForeignKey("tbl_usuario.id"))

    def __init__(
        self,
        nombre_rutina,
        descripcion_rutina,
        fk_usuario,
    ):
        self.nombre_rutina = nombre_rutina
        self.descripcion_rutina = descripcion_rutina
        self.fk_usuario = fk_usuario


with app.app_context():
    db.create_all()


class RutinaEjercicioSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "nombre_rutina",
            "descripcion_rutina",
            "fk_usuario",
        )
