import pytest
from app.models import Author
from app.services.author_service import AuthorService
from app.repositories.author_repository import SQLAlchemyAuthorRepository
from app import db


@pytest.fixture
def author_service(app):
    with app.app_context():
        service = AuthorService(SQLAlchemyAuthorRepository(db))
        yield service

class TestAuthorService:
    def test_create_author(self, app, author_service):
        with app.app_context():
            author_data = {
                'name': 'Test author',
            }
            author = author_service.create_author(author_data)
            assert isinstance(author, Author)
            assert author.id is not None
            assert author.name == 'Test author'

    def test_get_author(self, app, author_service):
        with app.app_context():
            author_data = {
                'name': 'Test author',
            }
            author = author_service.create_author(author_data)
            retrieved_author = author_service.get_author(author.id)
            assert retrieved_author == author

    def test_update_author(self, app, author_service):
        with app.app_context():
            author_data = {
                'name': 'Test author',
            }
            author = author_service.create_author(author_data)
            update_data = {
                'name': 'New Test author',
            }
            updated_author = author_service.update_author(author.id, update_data)
            assert updated_author == author_service.get_author(author.id)
            assert updated_author.name == 'New Test author'
        
    def test_delete_author(self, app, author_service):
        with app.app_context():
            author_data = {
                'name': 'Test author',
            }
            author = author_service.create_author(author_data)
            deleted_author = author_service.delete_author(author.id)
            assert deleted_author == author
            assert author_service.get_author(author.id) is None

    def test_get_all_authors(self, app, author_service):
        with app.app_context():
            author_data1 = {'name': 'Test author 1'}
            author1 = author_service.create_author(author_data1)

            author_data2 = {'name': 'Test author 2'}
            author2 = author_service.create_author(author_data2)

            authors = author_service.get_all_authors()

            assert isinstance(authors, list)
            assert len(authors) == 2
            assert author1 in authors
            assert author2 in authors



