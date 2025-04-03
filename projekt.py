import tkinter as tk
from tkinter import messagebox
import json

# Fil där böckerna sparas
BOOKS_FILE = "books.json"

def ladda_böcker():
    try:
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def spara_bok(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

def gör_bok():
    title = entry_title.get()
    if title:
        books = ladda_böcker()
        if title in books:
            messagebox.showerror("Fel", "Boken finns redan i biblioteket!")
        else:
            books[title] = "Tillgänglig"
            spara_bok(books)
            messagebox.showinfo("Success", f"Boken '{title}' har lagts till.")
            entry_title.delete(0, tk.END)
    else:
        messagebox.showerror("Fel", "Ange en boktitel!")

def låna_bok():
    title = entry_title.get()
    books = ladda_böcker()
    if title in books and books[title] == "Tillgänglig":
        books[title] = "Utlånad"
        spara_bok(books)
        messagebox.showinfo("Success", f"Du har lånat '{title}'.")
    elif title in books:
        messagebox.showerror("Fel", "Boken är redan utlånad!")
    else:
        messagebox.showerror("Fel", "Boken finns inte i biblioteket!")

def lämna_bok():
    title = entry_title.get()
    books = ladda_böcker()
    if title in books and books[title] == "Utlånad":
        books[title] = "Tillgänglig"
        spara_bok(books)
        messagebox.showinfo("Success", f"Du har lämnat tillbaka '{title}'.")
    elif title in books:
        messagebox.showerror("Fel", "Boken är redan tillgänglig!")
    else:
        messagebox.showerror("Fel", "Boken finns inte i biblioteket!")

def sök_bok():
    title = entry_title.get()
    books = ladda_böcker()
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

tk.Button(root, text="Lägg till bok", command=gör_bok).pack()
tk.Button(root, text="Låna bok", command=låna_bok).pack()
tk.Button(root, text="Lämna tillbaka bok", command=lämna_bok).pack()
tk.Button(root, text="Sök bok", command=sök_bok).pack()

root.mainloop()
