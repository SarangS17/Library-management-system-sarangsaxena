from database import read_file, write_file, BOOKS_FILE

def add_book():
    books = read_file(BOOKS_FILE)
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    book_id = input("Enter book ID: ")

    record = f"{book_id},{title},{author}"
    books.append(record)
    write_file(BOOKS_FILE, books)
    print("Book added successfully\n")

def view_books():
    books = read_file(BOOKS_FILE)
    print("\n---- Available Books ----")
    for book in books:
        book_id, title, author = book.split(",")
        print(f"{book_id} - {title} by {author}")
    print()
