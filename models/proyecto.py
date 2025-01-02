from models import db
from models.usuarios_proyectos import tabla_usuarios_proyectos

class Proyecto(db.Model):
    __tablename__ = 'proyecto'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String, nullable=False)

    # Relación con contratista
    contratista_id = db.Column(db.String, db.ForeignKey('contratista.id'), nullable=False)
    contratista = db.relationship("Contratista", back_populates="proyectos_contratista")

    # Relación con contratante
    contratante_id = db.Column(db.String, db.ForeignKey('contratante.id'), nullable=False)
    contratante = db.relationship("Contratante", back_populates="proyectos_contratante")

    # Relación con usuario administrador
    admin_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
    admin = db.relationship("User", back_populates="proyectos_administrados")

    # Relación inversa para acceder a los usuarios vinculados a un proyecto
    usuarios = db.relationship("User", secondary=tabla_usuarios_proyectos, back_populates="proyectos")