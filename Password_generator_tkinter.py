import tkinter as tk
from tkinter import messagebox
import random
import string

def list_of_pass():
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    digits = list(string.digits)
    special_characters = list(string.punctuation)
    lst = lowercase + uppercase + digits + special_characters
    return lst

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Length must be a positive integer")
            return

        lst1 = list_of_pass()
        random.shuffle(lst1)
        passcode = random.choices(lst1, k=length)
        password = ''.join(passcode)
        password_display.delete(0, tk.END)
        password_display.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def copy_password():
    window.clipboard_clear()
    window.clipboard_append(password_display.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x250")
window.resizable(False, False)

# Widgets
tk.Label(window, text="Password Length:", font=("Arial", 12)).pack(pady=10)
length_entry = tk.Entry(window, font=("Arial", 12))
length_entry.pack(pady=5)

generate_btn = tk.Button(window, text="Generate Password", font=("Arial", 12), command=generate_password)
generate_btn.pack(pady=10)

password_display = tk.Entry(window, font=("Arial", 12), width=30)
password_display.pack(pady=5)

copy_btn = tk.Button(window, text="Copy to Clipboard", font=("Arial", 12), command=copy_password)
copy_btn.pack(pady=10)

# Run the GUI loop
window.mainloop()
