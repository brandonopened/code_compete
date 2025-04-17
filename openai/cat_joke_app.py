"""
A simple Tkinter GUI app that fetches and displays a random cat fact
from the Cat Fact API (https://catfact.ninja/fact) when the user clicks
on the cat nose image. Requires Python 3, tkinter, and requests.
Place catnose.png in the same directory as this script.
"""
import sys
import tkinter as tk
from tkinter import messagebox
import requests

def fetch_fact():
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("fact", "No fact found.")
    except Exception as e:
        return f"Error fetching fact: {e}"

def on_image_click(event):
    fact = fetch_fact()
    fact_label.config(text=fact)

def main():
    root = tk.Tk()
    root.title("Cat Nose Random Fact")

    try:
        cat_img = tk.PhotoImage(file="catnose.png")
    except tk.TclError as e:
        messagebox.showerror("Image Load Error",
                             f"Could not load image 'catnose.png'.\n{e}")
        sys.exit(1)

    image_label = tk.Label(root, image=cat_img)
    image_label.pack(padx=10, pady=10)
    image_label.bind("<Button-1>", on_image_click)

    global fact_label
    fact_label = tk.Label(root, text="Click the cat nose!", wraplength=300, justify="center")
    fact_label.pack(padx=10, pady=(0, 10))

    root.mainloop()

if __name__ == "__main__":
    main()