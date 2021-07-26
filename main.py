import tkinter as tk
import math
import datetime as dt

text = None
text_entry = None

# ---------------------- Functions ----------------------- #

def begin():
    global text_entry, text
    start.destroy()

    text_entry = tk.Entry(font=('Arial', 12), width=100)
    text_entry.grid(column=1, row=2, padx=10, pady=10)

    text = text_entry.get()
    window.after(5000, check)

def check():
    global text
    if text == text_entry.get():
        text_entry.delete(0,'end')
        save()
        window.after(5000, check)
    else:
        window.after(5000, check)
    text = text_entry.get()
    
def save():
    global text
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
    with open(f"./{timestamp}.txt", 'w') as file:
        file.write(text)


# ------------------------- UI --------------------------- #

window = tk.Tk()
window.title("Disappearing Text")
window.config(padx=20, pady=20)

# Labels
title_label = tk.Label(text='Disappearing Text', font=('Arial',30))
title_label.grid(column=1, row=0)

subtitle_label = tk.Label(text='Type away, once you stop for 5 seconds, the text will vanish.', font=('Arial', 15))
subtitle_label.grid(column=1, row=1)

# Button
start = tk.Button(text='Click to start!', command=begin)
start.grid(column=1, row=3)

window.mainloop()