from abc import ABC, abstractmethod

from flask_sqlalchemy import SQLAlchemy
from app.models import Book
from typing import List, Optional


class BookRepository(ABC):
    @abstractmethod
    def save(self, book):
        pass

    @abstractmethod
    def get(self, book_id):
        pass

    @abstractmethod
    def update(self, book: Book):
        pass

    @abstractmethod
    def delete(self, book_id):
        pass

    @abstractmethod
    def get_all(self):
        pass


class SQLAlchemyBookRepository(BookRepository):
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def save(self, book: Book) -> Book:
        self.db.session.add(book)
        self.db.session.commit()
        return book

    def get(self, id: int) -> Optional[Book]:
        return self.db.session.query(Book).filter_by(id=id).first()

    def update(self, book: Book) -> Book:
        self.db.session.commit()
        return book

    def delete(self, id: int) -> None:
        book = self.get(id)
        self.db.session.delete(book)
        self.db.session.commit()

    def get_all(self) -> List[Book]:
        return self.db.session.query(Book).all()

