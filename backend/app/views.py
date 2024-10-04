from typing import Any

from flask import Blueprint
from flask_restful import Api, Resource
from werkzeug.exceptions import HTTPException

from .models import Audiobook, db

main_bp: Blueprint = Blueprint("main", __name__)

api: Api = Api(main_bp)


class AudiobookList(Resource):
    def get(self) -> tuple[list[dict[str, int | str]], int]:
        audiobooks: list[Audiobook] = Audiobook.query.all()

        return [audiobook.to_dict() for audiobook in audiobooks], 200


class AudiobookVote(Resource):
    def post(self, id: int) -> tuple[dict[str, Any], int]:
        audiobook: Audiobook = Audiobook.query.get(id)

        if audiobook:
            audiobook.votes += 1
            db.session.commit()

            return {"message": "Vote counted", "audiobook": audiobook.to_dict()}, 200

        return {"message": "Audiobook not found"}, 404


api.add_resource(AudiobookList, "/audiobooks")
api.add_resource(AudiobookVote, "/audiobooks/<int:id>/vote")


@main_bp.errorhandler(404)
def not_found(error: HTTPException) -> tuple[dict[str, str], int]:
    return {"error": "Not found"}, 404


@main_bp.errorhandler(500)
def internal_error(error: HTTPException) -> tuple[dict[str, str], int]:
    db.session.rollback()
    return {"error": "Internal server error"}, 500
