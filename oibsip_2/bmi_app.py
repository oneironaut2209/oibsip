import tkinter as tk
from tkinter import ttk, messagebox
from bmi_calculator import calculate_bmi

def on_calculate_bmi():
    weight = entry_weight.get()
    height = entry_height.get()
    try:
        bmi, category = calculate_bmi(weight, height)
        result_text.set(f"Your BMI: {bmi}\nCategory: {category}")
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x300")
root.resizable(True, True)

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.theme_use('clam')

label_weight = ttk.Label(root, text="Enter your weight (kg):")
label_weight.pack(pady=5)
entry_weight = ttk.Entry(root)
entry_weight.pack(pady=5)

label_height = ttk.Label(root, text="Enter your height (cm):")
label_height.pack(pady=5)
entry_height = ttk.Entry(root)
entry_height.pack(pady=5)

button_calculate = ttk.Button(root, text="Calculate BMI", command=on_calculate_bmi)
button_calculate.pack(pady=20)

result_text = tk.StringVar()
label_result = ttk.Label(root, textvariable=result_text)
label_result.pack(pady=20)

root.mainloop()
