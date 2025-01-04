from models import db
import enum
from sqlalchemy import Enum
from enum import Enum as PyEnum

class grupoSanguineo(enum.Enum):
    AP = "A+"
    AN = "A-"
    BP = "B+"
    BN = "B-"
    OP = "O+"
    ON = "O-"
    ABP = "AB+"
    ABN = "AB-"

class Empleado(db.Model):
    __tablename__ = 'empleado'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String, nullable=False)
    apellido = db.Column(db.String, nullable=False)
    cargo = db.Column(db.String, nullable=False)
    documento = db.Column(db.String, nullable=False)
    tipo = db.Column(db.String, nullable=False)  # Para distinguir entre Autorizador y Trabajador
    empresa_id = db.Column(db.String, db.ForeignKey('empresa.id'), nullable=False)
    # Relación con Empresa
    empresa = db.relationship("Empresa", back_populates="empleados")

    __mapper_args__ = {
        'polymorphic_identity': 'empleado',
        'polymorphic_on': tipo
    }

class Trabajador(Empleado):
    __tablename__ = 'trabajador'
    id = db.Column(db.Integer, db.ForeignKey('empleado.id'), primary_key=True, autoincrement=True)
    arl = db.Column(db.String, nullable=False)
    eps = db.Column(db.String, nullable=False)
    tipoDocumento = db.Column(db.String, default='CC')
    sst = db.Column(db.Boolean, default=False)
    grupoSanguineo = db.Column(Enum(grupoSanguineo), default=grupoSanguineo.OP)
    fechaNacimiento = db.Column(db.Date, nullable=False)
    fechaIngreso = db.Column(db.Date, nullable=False)
    vencimientoMedico = db.Column(db.Date, nullable=True)
    vencimientoCurso = db.Column(db.Date, nullable=True)


    __mapper_args__ = {
        'polymorphic_identity': 'trabajador',
    }

class Autorizador(Empleado):
    __tablename__ = 'autorizador'
    id = db.Column(db.Integer, db.ForeignKey('empleado.id'), primary_key=True, autoincrement=True)

    __mapper_args__ = {
        'polymorphic_identity': 'autorizador',
    }
