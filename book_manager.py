import json

class Book:
    def __init__(self, book_id, title, author, year, category, status, borrower_name):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.category = category
        self.status = status
        self.borrower_name = borrower_name


class LibraryManager:
    def __init__(self):
        self.books = []

    # Add a new book
    def add_book(self, book):
        self.books.append(book)

    # Borrow a book
    def borrow_book(self, book_id, borrower_name):
        for book in self.books:
            if book.book_id == book_id:
                if book.status == "Available":
                    book.status = "Borrowed"
                    book.borrower_name = borrower_name
                    print("Book borrowed successfully!")
                else:
                    print("This book is already borrowed!")
                return
        print("Book not found!")

    # Return a book
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.status == "Borrowed":
                    book.status = "Available"
                    book.borrower_name = ""
                    print("Book returned successfully!")
                else:
                    print("This book is not borrowed.")
                return
        print("Book not found!")

    # Save books to JSON
    def save_books(self, filename="books.json"):
        try:
            data = []
            for book in self.books:
                data.append({
                    "book_id": book.book_id,
                    "title": book.title,
                    "author": book.author,
                    "year": book.year,
                    "category": book.category,
                    "status": book.status,
                    "borrower_name": book.borrower_name
                })

            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)

            print("Books saved successfully!")
        except Exception as e:
            print("Error saving books:", e)

    # Load books from JSON
    def load_books(self, filename="books.json"):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)

            self.books = []
            for b in data:
                book = Book(
                    b["book_id"],
                    b["title"],
                    b["author"],
                    b["year"],
                    b["category"],
                    b["status"],
                    b["borrower_name"]
                )
                self.books.append(book)
                print("Books loaded successfully!")


        except FileNotFoundError:
            print("No saved file found, starting with empty library.")
        except Exception as e:
            print("Error loading books:", e)

    # Backup books
    def backup_books(self, filename="books_backup.json"):
        try:
            self.save_books(filename)
            print("Backup created successfully!")
        except:
            print("Backup failed")
