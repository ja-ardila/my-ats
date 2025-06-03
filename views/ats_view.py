from flask_restful import Resource, reqparse
from models.ats import ATS
from models.db import db
from datetime import datetime

class ATSView(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('empresa')
        parser.add_argument('ciudad')
        parser.add_argument('area_proceso')
        parser.add_argument('ubicacion')
        parser.add_argument('fecha')  
        parser.add_argument('lugar')
        parser.add_argument('hora')   
        parser.add_argument('id_proyecto', type=int)
        args = parser.parse_args()

        fecha = datetime.strptime(args['fecha'], '%Y-%m-%d').date() if args['fecha'] else None
        hora = datetime.strptime(args['hora'], '%H:%M').time() if args['hora'] else None

        nuevo_ats = ATS(
            empresa=args['empresa'],
            ciudad=args['ciudad'],
            area_proceso=args['area_proceso'],
            ubicacion=args['ubicacion'],
            fecha=fecha,
            lugar=args['lugar'],
            hora=hora,
            id_proyecto=args['id_proyecto']
        )

        db.session.add(nuevo_ats)
        db.session.commit()

        return {"mensaje": "ATS creado correctamente"}, 201