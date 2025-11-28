from books import add_book, view_books
from students import add_student, view_students
from database import load_data, save_data

def issue_book():
    data = load_data()
    reg_no = input("Enter student reg number: ")
    book_id = input("Enter book ID: ")

    for book in data["books"]:
        if book["book_id"] == book_id:
            data["issued"].append({"reg_no": reg_no, "book_id": book_id})
            save_data(data)
            print("Book issued successfully\n")
            return
    print("Book not found\n")

def return_book():
    data = load_data()
    reg_no = input("Enter student reg number: ")
    book_id = input("Enter book ID to return: ")

    for issue in data["issued"]:
        if issue["reg_no"] == reg_no and issue["book_id"] == book_id:
            data["issued"].remove(issue)
            save_data(data)
            print("Book returned successfully\n")
            return
    print("Record not found\n")

def menu():
    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Add Student")
        print("4. View Students")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("Enter option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            add_student()
        elif choice == "4":
            view_students()
        elif choice == "5":
            issue_book()
        elif choice == "6":
            return_book()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid option")

menu()
