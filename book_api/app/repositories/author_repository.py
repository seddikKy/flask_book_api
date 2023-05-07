from abc import ABC, abstractmethod

from flask_sqlalchemy import SQLAlchemy
from app.models import Author
from typing import List, Optional


class AuthorRepository(ABC):
    @abstractmethod
    def save(self, author):
        pass

    @abstractmethod
    def get(self, author_id):
        pass

    @abstractmethod
    def update(self, author: Author):
        pass

    @abstractmethod
    def delete(self, author_id):
        pass

    @abstractmethod
    def get_all(self):
        pass


class SQLAlchemyAuthorRepository(AuthorRepository):
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def save(self, author: Author) -> Author:
        self.db.session.add(author)
        self.db.session.commit()
        return author

    def get(self, id: int) -> Optional[Author]:
        return self.db.session.query(Author).filter_by(id=id).first()

    def update(self, author: Author) -> Author:
        self.db.session.commit()
        return author

    def delete(self, id: int) -> None:
        author = self.get(id)
        print("****************************")
        print(author)
        self.db.session.delete(author)
        self.db.session.commit()

    def get_all(self) -> List[Author]:
        return self.db.session.query(Author).all()

