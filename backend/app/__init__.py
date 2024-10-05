import logging
import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

db: SQLAlchemy = SQLAlchemy()


def create_tables(app: Flask) -> None:
    try:
        with app.app_context():
            db.create_all()

            from .models import Audiobook

            if Audiobook.query.count() == 0:
                audiobooks: list[Audiobook] = [
                    Audiobook(title="Audiobook 1", author="Author 1", cover_image="https://picsum.photos/200"),
                    Audiobook(title="Audiobook 2", author="Author 2", cover_image="https://picsum.photos/200"),
                    Audiobook(title="Audiobook 3", author="Author 3", cover_image="https://picsum.photos/200"),
                    Audiobook(title="Audiobook 4", author="Author 4", cover_image="https://picsum.photos/200"),
                ]

                db.session.bulk_save_objects(audiobooks)
                db.session.commit()

                app.logger.info("Initial audiobooks added to the database.")
    except SQLAlchemyError as e:
        app.logger.error(f"Error creating tables or adding initial data: {str(e)}")

        db.session.rollback()


def create_app() -> Flask:
    os.makedirs("instance", exist_ok=True)

    app: Flask = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    logging.basicConfig(level=logging.INFO)

    CORS(app)

    from .views import main_bp

    app.register_blueprint(main_bp)

    create_tables(app)

    return app
