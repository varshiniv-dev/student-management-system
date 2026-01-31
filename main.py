students = {}


def add_student():
    usn = input("Enter USN: ")
    name = input("Enter Name: ")
    students[usn] = name
    print("Student added successfully.")


def view_students():
    if not students:
        print("No records found.")
    else:
        for usn, name in students.items():
            print(usn, "-", name)


def delete_student():
    usn = input("Enter USN to delete: ")
    if usn in students:
        del students[usn]
        print("Student deleted.")
    else:
        print("Student not found.")


while True:
    print("\n1.Add  2.View  3.Delete  4.Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        break
    else:
        print("Invalid choice")
