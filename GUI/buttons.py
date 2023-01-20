import tkinter as tk
import sys
sys.path.append('../adaptive_math_game')
import division_module, subtraction_module, addition_module, multiplication_module

def on_button_click_m():
    multiplication_module.multiplication()

def on_button_click_s():
    subtraction_module.subtraction()

def on_button_click_d():
    division_module.division()

def on_button_click_a():
    addition_module.addit()

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
