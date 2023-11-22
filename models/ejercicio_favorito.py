from config.db import db, ma, app


class EjercicioFavorito(db.Model):
    __tablename__ = "tbl_EjercicioFavorito"

    id = db.Column(db.Integer, primary_key=True)
    fk_usuario = db.Column(db.Integer, db.ForeignKey("tbl_usuario.id"))
    fk_ejercicio = db.Column(db.Integer, db.ForeignKey("tbl_ejercicio.id"))

    def __init__(
        self,
        fk_usuario,
        fk_ejercicio,
    ):
        self.fk_usuario = fk_usuario
        self.fk_ejercicio = fk_ejercicio


with app.app_context():
    db.create_all()


class EjercicioFavoritoSchema(ma.Schema):
    class Meta:
        fields = ("id", "fk_usuario", "fk_ejercicio0")
