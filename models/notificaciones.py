from config.db import db, ma, app


class Notificaciones(db.Model):
    __tablename__ = "tbl_notificaciones"

    id = db.Column(db.Integer, primary_key=True)
    mensaje = db.Column(db.String(250))
    fecha_envio = db.Column(db.String(255))
    fecha_creacion = db.Column(db.String(255))
    fecha_view = db.Column(db.String(255))
    fk_usuario = db.Column(db.Integer, db.ForeignKey("tbl_usuario.id"))

    def __init__(
        self,
        mensaje,
        fecha_envio,
        fecha_creacion,
        fecha_view,
        fk_usuario,
    ):
        self.mensaje = mensaje
        self.fecha_envio = (fecha_envio,)
        self.fecha_creacion = fecha_creacion
        self.fecha_view = fecha_view
        self.fk_usuario = fk_usuario


with app.app_context():
    db.create_all()


class NotificacionesSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "mensaje",
            "fecha_envio",
            "fecha_creacion",
            "fecha_view",
            "fk_usuario",
        )
