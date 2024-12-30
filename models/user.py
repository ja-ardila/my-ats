from models import db
from flask_sqlalchemy import SQLAlchemy
import enum

class tipoUsuario(enum.Enum):
    CONTRATISTA_NOADMIN = "CONTRATISTA_NOADMIN"
    CONTRATISTA_ADMIN = "CONTRATISTA_ADMIN"
    CONTRATANTE = "CONTRATANTE"

class user(db.Model):
    id = db.Column(db.String, primary_key=True)
    usuario = db.Column(db.String, nullable=False)
    contrasena = db.Column(db.String, nullable=False)
    empresa = db.Column(db.String, nullable=False)
    tipoUsuario = db.Column(db.Enum(tipoUsuario), default=tipoUsuario.CONTRATISTA_NOADMIN)
    
