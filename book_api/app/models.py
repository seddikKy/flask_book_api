from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))

    def __init__(self, name):
        self.name = name


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }
    
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship('Author', backref=db.backref('books', lazy='dynamic'))

    def __init__(self, title, author_id):
        self.title = title
        self.author_id = author_id


    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author_id': self.author_id
        }
