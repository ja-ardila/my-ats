from .db import db

class Autorizador(db.Model):
    __tablename__= 'autorizador'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    cedula = db.Column(db.String, nullable=False)
    cargo = db.Column(db.String)
    firma = db.Column(db.String)
    id_ats = db.Column(db.Integer, db.ForeignKey('id.ats'))

    ats = db.relationship("ATS", backref="autorizadores")