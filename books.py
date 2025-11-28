from database import load_data, save_data

def add_book():
    data = load_data()
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    book_id = input("Enter book ID: ")

    data["books"].append({"title": title, "author": author, "book_id": book_id})
    save_data(data)
    print("Book added successfully\n")

def view_books():
    data = load_data()
    print("\n---- Available Books ----")
    for book in data["books"]:
        print(f"{book['book_id']} - {book['title']} by {book['author']}")
    print()
