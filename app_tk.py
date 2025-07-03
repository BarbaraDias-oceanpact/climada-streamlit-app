import tkinter as tk
from tkinter import scrolledtext
from climada.util import demo

def mostrar_dados():
    hazard = demo.hazard.HazardDemo().get()
    exposure = demo.exposures.ExposuresDemo().get()
    text_area.insert(tk.END, "Hazard demo:\n")
    text_area.insert(tk.END, f"{hazard}\n\n")
    text_area.insert(tk.END, "Exposure demo:\n")
    text_area.insert(tk.END, f"{exposure}\n\n")

root = tk.Tk()
root.title("CLIMADA com Tkinter")

btn = tk.Button(root, text="Mostrar informações dos demos", command=mostrar_dados)
btn.pack(pady=10)

text_area = scrolledtext.ScrolledText(root, width=80, height=25)
text_area.pack(padx=10, pady=10)

root.mainloop()
