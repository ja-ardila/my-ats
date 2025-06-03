from flask_restful import Resource, reqparse
from models.preuso import Preuso
from models.db import db
from datetime import datetime

class PreusoView(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_ats', type=int, required=True)
        parser.add_argument('equipo')
        parser.add_argument('marca')
        parser.add_argument('serial')
        parser.add_argument('estado')
        parser.add_argument('observaciones')
        parser.add_argument('fecha')
        parser.add_argument('firma_trabajador')
        parser.add_argument('firma_autorizador')
        args = parser.parse_args()

        preuso = Preuso(
            id_ats=args['id_ats'],
            equipo=args['equipo'],
            marca=args['marca'],
            serial=args['serial'],
            estado=args['estado'],
            observaciones=args['observaciones'],
            fecha=datetime.strptime(args['fecha'], '%y-%m-%d').date() if args['fecha'] else None,
            firma_trabajador=args['firma_trabajador'],
            firma_autorizador=args['firma_autorizador']
        )
        db.session.add(preuso)
        db.session.commit()

        return {"mensaje": "registro de preuso creado correctamente"},201
            
        
