from database import load_data, save_data

def add_student():
    data = load_data()
    name = input("Enter student name: ")
    reg_no = input("Enter registration number: ")

    data["students"].append({"name": name, "reg_no": reg_no})
    save_data(data)
    print("Student added successfully\n")

def view_students():
    data = load_data()
    print("\n---- Registered Students ----")
    for std in data["students"]:
        print(f"{std['reg_no']} - {std['name']}")
    print()
