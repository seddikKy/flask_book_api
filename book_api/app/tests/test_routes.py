from http import HTTPStatus
from typing import List

from flask import url_for
from flask.testing import FlaskClient
from app.tests.conftest import app
from pytest import fixture

from app import create_app, db
from app.models import Book


class TestBookRoutes:

    def test_get_all_books(self, client: FlaskClient):
        with client.application.app_context():
            response = client.get(url_for("book.get_all_books"))
            assert response.status_code == HTTPStatus.OK 

    def test_get_book(self, client: FlaskClient):
        book = Book(title="Book 1", author="Author 1")
        with client.application.app_context():
            db.session.add(book)
            db.session.commit()
            response = client.get(url_for("book.get_book", book_id=book.id))
            assert response.status_code == HTTPStatus.OK
            assert response.json["title"] == book.title
            assert response.json["author"] == book.author

    def test_create_book(self, client: FlaskClient):
        book_data = {"title": "Book 1", "author": "Author 1"}
        with client.application.app_context():
            response = client.post(
                url_for("book.create_book"),
                json=book_data,
                content_type="application/json",
            )
            assert response.status_code == HTTPStatus.CREATED
            assert response.json["book"]["title"] == book_data["title"]
            assert response.json["book"]["author"] == book_data["author"]

    def test_update_book(self, client: FlaskClient):
        book = Book(title="Book 1", author="Author 1")
        with client.application.app_context():
            db.session.add(book)
            db.session.commit()
            book_data = {"title": "Updated Book 1", "author": "Updated Author 1"}
            response = client.put(
                url_for("book.update_book", book_id=book.id),
                json=book_data,
                content_type="application/json",
            )
            assert response.status_code == HTTPStatus.OK
            assert response.json["book"]["title"] == book_data["title"]
            assert response.json["book"]["author"] == book_data["author"]

    def test_delete_book(self, client: FlaskClient):
        book = Book(title="Book 1", author="Author 1")
        with client.application.app_context():
            db.session.add(book)
            db.session.commit()
            response = client.delete(url_for("book.delete_book", book_id=book.id))
            assert response.status_code == HTTPStatus.OK
            assert not Book.query.filter_by(id=book.id).first()

