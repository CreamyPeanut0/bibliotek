import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Fil där böckerna sparas
BÖCKER_FIL = "books.txt"

def ladda_bok():
    böcker = {}
    try:
        with open(BÖCKER_FIL, "r") as fil:
            for line in fil:
                title, status = line.strip().split(" - ")
                böcker[title] = status
    except FileNotFoundError:
        pass  # Om filen inte finns så startar vi med en tom lista
    return böcker

def spara_bok(böcker):
    with open(BÖCKER_FIL, "w") as fil:
        for titel, status in böcker.items():
            fil.write(f"{titel} - {status}\n")

def uppdatera_bok_lista():
    books = ladda_bok()
    listbox_books.delete(0, tk.END)
    for titel, status in books.items():
        listbox_books.insert(tk.END, f"{titel} - {status}")

def lägg_till_bok():
    titel = entry_title.get()
    if titel:
        böcker = ladda_bok()
        if titel in böcker:
            messagebox.showerror("Fel", "Boken finns redan i biblioteket!")
        else:
            böcker[titel] = "Tillgänglig"
            spara_bok(böcker)
            uppdatera_bok_lista()
            messagebox.showinfo("Success", f"Boken '{titel}' har lagts till.")
            entry_title.delete(0, tk.END)
    else:
        messagebox.showerror("Fel", "Ange en boktitel!")

def låna_bok():
    titel = entry_title.get()
    böcker = ladda_bok()
    if titel in böcker and böcker[titel] == "Tillgänglig":
        böcker[titel] = "Utlånad"
        spara_bok(böcker)
        uppdatera_bok_lista()
        messagebox.showinfo("Success", f"Du har lånat '{titel}'.")
    elif titel in böcker:
        messagebox.showerror("Fel", "Boken är redan utlånad!")
    else:
        messagebox.showerror("Fel", "Boken finns inte i biblioteket!")

def lämna_tillbaka_bok():
    titel = entry_title.get()
    böcker = ladda_bok()
    if titel in böcker and böcker[titel] == "Utlånad":
        böcker[titel] = "Tillgänglig"
        spara_bok(böcker)
        uppdatera_bok_lista()
        messagebox.showinfo("Success", f"Du har lämnat tillbaka '{titel}'.")
    elif titel in böcker:
        messagebox.showerror("Fel", "Boken är redan tillgänglig!")
    else:
        messagebox.showerror("Fel", "Boken finns inte i biblioteket!")

def sök_bok():
    titel = entry_title.get()
    böcker = ladda_bok()
    if titel in böcker:
        messagebox.showinfo("Sökresultat", f"Boken '{titel}' är {böcker[titel]}.")
    else:
        messagebox.showerror("Fel", "Boken finns inte i biblioteket!")

def ta_bort_bok():
    titel = entry_title.get()
    böcker = ladda_bok()
    if titel in böcker:
        del böcker[titel]
        spara_bok(böcker)
        uppdatera_bok_lista()
        messagebox.showinfo("Success", f"Boken '{titel}' har tagits bort.")
    else:
        messagebox.showerror("Fel", "Boken finns inte i biblioteket!")

# Skapa GUI
root = tk.Tk()
root.title("Bibliotekssystem")
root.geometry("900x650")

# Ladda bakgrundsbild
bg_image = Image.open("bokfr.png")

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
