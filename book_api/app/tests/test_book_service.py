import pytest
from app.models import Book
from app.services.book_service import BookService
from app.repositories.book_repository import SQLAlchemyBookRepository
from app import db


@pytest.fixture
def book_service(app):
    with app.app_context():
        service = BookService(SQLAlchemyBookRepository(db))
        yield service

class TestBookService:
    def test_create_book(self, app, book_service):
        with app.app_context():
            book_data = {
                'title': 'Test Book',
                'author': 'Test Author'
            }
            book = book_service.create_book(book_data)
            assert isinstance(book, Book)
            assert book.id is not None
            assert book.title == 'Test Book'
            assert book.author == 'Test Author'

    def test_get_book(self, app, book_service):
        with app.app_context():
            book_data = {
                'title': 'Test Book',
                'author': 'Test Author'
            }
            book = book_service.create_book(book_data)
            retrieved_book = book_service.get_book(book.id)
            assert retrieved_book == book

    def test_update_book(self, app, book_service):
        with app.app_context():
            book_data = {
                'title': 'Test Book',
                'author': 'Test Author'
            }
            book = book_service.create_book(book_data)
            update_data = {
                'title': 'New Test Book',
                'author': 'New Test Author'
            }
            updated_book = book_service.update_book(book.id, update_data)
            assert updated_book == book_service.get_book(book.id)
            assert updated_book.title == 'New Test Book'
            assert updated_book.author == 'New Test Author'

    def test_delete_book(self, app, book_service):
        with app.app_context():
            book_data = {
                'title': 'Test Book',
                'author': 'Test Author'
            }
            book = book_service.create_book(book_data)
            deleted_book = book_service.delete_book(book.id)
            assert deleted_book == book
            assert book_service.get_book(book.id) is None

    def test_get_all_books(self, app, book_service):
        with app.app_context():
            book_data1 = {'title': 'Test Book 1', 'author': 'Test Author 1'}
            book1 = book_service.create_book(book_data1)

            book_data2 = {'title': 'Test Book 2', 'author': 'Test Author 2'}
            book2 = book_service.create_book(book_data2)

            books = book_service.get_all_books()

            assert isinstance(books, list)
            assert len(books) == 2
            assert book1 in books
            assert book2 in books



