import sqlite3

# ---------- Database Connection ----------
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# ---------- Create Table ----------
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    marks REAL
)
""")
conn.commit()

# ---------- Functions ----------
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    cursor.execute(
        "INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)",
        (name, age, course, marks)
    )
    conn.commit()
    print("✅ Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\n--- Student Records ---")
    if len(rows) == 0:
        print("No records found.")
    else:
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]} | Marks: {row[4]}")

def update_student():
    sid = int(input("Enter student ID to update: "))
    new_marks = float(input("Enter new marks: "))

    cursor.execute("UPDATE students SET marks=? WHERE id=?", (new_marks, sid))
    conn.commit()

    if cursor.rowcount == 0:
        print("❌ Student ID not found.")
    else:
        print("✅ Student updated successfully!")

def delete_student():
    sid = int(input("Enter student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id=?", (sid,))
    conn.commit()

    if cursor.rowcount == 0:
        print("❌ Student ID not found.")
    else:
        print("✅ Student deleted successfully!")

# ---------- Main Menu ----------
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank you! Exiting...")
        break
    else:
        print("❌ Invalid choice. Try again.")

conn.close()
