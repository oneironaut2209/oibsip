import tkinter as tk
from tkinter import ttk
from password_gen import generate_password, copy_to_clipboard


def on_generate_password():
    length = int(length_var.get())
    include_uppercase = uppercase_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()

    password = generate_password(
        length, include_uppercase, include_numbers, include_symbols
    )
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


root = tk.Tk()
root.title("Password Generator")

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.theme_use("clam")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky="nsew")

frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=0)
frame.rowconfigure(2, weight=0)
frame.rowconfigure(3, weight=0)
frame.rowconfigure(4, weight=0)
frame.rowconfigure(5, weight=0)

ttk.Label(frame, text="Password Length:").grid(row=0, column=0, pady=5, sticky="w")
length_var = tk.StringVar(value="12")
ttk.Entry(frame, textvariable=length_var).grid(row=0, column=1, pady=5, sticky="ew")

uppercase_var = tk.BooleanVar(value=True)
ttk.Checkbutton(frame, text="Include Uppercase Letters", variable=uppercase_var).grid(
    row=1, column=0, columnspan=2, pady=5, sticky="w"
)

numbers_var = tk.BooleanVar(value=True)
ttk.Checkbutton(frame, text="Include Numbers", variable=numbers_var).grid(
    row=2, column=0, columnspan=2, pady=5, sticky="w"
)

symbols_var = tk.BooleanVar(value=True)
ttk.Checkbutton(frame, text="Include Symbols", variable=symbols_var).grid(
    row=3, column=0, columnspan=2, pady=5, sticky="w"
)

ttk.Button(frame, text="Generate Password", command=on_generate_password).grid(
    row=4, column=0, columnspan=2, pady=20, sticky="ew"
)

password_entry = ttk.Entry(frame, font=("Helvetica", 12))
password_entry.grid(row=5, column=0, columnspan=2, pady=5, sticky="ew")

ttk.Button(
    frame,
    text="Copy to Clipboard",
    command=lambda: copy_to_clipboard(password_entry.get()),
).grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()
