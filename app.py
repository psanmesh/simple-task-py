import tkinter as tk
from tkinter import messagebox
from db import init_db, insert_item, fetch_items

class PocApp:
    def __init__(self, root):
        self.root = root
        self.root.title("POC App")
        self.root.geometry("400x300")

        # Input
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Save button
        self.save_btn = tk.Button(root, text="Save", command=self.save_item)
        self.save_btn.pack(pady=5)

        # List
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        self.load_items()

    def save_item(self):
        value = self.entry.get().strip()
        if not value:
            messagebox.showwarning("Validation", "Input cannot be empty")
            return

        insert_item(value)
        self.entry.delete(0, tk.END)
        self.load_items()

    def load_items(self):
        self.listbox.delete(0, tk.END)
        for item in fetch_items():
            self.listbox.insert(tk.END, item)

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = PocApp(root)
    root.mainloop()
