import random
import math
import tkinter as tk
def start_game():
    global number, guesses, tries, bottom, top, flag
    bottom = int(entry_bottom.get())
    top = int(entry_top.get())
    number = random.randint(bottom, top)

window=tk.Tk()
window.title("Number Guessing Game")
window.geometry("300x300")
window.configure(bg="white")

title = tk.Label(window, text="Number Guessing Game", bg="white", fg="black", font="Arial 12 bold")
title.pack()

tk.Label(window, text="Enter bottom range", bg="white", fg="black", font="Arial 10").pack()
entry_bottom = tk.Entry(window)
entry_bottom.pack()

tk.Label(window, text="Enter top range", bg="white", fg="black", font="Arial 10").pack()
entry_top = tk.Entry(window)
entry_top.pack()


window.mainloop()
