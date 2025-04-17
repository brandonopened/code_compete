import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
import io
from urllib.request import urlopen

class CatFactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cat Facts")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Load and display cat nose image
        self.cat_nose_image = Image.open("catnose.png")
        self.cat_nose_image = self.cat_nose_image.resize((200, 200), Image.Resampling.LANCZOS)
        self.cat_nose_photo = ImageTk.PhotoImage(self.cat_nose_image)
        
        self.cat_nose_button = ttk.Button(
            self.main_frame,
            image=self.cat_nose_photo,
            command=self.get_cat_fact
        )
        self.cat_nose_button.grid(row=0, column=0, pady=20)
        
        # Create text area for cat fact
        self.fact_text = tk.Text(
            self.main_frame,
            wrap=tk.WORD,
            width=40,
            height=10,
            font=("Arial", 12)
        )
        self.fact_text.grid(row=1, column=0, pady=20)
        self.fact_text.config(state=tk.DISABLED)
        
        # Add click instruction
        self.instruction = ttk.Label(
            self.main_frame,
            text="Click the cat nose for a random cat fact!",
            font=("Arial", 10)
        )
        self.instruction.grid(row=2, column=0, pady=10)
        
    def get_cat_fact(self):
        try:
            response = requests.get("https://catfact.ninja/fact")
            if response.status_code == 200:
                fact = response.json()["fact"]
                self.fact_text.config(state=tk.NORMAL)
                self.fact_text.delete(1.0, tk.END)
                self.fact_text.insert(tk.END, fact)
                self.fact_text.config(state=tk.DISABLED)
            else:
                self.show_error("Failed to fetch cat fact")
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
    
    def show_error(self, message):
        self.fact_text.config(state=tk.NORMAL)
        self.fact_text.delete(1.0, tk.END)
        self.fact_text.insert(tk.END, message)
        self.fact_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = CatFactApp(root)
    root.mainloop() 