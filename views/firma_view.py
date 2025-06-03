from flask_restful import Resource, reqparse
from models.firma import Firma
from models.db import db
from datetime import datetime

class FirmaView(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', required=True)
        parser.add_argument('cargo')
        parser.add_argument('tipo')
        parser.add_argument('firma_digital')
        parser.add_argument('fecha')
        args = parser.parse_args()

        nueva_firma = Firma(
            nombre=args['nombre'],
            cargo=args['cargo'],
            tipo=args['tipo'],
            firma_digital=args['firma_digital'],
            fecha=datetime.strftime(args['fecha'], '%Y-%m-%d').date() if args['fecha'] else None
        )
    
        db.session.add(nueva_firma)
        db.session.commit()

        return{"mensaje": "firma registrada correctamente"}, 201
    