class BookViewer:

    def view_all_books(self, books):
        if not books:
            print("No books found.")
            return
        for book in books:
            print(f"book_id: {book.book_id}, {book.title} - {book.author} - {book.status}")
            

    def view_available_books(self, books):
        found = False
        for book in books:
            if book.status == 'Available':
                print(f"{book.book_id} - {book.title}")
                found = True
        if not found:
            print("No available books.")


    def view_borrowed_books(self, books):
        found = False
        for book in books:
            if book.status == 'Borrowed':
                print(f"{book.book_id} - {book.title} (Borrowed by: {book.borrower_name})")
                found = True
        if not found:
            print("No borrowed books.")


    def view_books_by_category(self, books, category):
        found = False
        for book in books:
            if book.category.lower() == category.lower():
                print(f"{book.book_id} - {book.title}")
                found = True
        if not found:
            print("No books found in this category.")


    def view_books_by_author(self, books, author):
        found = False
        for book in books:
            if book.author.lower() == author.lower():
                print(f"{book.book_id} - {book.title}")
                found = True
        if not found:
            print("No books found for this author.")


    def search_books(self, books, title):
        found = False
        for book in books:
            if book.title.lower() == title.lower():
                print(f"{book.book_id} - {book.title}")
                found = True
        if not found:
            print("No matching book found.")
