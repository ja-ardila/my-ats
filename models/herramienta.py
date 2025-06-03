from db import db

class Herramienta(db.Model):
    __tablename__= 'herramienta'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    estado = db.Column(db.String)
    cantidad = db.Column(db.Integer)
    observaciones = db.Column(db.String)
    id_pt = db.Column(db.Integer, db.ForeignKey('pt.id'))

    pt = db.relationship("PT", backref="herramientas")
    

