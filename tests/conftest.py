import pytest
from app import create_flask_app
from models import db

@pytest.fixture
def app():
    """Crea una instancia de la aplicación Flask para pruebas."""
    app = create_flask_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Base de datos en memoria para pruebas
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Inicializar la base de datos con la app
    db.init_app(app)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Crea un cliente de prueba para la aplicación Flask."""
    return app.test_client()
