from flask import Blueprint, jsonify, request
from app.repositories.book_repository import SQLAlchemyBookRepository
from app.services.book_service import BookService
from app import db

bp = Blueprint('book', __name__, url_prefix='/books')

book_repository = SQLAlchemyBookRepository(db)
book_service = BookService(book_repository)

@bp.route('/', methods=['GET'])
def get_all_books():
    books = book_service.get_all_books()
    return jsonify([book.to_dict() for book in books])

@bp.route('/', methods=['POST'])
def create_book():
    data = request.get_json()
    book = book_service.create_book(data)
    response = {
            "message": "book successfully added",
            "book": book.to_dict()
        }
    return jsonify(response), 201

@bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = book_service.get_book(book_id)
    if book:
        return jsonify(book.to_dict())
    else:
        return '', 404

@bp.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = book_service.update_book(book_id, data)
    if book:
        response = {
            "message": "book successfully updated",
            "book": book.to_dict()
        }
        return jsonify(response)
    else:
        return '', 404

@bp.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = book_service.delete_book(book_id)
    if book:
        response = {
            "message": "Deleted book successfully",
            "book": book.to_dict()
        }
        return jsonify(response)
    else:
        return '', 404
