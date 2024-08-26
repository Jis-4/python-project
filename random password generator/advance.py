import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = int(length_entry.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Warning", "You must select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Set up the main window
root = tk.Tk()
root.title("Random Password Generator")

# Password length label and entry
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Character type checkboxes
letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Letters", variable=letters_var).grid(row=1, column=0, sticky='w', padx=10)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=2, column=0, sticky='w', padx=10)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, sticky='w', padx=10)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Password display entry
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Copy to clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=6, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
