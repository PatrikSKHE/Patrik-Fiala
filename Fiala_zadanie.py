import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Knižnica na prácu s obrázkami
import matplotlib.pyplot as plt

# Funkcia na generovanie náhodných čísel
def generuj_cisla(pocet, min_hodnota, max_hodnota):
    return [random.randint(min_hodnota, max_hodnota) for _ in range(pocet)]

# Funkcia na výpočet štatistík
def vypocitaj_statistiky(cisla):
    najvacsie = max(cisla)
    najmensie = min(cisla)
    priemer = sum(cisla) / len(cisla)
    return najvacsie, najmensie, priemer

# Funkcia na vykreslenie grafu
def vykresli_graf(cisla):
    plt.bar(range(1, len(cisla) + 1), cisla)
    plt.show()

# Funkcia spustená tlačidlom
def spusti_program():
    min_hodnota = int(min_entry.get())  # Získa minimálnu hodnotu
    max_hodnota = int(max_entry.get())  # Získa maximálnu hodnotu
    pocet_cisel = 25
    cisla = generuj_cisla(pocet_cisel, min_hodnota, max_hodnota)

    # Výpočet štatistík
    najvacsie, najmensie, priemer = vypocitaj_statistiky(cisla)

    # Zobrazenie výsledkov
    vysledky = f"Čísla: {cisla}\nNajväčšie číslo: {najvacsie}\nNajmenšie číslo: {najmensie}\nPriemer: {priemer:.2f}"
    messagebox.showinfo("Výsledky", vysledky)

    # Vykreslenie grafu
    vykresli_graf(cisla)

# Vytvorenie hlavného okna
root = tk.Tk()
root.title("Generátor náhodných čísel")
root.geometry("400x400")  # Nastavenie veľkosti okna

# Načítanie obrázka na pozadie
bg_image = Image.open("windowsxp.jpg")  # Načítanie obrázka
bg_photo = ImageTk.PhotoImage(bg_image.resize((400, 400)))  # Úprava veľkosti obrázka

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack(fill="both", expand=True)

# Pridanie obrázka na pozadie
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Základné informácie
meno_label = tk.Label(root, text="Patrik Fiala", font=("Arial", 12), bg="white")
meno_label.place(x=160, y=20)  # Umiestnenie na pozadí

predmet_label = tk.Label(root, text="Programovacie techniky", font=("Arial", 12), bg="white")
predmet_label.place(x=110, y=50)

zadanie_label = tk.Label(root, text="Zadanie úlohy: 4", font=("Arial", 12), bg="white")
zadanie_label.place(x=140, y=80)

# Polia na zadanie minimálnej a maximálnej hodnoty
min_label = tk.Label(root, text="Minimálna hodnota:", font=("Arial", 12), bg="white")
min_label.place(x=20, y=150)

min_entry = tk.Entry(root, font=("Arial", 12))
min_entry.place(x=200, y=150)
min_entry.insert(0, "100")  # Prednastavená hodnota

max_label = tk.Label(root, text="Maximálna hodnota:", font=("Arial", 12), bg="white")
max_label.place(x=20, y=190)

max_entry = tk.Entry(root, font=("Arial", 12))
max_entry.place(x=200, y=190)
max_entry.insert(0, "1000")  # Prednastavená hodnota

# Tlačidlo na spustenie programu
spustit_button = tk.Button(root, text="Spusti program", command=spusti_program, font=("Arial", 12), bg="lightblue")
spustit_button.place(x=140, y=300)

# Spustenie GUI
root.mainloop()