from flask import Flask
from flask_restful import Api
from views import *
from os import environ
from models import db

def create_flask_app():
    dbURL = "postgresql://{}:{}@{}:{}/{}".format(environ.get('DB_USER', ""), environ.get('DB_PASSWORD', ""), 
                      environ.get('DB_HOST', ""), environ.get('DB_PORT', ""), environ.get('DB_NAME', ""))
    if dbURL == "postgresql://:@:/":
        dbURL = 'sqlite:///my_ats.db'
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = dbURL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app_context = app.app_context()
    app_context.push()
    endpoints(app)

    return app

def endpoints(app):
    api = Api(app)
    #api.add_resource(UsersView, '/users')


app = create_flask_app()
db.init_app(app)
db.create_all()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=3000)

""" from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_ats2.db'
db = SQLAlchemy(app)

# Clase base Empleado
class Empleado(db.Model):
    __tablename__ = 'empleados'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    tipo_empleado = db.Column(db.String(50))

    # Este argumento define el polimorfismo
    __mapper_args__ = {
        'polymorphic_identity': 'empleado',
        'polymorphic_on': tipo_empleado
    }

# Clase hija Trabajador que hereda de Empleado
class Trabajador(Empleado):
    __tablename__ = 'trabajadores'
    id = db.Column(db.Integer, db.ForeignKey('empleados.id'), primary_key=True)
    puesto = db.Column(db.String, nullable=False)

    # Este argumento define el polimorfismo
    __mapper_args__ = {
        'polymorphic_identity': 'trabajador',
    }

# Clase hija Manager que hereda de Empleado
class Manager(Empleado):
    __tablename__ = 'managers'
    id = db.Column(db.Integer, db.ForeignKey('empleados.id'), primary_key=True)
    departamento = db.Column(db.String, nullable=False)

    # Este argumento define el polimorfismo
    __mapper_args__ = {
        'polymorphic_identity': 'manager',
    }


# Crear la base de datos y las tablas
with app.app_context():
    db.create_all()

# Crear instancias de cada tipo de empleado
trabajador = Trabajador(nombre="Juan Pérez", puesto="Desarrollador")
manager = Manager(nombre="Ana López", departamento="TI")

# Agregar a la base de datos
with app.app_context():
    db.session.add(trabajador)
    db.session.add(manager)
    db.session.commit()

# Consultar y mostrar los empleados desde la base de datos
with app.app_context():
    empleados = Empleado.query.all()
    for empleado in empleados:
        print(empleado) """