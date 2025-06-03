from flask_restful import Resource, reqparse
from models.trabajador import Trabajador
from models.db import db

class TrabajadorView(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', required=True)
        parser.add_argument('cedula', required=True)
        parser.add_argument('cargo')
        parser.add_argument('firma')
        parser.add_argument('id_ats', type=int, required=True)
        args = parser.parse_args()

        trabajador = Trabajador(
            nombre=args['nombre'],
            cedula=args['cedula'], 
            cargo=args['cargo'],
            firma=args['firma'],
            id_ats=args['id_ats']
        )

        db.session.add(trabajador)
        db.session.commit()

        return {"mensaje": "trabajador registrado correctamente"}, 201
    
        