#source file for Application

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import ttkbootstrap as ttkb

root = ttkb.Window(themename="flatly")  # Try themes like "minty", "darkly", etc.


# # Establish database connection
# conn = mysql.connector.connect(
#     host='localhost',
#     user='your_username',
#     password='your_password',
#     database='your_database'
# )
# cursor = conn.cursor()

# # Main application window
# root = tk.Tk()
# root.title("Student Course Registration System")
# root.geometry("800x600")

# # Function to display all students
# def view_students():
#     cursor.execute("SELECT * FROM Students")
#     records = cursor.fetchall()
#     display_result(records, ["ID", "Name", "Email", "Phone", "Address"])

# # Function to add a new student
# def add_student():
#     name = entry_name.get()
#     email = entry_email.get()
#     phone = entry_phone.get()
#     address = entry_address.get()
#     cursor.execute("INSERT INTO Students (name, email, phone, address) VALUES (%s, %s, %s, %s)",
#                    (name, email, phone, address))
#     conn.commit()
#     messagebox.showinfo("Success", "Student added successfully")

# # Function to delete a student by ID
# def delete_student():
#     student_id = entry_id.get()
#     cursor.execute("DELETE FROM Students WHERE student_id = %s", (student_id,))
#     conn.commit()
#     messagebox.showinfo("Deleted", f"Student ID {student_id} deleted")

# # Function to show student-course join results
# def show_enrollments():
#     cursor.execute('''
#         SELECT Students.name AS Student, Courses.course_name AS Course, Enrollments.enrollment_date
#         FROM Enrollments
#         JOIN Students ON Enrollments.student_id = Students.student_id
#         JOIN Courses ON Enrollments.course_id = Courses.course_id
#     ''')
#     records = cursor.fetchall()
#     display_result(records, ["Student", "Course", "Enrollment Date"])

# # Function to perform a subquery (e.g., show students not enrolled in any course)
# def show_unenrolled_students():
#     cursor.execute('''
#         SELECT name FROM Students
#         WHERE student_id NOT IN (SELECT student_id FROM Enrollments)
#     ''')
#     records = cursor.fetchall()
#     display_result(records, ["Unenrolled Students"])

# # Helper function to display query results in the UI
# def display_result(rows, columns):
#     for widget in frame_result.winfo_children():
#         widget.destroy()
#     tree = ttk.Treeview(frame_result, columns=columns, show='headings')
#     for col in columns:
#         tree.heading(col, text=col)
#         tree.column(col, width=150)
#     for row in rows:
#         tree.insert('', tk.END, values=row)
#     tree.pack(fill=tk.BOTH, expand=True)

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

tk.Label(frame_input, text="Address:").grid(row=4, column=0)
entry_address = tk.Entry(frame_input)
entry_address.grid(row=4, column=1)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Add Student").grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="View Students").grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Delete Student").grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Show Enrollments").grid(row=0, column=3, padx=5)
tk.Button(frame_buttons, text="Show Unenrolled Students").grid(row=0, column=4, padx=5)

frame_result = tk.Frame(root)
frame_result.pack(fill=tk.BOTH, expand=True, pady=20)

root.mainloop()

# Close DB connection when the app is closed
conn.close()
