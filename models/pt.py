from .db import db

class PT(db.Model):
    __tablename__ = 'pt'
    id = db.Column(db.Integer, primary_key=True)
    id_ats = db.Column(db.Integer, db.ForeignKey('ats.id'))
    fecha_creacion = db.Column(db.Date)
    valido_desde = db.Column(db.DateTime)
    valido_hasta = db.Column(db.DateTime)
    lugar_ejecucion = db.Column(db.String)
    tipo_trabajo = db.Column(db.String)  
    descripcion = db.Column(db.String)
    observaciones = db.Column(db.String)
    estado = db.Column(db.String, default="abierto")

    ats = db.relationship("ATS", backref="pts")