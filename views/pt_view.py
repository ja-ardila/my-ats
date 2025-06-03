from flask_restful import Resource, reqparse
from models.pt import PT
from models.db import db
from datetime import datetime

class PTView(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_ats', type=int, required=True)
        parser.add_argument('fecha_creacion')
        parser.add_argument('valido_desde')
        parser.add_argument('valido_hasta')
        parser.add_argument('lugar_ejecucion')
        parser.add_argument('tipo_trabajo')
        parser.add_argument('descripcion')
        parser.add_argument('observaciones')

        args = parser.parse_args()

        nuevo_pt = PT(
            id_ats=args['id_ats'],
            fecha_creacion=datetime.strptime(args['fecha_creacion'], '%Y-%m-%d').date() if args['fecha_creacion'] else None,
            valido_desde=datetime.strptime(args['valido_desde'], '%Y-%m-%d %H:%M') if args['valido_desde'] else None,
            valido_hasta=datetime.strptime(args['valido_hasta'], '%Y-%m-%d %H:%M') if args['valido_hasta'] else None,
            lugar_ejecucion=args['lugar_ejecucion'],
            tipo_trabajo=args['tipo_trabajo'],
            descripcion=args['descripcion'],
            observaciones=args['observaciones']
        )

        db.session.add(nuevo_pt)
        db.session.commit()

        return {"mensaje": "PT creado correctamente"}, 201