from flask import Blueprint, jsonify, request
from app.repositories.author_repository import SQLAlchemyAuthorRepository
from app.services.author_service import AuthorService
from app import db

bp = Blueprint('author', __name__, url_prefix='/authors')

author_repository = SQLAlchemyAuthorRepository(db)
author_service = AuthorService(author_repository)

@bp.route('/', methods=['GET'])
def get_all_authors():
    authors = author_service.get_all_authors()
    return jsonify([author.to_dict() for author in authors])

@bp.route('/', methods=['POST'])
def create_author():
    data = request.get_json()
    author = author_service.create_author(data)
    response = {
            "message": "author successfully added",
            "author": author.to_dict()
        }
    return jsonify(response), 201

@bp.route('/<int:author_id>', methods=['GET'])
def get_author(author_id):
    author = author_service.get_author(author_id)
    if author:
        return jsonify(author.to_dict())
    else:
        return '', 404

@bp.route('/<int:author_id>', methods=['PUT'])
def update_author(author_id):
    data = request.get_json()
    author = author_service.update_author(author_id, data)
    if author:
        response = {
            "message": "author successfully updated",
            "author": author.to_dict()
        }
        return jsonify(response)
    else:
        return '', 404

@bp.route('/<int:author_id>', methods=['DELETE'])
def delete_author(author_id):
    author = author_service.delete_author(author_id)
    if author:
        response = {
            "message": "Deleted author successfully",
            "author": author.to_dict()
        }
        return jsonify(response)
    else:
        return '', 404
