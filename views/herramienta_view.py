from flask_restful import Resource, reqparse
from models.herramienta import Herramienta
from models.db import db

class HerramientaView(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', required=True)
        parser.add_argument('estado')
        parser.add_argument('cantidad', type=int)
        parser.add_argument('observaciones')
        parser.add_argument('id_pt', type=int, required=True)
        args = parser.parse_args()

        herramienta = Herramienta(
            nombre=args['nombre'],
            estado=args['estado'],
            cantidad=args['cantidad'],
            observaciones=args['observaciones'],
            id_pt=args['id_pt']
        )

        db.session.add(herramienta)
        db.session.commit()

        return {"mensaje": "Herramienta registrada correctamente"}, 201
    

