BOOKS_FILE = "books.txt"
STUDENTS_FILE = "students.txt"
ISSUED_FILE = "issued.txt"

def read_file(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except:
        return []

def write_file(filename, data):
    with open(filename, "w") as file:
        for item in data:
            file.write(item + "\n")
