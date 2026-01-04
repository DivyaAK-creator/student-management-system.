import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "students.csv")


# ---------- ADD STUDENT ----------
def add_student():
    with open (FILE_NAME,"r")as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if row and row[0].strip()==sid:
                print("Student ID is already exists")
                return
    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)

        # If file is empty, write header
        if os.stat(FILE_NAME).st_size == 0:
            writer.writerow(["ID","Name","Department","Marks"])

        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        marks = input("Enter Marks: ")

        writer.writerow([sid,name,dept,marks])
        print("Student added successfully")


# ---------- VIEW STUDENTS ----------
def view_students():
    print("\nID".ljust(10), "Name".ljust(20), "Dept".ljust(10), "Marks".ljust(10))
    print("-" * 55)

    try:
        with open(FILE_NAME, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
            
                if not row:        # skip empty rows
                    continue
                print(
                    row[0].ljust(10),
                    row[1].ljust(20),
                    row[2].ljust(10),
                    row[3].ljust(10)
                )
    except FileNotFoundError:
        print("No student file found")


# ---------- SEARCH STUDENT ----------
def search_student():
    sid = input("Enter Student ID to search: ")
    found = False

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] == sid:
                print(" Student Found:", row)
                found = True
                break

    if not found:
        print(" Student not found")


# ---------- UPDATE STUDENT ----------
def update_student():
    sid = input("Enter Student ID to update: ")
    rows = []
    updated = False

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0].strip() == sid:
                header = next(reader)
                rows.append(header)
                print("Old Data:", row)
                sid = input("Enter new ID: ")
                name = input("Enter new Name: ")
                dept = input("Enter new Department: ")
                marks = input("Enter new Marks: ")
                rows.append([sid, name, dept, marks])
                updated = True
            else:
                rows.append(row)

    if updated:
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print(" Student updated successfully")
    else:
        print(" Student ID not found")

#--------Delete function-------

def delete_student():
    delete_id = input("Enter Student ID to delete: ").strip()

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        if not rows:
            print("No students found.")
            return

        new_rows = []
        found = False

        new_rows.append(rows[0])

        for row in rows:
            if row[0].strip()!= delete_id:
                new_rows.append(row)
            else:
                found = True

        if not found:
            print("Student ID not found.")
            return

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)

        print("Student deleted successfully.")

    except FileNotFoundError:
        print("No students file found.")








# ---------- MAIN MENU ----------
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. delete student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("👋 Exiting program")
        break
    else:
        print(" Invalid choice")