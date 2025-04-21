#source file for Application

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import ttkbootstrap as ttkb

# Establish database connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Blair@2345',
    database='Project'
)
cursor = conn.cursor()

# Main application window
root = ttkb.Window(themename="minty")  # Try themes like "minty", "darkly", etc.
root.title("Student Course Registration System")
root.geometry("1200x800")

# Function to display all students
def view_students():
    cursor.execute("SELECT * FROM Students")
    records = cursor.fetchall()
    display_result(records, ["ID", "Name", "Email", "Phone"])

# Function to add a new student
def add_student():
    id = entry_id.get()
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    cursor.execute("INSERT INTO Students (Student_id, Name, Email, Phone) VALUES (%s, %s, %s, %s)",
                   (id, name, email, phone))
    conn.commit()
    messagebox.showinfo("Success", "Student added successfully")

# Function to delete a student by ID
def delete_student():
    Student_id = entry_id.get()
    cursor.execute("DELETE FROM Students WHERE student_id = %s", (Student_id,))
    conn.commit()
    messagebox.showinfo("Deleted", f"Student ID {Student_id} deleted")

# Function to search student by name/email
def search_student():
    keyword = entry_search.get()
    cursor.execute("SELECT * FROM Students WHERE name LIKE %s OR email LIKE %s", (f"%{keyword}%", f"%{keyword}%"))
    records = cursor.fetchall()
    display_result(records, ["ID", "Name", "Email", "Phone"])  

# Function to update student info
def update_student():
    student_id = entry_id.get()
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    
    if not student_id:
        messagebox.showwarning("Input Error", "Please enter the Student ID to update.")
        return

    update_query = '''
        UPDATE Students 
        SET name = %s, email = %s, phone = %s
        WHERE student_id = %s
    '''
    cursor.execute(update_query, (name, email, phone, student_id))
    conn.commit()
    messagebox.showinfo("Success", f"Student ID {student_id} updated successfully")


# Function to show student-course join results
def show_enrollments():
    cursor.execute('''
        SELECT Students.Name AS Student, Courses.Name AS Course, Enrollments.Enrollment_date
        FROM Enrollments
        JOIN Students ON Enrollments.Student_id = Students.Student_id
        JOIN Courses ON Enrollments.Course_id = Courses.Course_id
    ''')
    records = cursor.fetchall()
    display_result(records, ["Student", "Course", "Enrollment Date"])

# Function to perform a subquery (e.g., show students not enrolled in any course)
def show_unenrolled_students():
    cursor.execute('''
        SELECT name FROM Students
        WHERE student_id NOT IN (SELECT Student_id FROM Enrollments)
    ''')
    records = cursor.fetchall()
    display_result(records, ["Unenrolled Students"])

# Helper function to display query results in the UI
def display_result(rows, columns):
    for widget in frame_result.winfo_children():
        widget.destroy()
    tree = ttk.Treeview(frame_result, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col, anchor='center')
        tree.column(col, width=150, anchor='center')
    for row in rows:
        tree.insert('', tk.END, values=row)
    tree.pack(fill=tk.BOTH, expand=True)

# UI Elements
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="ID:").grid(row=0, column=0)
entry_id = tk.Entry(frame_input)
entry_id.grid(row=0, column=1)

tk.Label(frame_input, text="Name:").grid(row=1, column=0)
entry_name = tk.Entry(frame_input)
entry_name.grid(row=1, column=1)

tk.Label(frame_input, text="Email:").grid(row=2, column=0)
entry_email = tk.Entry(frame_input)
entry_email.grid(row=2, column=1)

tk.Label(frame_input, text="Phone:").grid(row=3, column=0)
entry_phone = tk.Entry(frame_input)
entry_phone.grid(row=3, column=1)

#Student buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)


tk.Button(frame_buttons, text="Add Student", command=add_student).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Update Student", command=update_student).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Delete Student", command=delete_student).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="View Students", command=view_students).grid(row=0, column=3, padx=6)

tk.Button(frame_buttons, text="Show Enrollments", command=show_enrollments).grid(row=0, column=4, padx=5)
tk.Button(frame_buttons, text="Show Unenrolled Students", command=show_unenrolled_students).grid(row=0, column=5, padx=5)

frame_search = tk.Frame(root)
frame_search.pack(pady=10)

tk.Label(frame_search, text="Search Student:").pack(side=tk.LEFT)
entry_search = tk.Entry(frame_search)
entry_search.pack(side=tk.LEFT)
tk.Button(frame_search, text="Search", command=search_student).pack(side=tk.LEFT, padx=5)

frame_result = tk.Frame(root)
frame_result.pack(fill=tk.BOTH, expand=True, pady=20)

root.mainloop()

# Close DB connection when the app is closed
conn.close()
