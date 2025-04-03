import tkinter as tk
from tkinter import messagebox
import json

# Fil där böckerna sparas
BOOKS_FILE = "books.json"

def load_books():
    try:
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    title = entry_title.get()
    if title:
        books = load_books()
        if title in books:
            messagebox.showerror("Fel", "Boken finns redan i biblioteket!")
        else:
            books[title] = "Tillgänglig"
            save_books(books)
            messagebox.showinfo("Success", f"Boken '{title}' har lagts till.")
            entry_title.delete(0, tk.END)
    else:
        messagebox.showerror("Fel", "Ange en boktitel!")

def borrow_book():
    title = entry_title.get()
    books = load_books()
    if title in books and books[title] == "Tillgänglig":
        books[title] = "Utlånad"
        save_books(books)
        messagebox.showinfo("Success", f"Du har lånat '{title}'.")
    elif title in books:
        messagebox.showerror("Fel", "Boken är redan utlånad!")
    else:
        messagebox.showerror("Fel", "Boken finns inte i biblioteket!")

def return_book():
    title = entry_title.get()
    books = load_books()
    if title in books and books[title] == "Utlånad":
        books[title] = "Tillgänglig"
        save_books(books)
        messagebox.showinfo("Success", f"Du har lämnat tillbaka '{title}'.")
    elif title in books:
        messagebox.showerror("Fel", "Boken är redan tillgänglig!")
    else:
        messagebox.showerror("Fel", "Boken finns inte i biblioteket!")

def search_book():
    title = entry_title.get()
    books = load_books()
    if title in books:
        messagebox.showinfo("Sökresultat", f"Boken '{title}' är {books[title]}.")
    else:
        messagebox.showerror("Fel", "Boken finns inte i biblioteket!")

# Skapa GUI
root = tk.Tk()
root.title("Bibliotekssystem")
root.geometry("400x300")

tk.Label(root, text="Boktitel:").pack()
entry_title = tk.Entry(root)
entry_title.pack()

tk.Button(root, text="Lägg till bok", command=add_book).pack()
tk.Button(root, text="Låna bok", command=borrow_book).pack()
tk.Button(root, text="Lämna tillbaka bok", command=return_book).pack()
tk.Button(root, text="Sök bok", command=search_book).pack()

root.mainloop()
