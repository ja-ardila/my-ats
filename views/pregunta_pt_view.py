from flask_restful import Resource, reqparse
from models.pregunta_pt import Pregunta_PT
from models.db import db

class PreguntaPTView(Resource):
    def post(self):
        parser = reqparse.RequestParser('pregunta', required=True)
        parser.add_argument('respuesta')
        parser.add_argument('id_pt', type=int, required=True)
        args = parser.parse_args()

        pregunta = Pregunta_PT(
            pregunta=args['pregunta'],
            respuesta=args['respuesta'],
            id_pt=args['id_pt']
        )

        db.session.add(pregunta)
        db.session.commit()

        return {"mensaje": "Pregunta de analisis registrada correctamente"}, 201