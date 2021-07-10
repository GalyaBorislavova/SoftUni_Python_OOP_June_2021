class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, current_library):
        if book_name in current_library.books_available[author]:
            current_library.books_available[author].remove(book_name)
            self.books.append(book_name)
            current_library.add_user(self)
            if self.username in current_library.rented_books:
                user_rented_books = current_library.rented_books[self.username]
                if not user_rented_books:
                    current_library.rented_books[self.username] = {book_name: days_to_return}
                else:
                    current_library.rented_books[self.username][book_name] = days_to_return
            else:
                current_library.rented_books[self.username] = {book_name: days_to_return}
                return f"{book_name} successfully rented for the next {days_to_return} days!"
        for username, rent_books in current_library.rented_books.items():
            for book, days in rent_books.items():
                if book == book_name:
                    return f'The book "{book_name}" is already rented and will be available in {days} days!'

    def return_book(self, author: str, book_name: str, current_library):
        if book_name in self.books:
            self.books.remove(book_name)
            current_library.books_available[author].append(book_name)
            del (current_library.rented_books[self.username][book_name])
        else:
            return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        sorted_user_rent_books = sorted(self.books)
        return ', '.join(sorted_user_rent_books)

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
