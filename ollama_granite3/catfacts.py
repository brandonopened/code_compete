import tkinter as tk
import requests
import random

def get_random_fact():
    response = requests.get('https://catfact.ninja/api/facts')
    data = response.json()
    random_fact = random.choice(data['all_cats_facts'])
    joke = random_fact[1]
    label.config(text=f"{joke}\n\nImage: catnose.png")

root = tk.Tk()
root.title("Cat Fact App")

button = tk.Button(root, text="Click for a Cat Joke", command=get_random_fact)
button.pack(pady=20)

label = tk.Label(root, text="", wraplength=400, justify='left', font=("Arial", 12))
label.pack(pady=20)

root.mainloop()