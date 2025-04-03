import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Fil där böckerna sparas
BOOKS_FILE = "books.txt"

def ladda_bok():
    böcker = {}
    try:
        with open(BOOKS_FILE, "r") as file:
            for line in file:
                title, status = line.strip().split(" - ")
                böcker[title] = status
    except FileNotFoundError:
        pass  # Om filen inte finns så startar vi med en tom lista
    return böcker

def spara_bok(böcker):
    with open(BOOKS_FILE, "w") as file:
        for title, status in böcker.items():
            file.write(f"{title} - {status}\n")

def uppdatera_bok_lista():
    books = ladda_bok()
    listbox_books.delete(0, tk.END)
    for title, status in books.items():
        listbox_books.insert(tk.END, f"{title} - {status}")

def lägg_till_bok():
    title = entry_title.get()
    if title:
        böcker = ladda_bok()
        if title in böcker:
            messagebox.showerror("Fel", "Boken finns redan i biblioteket!")
        else:
            böcker[title] = "Tillgänglig"
            spara_bok(böcker)
            uppdatera_bok_lista()
            messagebox.showinfo("Success", f"Boken '{title}' har lagts till.")
            entry_title.delete(0, tk.END)
    else:
        messagebox.showerror("Fel", "Ange en boktitel!")

def låna_bok():
    title = entry_title.get()
    böcker = ladda_bok()
    if title in böcker and böcker[title] == "Tillgänglig":
        böcker[title] = "Utlånad"
        spara_bok(böcker)
        uppdatera_bok_lista()
        messagebox.showinfo("Success", f"Du har lånat '{title}'.")
    elif title in böcker:
        messagebox.showerror("Fel", "Boken är redan utlånad!")
    else:
        messagebox.showerror("Fel", "Boken finns inte i biblioteket!")

def lämna_tillbaka_bok():
    title = entry_title.get()
    böcker = ladda_bok()
    if title in böcker and böcker[title] == "Utlånad":
        böcker[title] = "Tillgänglig"
        spara_bok(böcker)
        uppdatera_bok_lista()
        messagebox.showinfo("Success", f"Du har lämnat tillbaka '{title}'.")
    elif title in böcker:
        messagebox.showerror("Fel", "Boken är redan tillgänglig!")
    else:
        messagebox.showerror("Fel", "Boken finns inte i biblioteket!")

def sök_bok():
    title = entry_title.get()
    böcker = ladda_bok()
    if title in böcker:
        messagebox.showinfo("Sökresultat", f"Boken '{title}' är {böcker[title]}.")
    else:
        messagebox.showerror("Fel", "Boken finns inte i biblioteket!")

def ta_bort_bok():
    title = entry_title.get()
    böcker = ladda_bok()
    if title in böcker:
        del böcker[title]
        spara_bok(böcker)
        uppdatera_bok_lista()
        messagebox.showinfo("Success", f"Boken '{title}' har tagits bort.")
    else:
        messagebox.showerror("Fel", "Boken finns inte i biblioteket!")

# Skapa GUI
root = tk.Tk()
root.title("Bibliotekssystem")
root.geometry("900x600")

# Ladda bakgrundsbild
bg_image = Image.open("böcker.jpg")  # Ange sökvägen till din bild här

bg_photo = ImageTk.PhotoImage(bg_image)

# Skapa en label för att visa bakgrundsbilden
background_label = tk.Label(root, image=bg_photo)
background_label.place(relwidth=1, relheight=1)  # Placera bakgrunden över hela fönstret

frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=10, pady=10)

frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT, padx=10, pady=10)

tk.Label(frame_left, text="Boktitel:").pack()
entry_title = tk.Entry(frame_left)
entry_title.pack()

tk.Button(frame_left, text="Lägg till bok", command=lägg_till_bok).pack()
tk.Button(frame_left, text="Ta bort bok", command=ta_bort_bok).pack()
tk.Button(frame_left, text="Låna bok", command=låna_bok).pack()
tk.Button(frame_left, text="Lämna tillbaka bok", command=lämna_tillbaka_bok).pack()
tk.Button(frame_left, text="Sök bok", command=sök_bok).pack()


tk.Label(frame_right, text="Alla böcker:").pack()
listbox_books = tk.Listbox(frame_right, width=50, height=10)
listbox_books.pack()

uppdatera_bok_lista()

root.mainloop()
