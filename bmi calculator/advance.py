import tkinter as tk
from tkinter import messagebox
import json
import os

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Function to categorize BMI
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Function to save BMI data
def save_bmi_data(name, bmi):
    data = {}
    filename = "bmi_data.json"

    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)

    if name in data:
        data[name].append(bmi)
    else:
        data[name] = [bmi]

    with open(filename, 'w') as file:
        json.dump(data, file)

# Function to calculate and display BMI
def calculate_and_display_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        name = entry_name.get()
        
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        
        result_label.config(text=f"BMI: {bmi:.2f} ({category})")
        save_bmi_data(name, bmi)

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")

# Function to show historical data
def show_history():
    filename = "bmi_data.json"
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            name = entry_name.get()
            if name in data:
                history = "\n".join([f"BMI: {b:.2f}" for b in data[name]])
                messagebox.showinfo("BMI History", f"History for {name}:\n{history}")
            else:
                messagebox.showinfo("No Data", f"No data found for {name}.")
    else:
        messagebox.showinfo("No Data", "No historical data found.")

# Setting up the GUI
root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Weight (kg):").grid(row=1, column=0)
entry_weight = tk.Entry(root)
entry_weight.grid(row=1, column=1)

tk.Label(root, text="Height (m):").grid(row=2, column=0)
entry_height = tk.Entry(root)
entry_height.grid(row=2, column=1)

tk.Button(root, text="Calculate BMI", command=calculate_and_display_bmi).grid(row=3, column=0, columnspan=2)
result_label = tk.Label(root, text="BMI: ")
result_label.grid(row=4, column=0, columnspan=2)

tk.Button(root, text="Show History", command=show_history).grid(row=5, column=0, columnspan=2)

root.mainloop()
