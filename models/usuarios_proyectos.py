from models import db

# Tabla de asociación para la relación muchos a muchos entre usuarios y proyectos
tabla_usuarios_proyectos = db.Table(
    'tabla_usuarios_proyectos',
    db.Column('proyecto_id', db.Integer, db.ForeignKey('proyecto.id'), primary_key=True),
    db.Column('usuario_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)