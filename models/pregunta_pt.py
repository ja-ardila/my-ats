from .db import db

class Pregunta_PT  (db.Model):
        __tablename__ = 'pregunta_pt'
        id = db.Column(db.Integer,primary_key=True)
        pregunta = db.Column(db.String, nullable=False)
        respuesta = db.Column(db.String)
        id_pt = db.Column(db.Integer, db.ForeignKey('pt.id'))

        pt = db.relationship("PT", backref="preguntas")
        

