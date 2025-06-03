from .db import db

class Firma(db.Model):
    __tablename__ = 'frima'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    cargo = db.Column(db.String)
    tipo = db.Column(db.String)
    firma_digital = db.Column(db.string)
    fecha = db.Column(db.Date)
    