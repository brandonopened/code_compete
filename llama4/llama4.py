import tkinter as tk
from PIL import Image, ImageTk
import requests

class CatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cat Joke App")

        # Load the cat nose image
        self.cat_nose_image = ImageTk.PhotoImage(Image.open("catnose.png"))
        self.cat_nose_button = tk.Button(self.root, image=self.cat_nose_image, command=self.get_random_joke)
        self.cat_nose_button.pack(pady=20)

        # Label to display the joke
        self.joke_label = tk.Label(self.root, text="", wraplength=400, font=("Arial", 12))
        self.joke_label.pack(padx=20, pady=20)

    def get_random_joke(self):
        try:
            response = requests.get("https://catfact.ninja/fact")
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            joke = data.get("fact", "No joke found")
            self.joke_label.config(text=joke)
        except requests.RequestException as e:
            self.joke_label.config(text=f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CatApp(root)
    root.mainloop()