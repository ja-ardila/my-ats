from .db import db

class Trabajador(db.Model):
    __tablename__ ='trabajador'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    cedula = db.Column(db.String, nullable=False)
    cargo = db.Column(db.String)
    firma = db.Column(db.string)
    id_ats = db.Column(db.Integer, db.ForeignKey('ats.id')) 

    ats = db.relationship("ATS", backref="trabajadores")
