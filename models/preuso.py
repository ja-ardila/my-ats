from .db import db

class Preuso(db.Model):
    __tablename__ = 'preuso'
    id = db.Column(db.Integer,primary_key=True)
    id_ats = db.Column(db.Integer, db.ForeignKey('ats.id'))
    equipo = db.Column(db.String)
    marca = db.Column(db.String)
    serial = db.Column(db.String)
    estado = db.Column(db.String)
    observaciones = db.Column(db.String)
    fecha = db.Column(db.Date)
    firma_trabajador = db.Column(db.String)
    firma_autorizador =db.Column(db.String)

    ats = db.relationship("ATS",backref="preusos")
