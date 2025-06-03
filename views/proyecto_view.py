from flask_restful import Resource, reqparse
from models.proyecto import Proyecto
from models.db import db

class ProyectoView(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', required=True)
        parser.add_argument('contratista_id', type=int, required=True)
        parser.add_argument('contratante_id', type=int, required=True)
        parser.add_argument('admin_id', type=int, required=True)
        args= parser.parse_args()

        proyecto = Proyecto(
            nombre=args['nombre'],
            contratista_id=args['contratista_id'],
            contratante_id=args['contratante_id'],
            admin_id=args['admin_id']
        )

        db.session.add(proyecto)
        db.session.commit()

        return {"mensaje": "Proyecto creado correctamente"}, 201
