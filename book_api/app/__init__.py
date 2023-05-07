import os
from flask import Flask
from app.models import db
from config import Config


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SERVER_NAME="localhost:5000" 
    )

    if test_config:
        app.config.update(test_config)
    else:
        app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        from .routes.book_routes import bp as book_bp
        from .routes.author_routes import bp as author_bp
        app.register_blueprint(book_bp)
        app.register_blueprint(author_bp)
        

    return app
