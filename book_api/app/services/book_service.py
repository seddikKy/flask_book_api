from app.models import Book


class BookService:
    def __init__(self, book_repository):
        self.book_repository = book_repository

    def create_book(self, book_data):
        book = Book(
            title=book_data['title'],
            author_id=book_data['author_id']
        )
        self.book_repository.save(book)
        return book

    def get_book(self, book_id):
        return self.book_repository.get(book_id)

    def update_book(self, book_id, book_data):
        book = self.get_book(book_id)
        if not book:
            return False
        print(book_data)
        book.title = book_data['title']
        book.author_id = book_data['author_id']
        self.book_repository.save(book)
        return book

    def delete_book(self, book_id):
        book = self.get_book(book_id)
        self.book_repository.delete(book_id)
        return book

    def get_all_books(self):
        return self.book_repository.get_all()
