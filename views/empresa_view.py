from flask_restful import Resource, reqparse
from models.empresa import Empresa, Contratante, Contratista
from models.db import db

class EmpresaView(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', required=True)
        parser.add_argument('tipo') #empresa, contratante o contratista
        parser.add_argument('nit', required=True)
        parser.add_argument('correo')
        args = parser.parse_args()

        tipo = args['tipo'].lower()

        if tipo == 'contratante':
            empresa = Contratante(
                nombre=args['nombre'],
                tipo='contratente',
                nit=args['nit'],
                correo=args['correo']
            )
        elif tipo == 'contratista':
            empresa = Contratista(
                nombre=args['nombre'],
                tipo='contratista',
                nit=args['nit'],
                correo=args['correo']
            )
        else:
            empresa = Empresa(
                nombre=args['nombre'],
                tipo=args['empresa'],
                nit=args['nit'],
                correo=args['correo']
            )

        db.session.add(empresa)
        db.session.commit()

        return {"mensaje": f"{tipo.capitalize()} creada correctamente"}, 201
