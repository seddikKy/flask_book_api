from app.models import Author


class AuthorService:
    def __init__(self, author_repository):
        self.author_repository = author_repository

    def create_author(self, author_data):
        author = Author(
            name=author_data['name'],
        )
        self.author_repository.save(author)
        return author

    def get_author(self, author_id):
        return self.author_repository.get(author_id)

    def update_author(self, author_id, author_data):
        author = self.get_author(author_id)
        if not author:
            return False

        author.name = author_data['name']
        self.author_repository.save(author)
        return author

    def delete_author(self, author_id):
        author = self.get_author(author_id)
        self.author_repository.delete(author_id)
        return author

    def get_all_authors(self):
        return self.author_repository.get_all()
