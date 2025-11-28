from database import read_file, write_file, STUDENTS_FILE

def add_student():
    students = read_file(STUDENTS_FILE)
    name = input("Enter student name: ")
    reg_no = input("Enter registration number: ")

    record = f"{reg_no},{name}"
    students.append(record)
    write_file(STUDENTS_FILE, students)
    print("Student added successfully\n")

def view_students():
    students = read_file(STUDENTS_FILE)
    print("\n---- Registered Students ----")
    for std in students:
        reg_no, name = std.split(",")
        print(f"{reg_no} - {name}")
    print()
