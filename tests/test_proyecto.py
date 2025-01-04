# Crear un contexto de aplicación para interactuar con la base de datos
def test_example(client, app):
    with app.app_context():
        print("\n")
        from models import Proyecto, Contratista, Contratante, User, db, Empresa, Trabajador, Autorizador, Area, Ubicacion, Lugar, Ciudad
        from datetime import date
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

        print("\nPrueba de contratantes")
        contratantes = Contratante.query.all()
        for contratante in contratantes:
            print(contratante.nombre)

        print("\nPrueba de contratistas")
        contratistas = Contratista.query.all()
        for contratista in contratistas:
            print(contratista.nombre)

        # Crear un proyecto asociado
        proyecto = Proyecto(
            nombre="Proyecto de Prueba",
            contratista=contratista,
            contratante=contratante,
            admin=admin
        )

        db.session.add(proyecto)
        db.session.commit()

        proyectos = Proyecto.query.all()
        print("\nPrueba de proyecto(s)")
        for proyecto in proyectos:
            print(proyecto.admin)
            print(proyecto.contratista)
            print(proyecto.contratante)
            print(proyecto.nombre)
            print(proyecto.usuarios)

        admin.empresa_id = 1

        print("\nPrueba de admin user")
        usuarios = User.query.all()
        for usuario in usuarios:
            print(usuario.usuario)
            print(usuario.empresa)

        #Crear empleados
        empleadoT = Trabajador(
            nombre = "Juan Andrés",
            apellido = "Ardila",
            cargo = "Ingeniero",
            documento = "102928192",
            empresa_id = 1,
            arl = "Sura",
            eps = "Famisanar",
            fechaNacimiento = date(1990, 5, 15),
            fechaIngreso = date(2022, 3, 1),
        )

        empleadoC = Autorizador(
            nombre = "Enrique",
            apellido = "Díaz",
            cargo = "Supervisor",
            documento = "3283923",
            empresa_id = 2,
        )

        empleadoT2 = Trabajador(
            nombre = "Juan Pablo",
            apellido = "Carrillo",
            cargo = "Técnico",
            documento = "102928161",
            empresa_id = 1,
            arl = "Sura",
            eps = "Sanitas",
            fechaNacimiento = date(1999, 5, 15),
            fechaIngreso = date(2023, 3, 1),
        )

        empleadoC2 = Autorizador(
            nombre = "Gonzalo",
            apellido = "Verón",
            cargo = "Jefe de Area",
            documento = "102937612",
            empresa_id = 2,
        )

        #Agregar empleados a la base de datos
        db.session.add(empleadoT)
        db.session.add(empleadoC)
        db.session.add(empleadoT2)
        db.session.add(empleadoC2)
        db.session.commit()

        print("\nPrueba de trabajadores")
        trabajadores1 = Trabajador.query.all()
        for trabajador in trabajadores1:
            print(trabajador.nombre + " " + trabajador.apellido)
            print(trabajador.empresa)
            print(trabajador.tipo)

        print("\nPrueba de autorizadores")
        autorizadores1 = Autorizador.query.all()
        for autorizador in autorizadores1:
            print(autorizador.nombre)
            print(autorizador.apellido)
            print(autorizador.empresa)
            print(autorizador.tipo)


        print("\nPrueba de empleados en empresa")
        empresas = Empresa.query.all()
        for empresa in empresas:
            print(empresa.nombre)
            print(empresa.tipo)
            print(empresa.empleados)
        
        #Area, ubicaciones, lugares, y ciudades
        area1 = Area(
            nombre = "Subestación eléctrica",
            contratante_id = 2
        )
        ubicacion1 = Ubicacion(
            direccion = "Calle 123",
            contratante_id = 2
        )
        lugar1 = Lugar(
            nombre = "Primer piso",
            contratante_id = 2
        )
        ciudad1 = Ciudad(
            nombre = "Cali",
            contratante_id = 2
        )

        #Agregar areas, ubicaciones lugares, ciudades a la base de datos
        db.session.add(area1)
        db.session.add(ubicacion1)
        db.session.add(lugar1)
        db.session.add(ciudad1)
        db.session.commit()

        print("\n")
        contratista2 = Contratante.query.first()
        print(contratista2.areas[0].nombre)
        print(contratista2.ubicaciones[0].direccion)
        print(contratista2.lugares[0].nombre)
        print(contratista2.ciudades[0].nombre)






    