# Crear un contexto de aplicación para interactuar con la base de datos
def test_example(client, app):
    with app.app_context():
        from models import Proyecto, Contratista, Contratante, User, db, Empresa
        # Crear objetos de prueba
        contratista = Contratista(
            nombre="Empresa Contratista 1",
            nit="392293221-1",
            correo="correo@contratista.com"
            )
        contratante = Contratante(
            nombre="Empresa Contratante 1",
            nit="48928323-1",
            correo="correo@contratante.com"
            )
        admin = User(
            usuario="admin_user",
            contrasena="password",
            empresa=contratante,
            correo = "correo@usuario.com",
            tipoUsuario = "CONTRATANTE"
            )

        # Agregar datos a la base de datos
        db.session.add(contratista)
        db.session.add(contratante)
        db.session.add(admin)
        db.session.commit()

        contratantes = Contratante.query.all()
        for contratante in contratantes:
            print(contratante.nombre)

        contratistas = Contratista.query.all()
        for contratista in contratistas:
            print(contratista.nombre)

        usuarios = User.query.all()
        for usuario in usuarios:
            print(usuario.usuario)

        # Crear un proyecto asociado
        proyecto = Proyecto(
            nombre="Proyecto de Prueba",
            contratista=contratista,
            contratante=contratante,
            admin=admin
        )

        db.session.add(proyecto)
        db.session.commit()



    