#14 management system
FILE_NAME = "students.txt"

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{marks}\n")
    print("Student added successfully!\n")
def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            print("\nStudent Records:")
            print("------------------")
            print(file.read())
    except FileNotFoundError:
        print("No records found.\n")
def search_student():
    roll_search = input("Enter Roll No to search: ")
    found = False
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                roll, name, marks = line.strip().split(",")

                if roll == roll_search:
                    print("\nRecord Found:")
                    print("Roll No:", roll)
                    print("Name:", name)
                    print("Marks:", marks)
                    found = True
                    break

        if not found:
            print("Student not found.\n")

    except FileNotFoundError:
        print("No records available.\n")
def delete_student():
    roll_delete = input("Enter Roll No to delete: ")
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        with open(FILE_NAME, "w") as file:
            for line in lines:
                roll, name, marks = line.strip().split(",")

                if roll != roll_delete:
                    file.write(line)
                else:
                    found = True

        if found:
            print("Student deleted successfully!\n")
        else:
            print("Student not found.\n")

    except FileNotFoundError:
        print("No records available.\n")

while True:
    print("\n===== Student Record System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting system...")
        break
    else:
        print("Invalid choice! Try again.\n")