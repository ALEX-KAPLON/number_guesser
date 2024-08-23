import random
import math
import tkinter as tk
from tkinter import mainloop

print("\tNumber guesser game:")

bottom = int(input("Enter bottom range: "))
top = int(input("Enter top range: "))

number = random.randint(bottom, top)
guesses = math.ceil(math.log2(top - bottom + 1))
print("\tYou have", guesses, "guesses to guess the number between", bottom, "and", top)

tries = 0
flag=False
while tries < guesses:
    tries += 1
    guess = int(input("Enter your guess => "))

    if guess == number:
        print("Congratulations! You guessed the number in", tries, "tries.")
        flag=True
        break
    elif guess < number:
        print("Try again! Your guess is too low.")
    else:
        print("Try again! Your guess is too high.")
if not flag:
    print("You have exhausted all your guesses. The number was", number)
window=tk.Tk()
window.title("Number Guesser Game")
window.geometry("500x300")
window.configure(bg="white")
window.mainloop()