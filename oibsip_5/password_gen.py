import random
import string
import pyperclip
from tkinter import messagebox


def generate_password(length, include_uppercase, include_numbers, include_symbols):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def copy_to_clipboard(password):
    pyperclip.copy(password)
    messagebox.showinfo("Password Generator", "Password copied to clipboard!")
