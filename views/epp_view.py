from flask_restful import Resource, reqparse
from models.epp import EPP
from models.db import db

class  EPPView(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', required=True)
        parser.add_argument('estado', type=int)
        parser.add_argument('id_pt', type=int, required=True)
        args = parser.parse_args()

        epp = EPP(
            nombre=args['nombre'],
            canitdad=args['cantidad'],
            estado=args['estado'],
            id_pt=args['id_pt']
        )

        db.session.add(epp)
        db.session.commit()

        return {'mensaje': "EPP registrado correctamente"}, 201