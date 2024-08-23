import random
import math
import tkinter as tk
def start_game():
    global number, guesses, tries, bottom, top, flag
    bottom = int(entry_bottom.get())
    top = int(entry_top.get())
    number = random.randint(bottom, top)
    guesses = round(math.log(top - bottom + 1, 2))
    tries = 0
    flag = False

    result.config(text=f"You have {guesses} guesses to find the number between {bottom} and {top}")
    entry_guess.config(state=tk.NORMAL)
    guess_button.config(state=tk.NORMAL)
    start_game_button.config(state=tk.DISABLED)
def check_guess():
    global number, guesses, tries, bottom, top, flag
    tries += 1
    guess = int(entry_guess.get())
    if guess == number:
        result.config(text=f"Congratulations! You found the number in {tries} tries")
        entry_guess.config(state=tk.DISABLED)
        guess_button.config(state=tk.DISABLED)
        start_game_button.config(state=tk.NORMAL)
    elif guess < number:
        result.config(text=f"Try a higher number. You have {guesses - tries} guesses left")
    else:
        result.config(text=f"Try a lower number. You have {guesses - tries} guesses left")
    if tries > guesses:
        result.config(text=f"Game Over! The number was {number}")
        entry_guess.config(state=tk.DISABLED)
        guess_button.config(state=tk.DISABLED)
        start_game_button.config(state=tk.NORMAL)
        flag = True




window=tk.Tk()
window.title("Number Guessing Game")
window.state("zoomed")
window.configure(bg="white")

title = tk.Label(window, text="Number Guessing Game", bg="white", fg="black", font="Arial 15 bold")
title.pack()

tk.Label(window, text="Enter bottom range", bg="white", fg="black", font="Arial 10").pack()
entry_bottom = tk.Entry(window)
entry_bottom.pack()

tk.Label(window, text="Enter top range", bg="white", fg="black", font="Arial 10").pack()
entry_top = tk.Entry(window)
entry_top.pack()

start_game_button = tk.Button(window, text="Start Game", bg="black", fg="white", font="Arial 10", command=start_game)
start_game_button.pack()

tk.Label(window, text="↓↓↓Enter your guess ↓↓↓ ", bg="white", fg="black", font="Arial 10").pack()
entry_guess = tk.Entry(window, state=tk.DISABLED)
entry_guess.pack()

guess_button = tk.Button(window, text="Guess", bg="black", fg="white", font="Arial 10", command=check_guess, state=tk.DISABLED)
guess_button.pack()

result = tk.Label(window, text="", bg="white", fg="black", font="Arial 10")
result.pack()

leave_button = tk.Button(window, text="Leave Game", bg="red", fg="white", font="Arial 15 bold", command=window.destroy)
leave_button.pack()

window.mainloop()
