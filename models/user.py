from models import db
from models.usuarios_proyectos import tabla_usuarios_proyectos
import enum

class tipoUsuario(enum.Enum):
    CONTRATISTA_NOADMIN = "CONTRATISTA_NOADMIN"
    CONTRATISTA_ADMIN = "CONTRATISTA_ADMIN"
    CONTRATANTE = "CONTRATANTE"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario = db.Column(db.String, nullable=False)
    contrasena = db.Column(db.String, nullable=False)
    correo = db.Column(db.String, nullable=False)
    tipoUsuario = db.Column(db.Enum(tipoUsuario), default=tipoUsuario.CONTRATISTA_NOADMIN)
    empresa_id = db.Column(db.String, db.ForeignKey('empresa.id'), nullable=False)  # Clave foránea
    empresa = db.relationship('Empresa', back_populates='usuarios')  # Relación con Empresa
    proyectos = db.relationship('Proyecto', secondary=tabla_usuarios_proyectos, back_populates='usuarios')
    proyectos_administrados = db.relationship("Proyecto", back_populates="admin", cascade="all, delete-orphan")
    
