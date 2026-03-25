import sqlite3

# Database setup
def init_db():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER CHECK(age > 0),
            department TEXT NOT NULL,
            salary REAL CHECK(salary >= 0)
        )
    """)
    conn.commit()
    conn.close()

# Add employee
def add_employee(name, age, department, salary):
    try:
        conn = sqlite3.connect("employees.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employees (name, age, department, salary) VALUES (?, ?, ?, ?)",
                       (name, age, department, salary))
        conn.commit()
        print("Employee added successfully.")
    except Exception as e:
        print(" Error adding employee:", e)
    finally:
        conn.close()

# View all employees
def view_employees():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()
    if rows:
        print("\n Employee List:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Dept: {row[3]}, Salary: ₹{row[4]:.2f}")
    else:
        print(" No employees found.")

# Search employee by name
def search_employee(name):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Dept: {row[3]}, Salary: ₹{row[4]:.2f}")
    else:
        print("No matching employee found.")

# Update employee
def update_employee(emp_id, name=None, age=None, department=None, salary=None):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
    if not cursor.fetchone():
        print("⚠ Employee not found.")
        conn.close()
        return

    if name:
        cursor.execute("UPDATE employees SET name=? WHERE id=?", (name, emp_id))
    if age:
        cursor.execute("UPDATE employees SET age=? WHERE id=?", (age, emp_id))
    if department:
        cursor.execute("UPDATE employees SET department=? WHERE id=?", (department, emp_id))
    if salary:
        cursor.execute("UPDATE employees SET salary=? WHERE id=?", (salary, emp_id))

    conn.commit()
    conn.close()
    print("Employee updated successfully.")

# Delete employee
def delete_employee(emp_id):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id=?", (emp_id,))
    conn.commit()
    conn.close()
    print("Employee deleted successfully.")

# Menu
def menu():
    while True:
        print("\n=== Employee Management System ===")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            name = input("Enter name: ").strip()
            try:
                age = int(input("Enter age: "))
                salary = float(input("Enter salary: "))
            except ValueError:
                print("Invalid age or salary.")
                continue
            department = input("Enter department: ").strip()
            add_employee(name, age, department, salary)
        elif choice == "2":
            view_employees()
        elif choice == "3":
            name = input("Enter name to search: ").strip()
            search_employee(name)
        elif choice == "4":
            try:
                emp_id = int(input("Enter employee ID to update: "))
            except ValueError:
                print(" Invalid ID.")
                continue
            name = input("Enter new name (leave blank to skip): ").strip() or None
            age = input("Enter new age (leave blank to skip): ").strip()
            age = int(age) if age else None
            department = input("Enter new department (leave blank to skip): ").strip() or None
            salary = input("Enter new salary (leave blank to skip): ").strip()
            salary = float(salary) if salary else None
            update_employee(emp_id, name, age, department, salary)
        elif choice == "5":
            try:
                emp_id = int(input("Enter employee ID to delete: "))
            except ValueError:
                print(" Invalid ID.")
                continue
            delete_employee(emp_id)
        elif choice == "6":
            print("👋 Exiting Employee Management System.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    init_db()
    menu()

