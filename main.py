from books import add_book, view_books
from students import add_student, view_students
from database import read_file, write_file, ISSUED_FILE

def issue_book():
    issues = read_file(ISSUED_FILE)
    reg_no = input("Enter student reg number: ")
    book_id = input("Enter book ID: ")

    record = f"{reg_no},{book_id}"
    issues.append(record)
    write_file(ISSUED_FILE, issues)
    print("Book issued successfully\n")

def return_book():
    issues = read_file(ISSUED_FILE)
    reg_no = input("Enter student reg number: ")
    book_id = input("Enter book ID to return: ")

    record = f"{reg_no},{book_id}"

    if record in issues:
        issues.remove(record)
        write_file(ISSUED_FILE, issues)
        print("Book returned successfully\n")
    else:
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
