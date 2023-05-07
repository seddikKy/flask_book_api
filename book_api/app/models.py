from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    author = db.Column(db.String(128))

    def __init__(self, title, author):
        self.title = title
        self.author = author


    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author
        }