import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Login")
root.geometry("300x200")

# Predefined credentials (for demonstration)
USERNAME = "admin"
PASSWORD = "password123"

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == USERNAME and password == PASSWORD:
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Invalid Credentials")

# Labels and entries for username and password
tk.Label(root, text="Username").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

# Run the application
root.mainloop()
