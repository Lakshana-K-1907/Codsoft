import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Recursive GUI Calculator")

# Global variable to store current result for continued calculations
current_result = None

# Function to perform the calculation
def perform_calculation():
    global current_result
    
    try:
        # Get numbers from input fields
        if current_result is not None and use_result_var.get():
            num1 = current_result
        else:
            num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        operation = operation_var.get()

        # Perform operation based on user choice
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        elif operation == '//':
            result = num1 // num2
        elif operation == '%':
            result = num1 % num2
        elif operation == '^':
            result = pow(num1, num2)
        else:
            messagebox.showerror("Invalid Input", "Choose a valid operation.")
            return

        current_result = result  # Store the result for further operations
        label_result.config(text=f"Result: {result}")
        ask_continue()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division by zero is not allowed.")

# Function to ask the user if they want to continue
def ask_continue():
    response = messagebox.askyesno("Continue?", "Do you want to continue the calculation?")
    if response:
        response_same = messagebox.askyesno("Continue with same result?", "Continue with same result as number 1?")
        use_result_var.set(response_same)
        entry_num1.delete(0, tk.END)
        entry_num2.delete(0, tk.END)
        if not response_same:
            global current_result
            current_result = None
    else:
        messagebox.showinfo("End", f"Final Result: {current_result}")
        root.quit()

# --- UI ELEMENTS ---

# Entry for first number
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

# Entry for second number
tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

# Dropdown menu to select operation
tk.Label(root, text="Choose operation:").grid(row=2, column=0, padx=10, pady=5)
operation_var = tk.StringVar()
operation_var.set('+')  # Default operation
operation_menu = tk.OptionMenu(root, operation_var, '+', '-', '*', '/', '//', '%', '^')
operation_menu.grid(row=2, column=1, padx=10, pady=5)

# Button to perform calculation
calculate_btn = tk.Button(root, text="Calculate", command=perform_calculation)
calculate_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Checkbox to indicate use of previous result
use_result_var = tk.BooleanVar()
use_result_checkbox = tk.Checkbutton(root, text="Use previous result as number 1", variable=use_result_var)
use_result_checkbox.grid(row=4, column=0, columnspan=2)

# Label to display result
label_result = tk.Label(root, text="Result:")
label_result.grid(row=5, column=0, columnspan=2, pady=10)

# Run the GUI loop
root.mainloop()
