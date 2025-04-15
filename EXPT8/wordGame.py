import tkinter as tk
import random

root = tk.Tk()
words = ["pun", "run", "fun", "bun", "tree", "free"]


def shuffle():
    return random.choice(words)


def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


def get():
    user_input = entry.get().lower()
    if user_input == word:
        clear_window()
        win_label = tk.Label(root, text="YOU WIN! 🎉", font=("Aptos", 24))
        win_label.place(relx=0.5, rely=0.5, anchor="center")
    else:
        out = tk.Label(root, text="TRY AGAIN!")
        out.pack()
        root.after(1000, out.destroy)


word = shuffle()

root.title("Word Game")
root.geometry("300x300")

entry = tk.Entry(root, width=20)
entry.place(x=50, y=100)

button = tk.Button(root, text="Guess", command=get)
button.place(x=115, y=150)

root.mainloop()
