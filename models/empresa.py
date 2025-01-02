from models import db

class Empresa(db.Model):
    __tablename__ = 'empresa'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String, nullable=False)
    tipo = db.Column(db.String)
    nit = db.Column(db.String, nullable=False)
    correo = db.Column(db.String, nullable=False)

    usuarios = db.relationship("User", back_populates="empresa")  # Relación con Empresa


    """ def __init__(self):
        from models import User  # Importación aquí, cuando realmente se necesite
        self.usuarios = db.relationship(User, back_populates='empresa', lazy=True) """

    """logo = db.Column(db.LargeBinary, nullable=True)  # Campo binario para la imagen"""
    # Relación con empleados
    empleados = db.relationship("Empleado", back_populates="empresa") 


    __mapper_args__ = {
        'polymorphic_identity': 'empresa',
        'polymorphic_on': tipo,
        #'with_polymorphic': '*',  # Incluye todas las subclases en consultas por Empresa
    }

class Contratista(Empresa):
    __tablename__ = 'contratista'
    id = db.Column(db.Integer, db.ForeignKey('empresa.id'), primary_key=True)
    proyectos_contratista = db.relationship("Proyecto", back_populates="contratista", cascade="all, delete-orphan")

    __mapper_args__ = {
        'polymorphic_identity': 'contratista',
    }

class Contratante(Empresa):
    __tablename__ = 'contratante'
    id = db.Column(db.Integer, db.ForeignKey('empresa.id'), primary_key=True)
    proyectos_contratante = db.relationship("Proyecto", back_populates="contratante", cascade="all, delete-orphan")

    # Relaciones uno-a-muchos
    """ areas = db.relationship("Area", back_populates="contratante", cascade="all, delete-orphan")
    ubicaciones = db.relationship("Ubicacion", back_populates="contratante", cascade="all, delete-orphan")
    lugares = db.relationship("Lugar", back_populates="contratante", cascade="all, delete-orphan")
    ciudades = db.relationship("Ciudad", back_populates="contratante", cascade="all, delete-orphan") """

    __mapper_args__ = {
        'polymorphic_identity': 'contratante',
    }

""" #Tablas Arrays

class Area(db.Model):
    __tablename__ = 'area'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String, nullable=False)
    contratante_id = db.Column(db.String, db.ForeignKey('contratante.id'), nullable=False)

    contratante = db.relationship("Contratante", back_populates="areas")

class Ubicacion(db.Model):
    __tablename__ = 'ubicacion'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    direccion = db.Column(db.String, nullable=False)
    contratante_id = db.Column(db.String, db.ForeignKey('contratante.id'), nullable=False)

    contratante = db.relationship("Contratante", back_populates="ubicaciones")

class Lugar(db.Model):
    __tablename__ = 'lugar'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String, nullable=False)
    contratante_id = db.Column(db.String, db.ForeignKey('contratante.id'), nullable=False)

    contratante = db.relationship("Contratante", back_populates="lugares")

class Ciudad(db.Model):
    __tablename__ = 'ciudad'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String, nullable=False)
    contratante_id = db.Column(db.String, db.ForeignKey('contratante.id'), nullable=False)

    contratante = db.relationship("Contratante", back_populates="ciudades") """