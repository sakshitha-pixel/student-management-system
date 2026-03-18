import sqlite3

# Database connection
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY,
name TEXT,
branch TEXT,
marks INTEGER,
grade TEXT
)
""")

# Grade function
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"

# Add student
def add_student():
    id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    marks = int(input("Enter Marks: "))

    grade = calculate_grade(marks)

    cursor.execute("INSERT INTO students VALUES(?,?,?,?,?)",
                   (id, name, branch, marks, grade))
    conn.commit()

    print("Student Added Successfully")
    print("Grade:", grade)

# View students
def view_students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    if data:
        print("\nStudent Records:")
        for i in data:
            print(i)
    else:
        print("No records found")

# Search student
def search_student():
    id = int(input("Enter Student ID: "))

    cursor.execute("SELECT * FROM students WHERE id=?", (id,))
    data = cursor.fetchone()

    if data:
        print("Record Found:", data)
    else:
        print("Student not found")

# Update student
def update_student():
    id = int(input("Enter Student ID: "))
    new_marks = int(input("Enter new marks: "))

    grade = calculate_grade(new_marks)

    cursor.execute("UPDATE students SET marks=?, grade=? WHERE id=?",
                   (new_marks, grade, id))
    conn.commit()

    print("Record Updated")

# Delete student
def delete_student():
    id = int(input("Enter Student ID: "))

    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()

    print("Record Deleted")

# Menu
while True:

    print("\n----- Student Management System -----")
    print("1 Add Student")
    print("2 View Students")
    print("3 Search Student")
    print("4 Update Student")
    print("5 Delete Student")
    print("6 Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_student()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        print("Exiting program")
        break

    else:
        print("Invalid choice")
