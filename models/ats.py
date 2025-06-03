from .db import db

class ATS(db.Model):
    __tablename__ = 'ats'
    id = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.String)  
    ciudad = db.Column(db.String)
    area_proceso = db.Column(db.String)
    ubicacion = db.Column(db.String)
    fecha = db.Column(db.Date)
    lugar = db.Column(db.String)
    hora = db.Column(db.Time)
    estado_cerrado = db.Column(db.Boolean, default=False)
    id_proyecto = db.Column(db.Integer)