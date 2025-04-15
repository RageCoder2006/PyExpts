import tkinter as tk
import random

root = tk.Tk()
words = ["pun", "run", "fun", "bun", "tree", "free"]
score = 0

def shuffle():
    return random.choice(words)

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def get():
    global score
    user_input = entry.get().lower()
    if user_input == word:
        score = score + 1
        clear_window()
        win_label = tk.Label(root, text="YOU WIN! 🎉", font=("Aptos", 24))
        win_label.place(relx=0.5, rely=0.4, anchor="center")
        score_label = tk.Label(root, text="Score: " + str(score), font=("Aptos", 14))
        score_label.place(relx=0.5, rely=0.6, anchor="center")
    else:
        feedback_label.config(text="TRY AGAIN!")
        root.after(1000, lambda: feedback_label.config(text=""))

word = shuffle()

root.title("Word Game")
root.geometry("300x300")

label = tk.Label(root, text="GUESS THE WORD", font=("Aptos", 18))
label.place(relx=0.5, rely=0.2, anchor="center")

entry = tk.Entry(root, width=20)
entry.place(x=50, y=100)

button = tk.Button(root, text="Guess", command=get)
button.place(x=115, y=150)

feedback_label = tk.Label(root, text="", font=("Aptos", 12))
feedback_label.place(relx=0.5, rely=0.7, anchor="center")

score_label = tk.Label(root, text="Score: " + str(score), font=("Aptos", 12))
score_label.place(relx=0.5, rely=0.85, anchor="center")

root.mainloop()
