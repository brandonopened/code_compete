import tkinter as tk
from tkinter import messagebox
import requests
import os
from PIL import Image, ImageTk

class CatFactsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cat Facts")
        self.root.geometry("400x400")
        
        # Load the cat nose image
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "catnose.png")
        
        # Open and resize the image
        cat_image = Image.open(image_path)
        cat_image = cat_image.resize((200, 200))
        self.cat_photo = ImageTk.PhotoImage(cat_image)
        
        # Create a label to display the image
        self.image_label = tk.Label(root, image=self.cat_photo, cursor="hand2")
        self.image_label.pack(pady=20)
        self.image_label.bind("<Button-1>", self.get_cat_fact)
        
        # Create a label for instructions
        self.instruction_label = tk.Label(
            root, 
            text="Click on the cat nose to get a random cat fact!",
            font=("Arial", 12)
        )
        self.instruction_label.pack(pady=10)
        
        # Create a text widget to display the fact
        self.fact_text = tk.Text(root, height=5, width=40, wrap=tk.WORD, font=("Arial", 10))
        self.fact_text.pack(pady=10, padx=20)
        self.fact_text.config(state=tk.DISABLED)
        
    def get_cat_fact(self, event=None):
        try:
            # Make API request to get a random cat fact
            response = requests.get("https://catfact.ninja/fact")
            response.raise_for_status()
            
            # Extract the fact from the JSON response
            data = response.json()
            fact = data.get("fact", "No fact available")
            
            # Update the text widget with the new fact
            self.fact_text.config(state=tk.NORMAL)
            self.fact_text.delete(1.0, tk.END)
            self.fact_text.insert(tk.END, fact)
            self.fact_text.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to get cat fact: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CatFactsApp(root)
    root.mainloop()