import tkinter as tk
from adaptive_math import division, subtraction, addition, multiplication

def on_button_click_m():
    multiplication()

def on_button_click_s():
    subtraction()

def on_button_click_d():
    division()

def on_button_click_a():
    addition()

# Create the main window
window = tk.Tk()
window.title("My GUI")

# Create a button
button = tk.Button(text=" × ", command=on_button_click_m)
button.pack()

button = tk.Button(text=" ÷ ", command=on_button_click_m)
button.pack()

button = tk.Button(text=" + ", command=on_button_click_m)
button.pack()

button = tk.Button(text=" - ", command=on_button_click_m)
button.pack()

# Run the Tkinter event loop
window.mainloop()
