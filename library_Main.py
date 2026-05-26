from book_manager import LibraryManager, Book
from Book_Viewer import BookViewer

def main():
    print('\n Welcome to Library Management System \n')
    manager = LibraryManager()  
    viewer = BookViewer()
    manager.load_books()  #Load saved books
    #	Loop menu with options
    while True:
        print('\n  ------ Main Menu ----------')
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. View all books")
        print("5. View available books")
        print("6. View borrowed books")
        print("7. View books by category")
        print("8. View books by author")
        print("9. Search for a book")
        print("10. Exit")

        try:
            choice = int(input("Enter your choice (1-10): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 10.")
            continue
        # Add a new book
        if choice == 1:
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            category = input("Category: ")
            new_book = Book(book_id, title, author, year, category, "Available", "")
            manager.add_book(new_book)
           
        #	Borrow a book
        elif choice == 2:
            book_id = input("Book ID to borrow: ")
            name = input("Borrower name: ")
            manager.borrow_book(book_id, name)
        #	Return a book
        elif choice == 3:
            book_id = input("Book ID to return: ")
            manager.return_book(book_id)
         #	View all books
        elif choice == 4:
            viewer.view_all_books(manager.books)
         # View available books
        elif choice == 5:
            viewer.view_available_books(manager.books)
         # 	View borrowed books
        elif choice == 6:
            viewer.view_borrowed_books(manager.books)
         #	View books by category
        elif choice == 7:
            category = input("Enter category: ")
            viewer.view_books_by_category(manager.books, category)
           #	View books by author
        elif choice == 8:
            author = input("Enter author: ")
            viewer.view_books_by_author(manager.books, author)
        #	Search for a book
        elif choice == 9:
            title = input("Enter a title: ")
            viewer.search_books(manager.books, title)
           # Exit
        elif choice == 10:
            print("Saving books... Goodbye!")
            manager.save_books(filename='books.json')
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 10.")

if __name__ == "__main__":
    main()