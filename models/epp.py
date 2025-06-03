from .db import db

class EPP(db.Model):
    __tablename__= 'EPP'
    id = db.Column(db.Integer, primary_Key=True)
    nombre = db.Column(db.String, nullable=False)
    cantidad = db.Column(db.Integer)
    estado = db.Column(db.String)
    id_pt = db.Column(db.Integer, db.ForeignKey('pt.id'))

    pt = db.relationship("PT", backref="epps")