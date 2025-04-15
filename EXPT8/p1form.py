import tkinter as tk

root = tk.Tk()
root.title("Form")
root.geometry("300x250")

def validate():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()

    if not name:
        result_label.config(text="Name is required.")
    elif "@" not in email or "." not in email:
        result_label.config(text="Invalid email.")
    elif not age.isdigit():
        result_label.config(text="Age must be a number.")
    else:
        result_label.config(text="All inputs are valid! ✅")

tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email:").pack(pady=5)
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Age:").pack(pady=5)
age_entry = tk.Entry(root)
age_entry.pack()

submit_btn = tk.Button(root, text="Submit", command=validate)
submit_btn.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
