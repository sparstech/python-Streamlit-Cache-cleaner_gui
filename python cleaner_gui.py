import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

CACHE_PATTERNS = ["__pycache__", ".cache", ".pytest_cache"]

def clean_cache():
    deleted = 0
    base_dir = Path.home()

    for root, dirs, files in os.walk(base_dir):
        for name in dirs:
            if name in CACHE_PATTERNS:
                try:
                    shutil.rmtree(Path(root) / name)
                    deleted += 1
                except:
                    pass

        for name in files:
            if name.endswith(".pyc"):
                try:
                    os.remove(Path(root) / name)
                    deleted += 1
                except:
                    pass

    messagebox.showinfo("Done", f"Deleted {deleted} cache items ✅")

# GUI
app = tk.Tk()
app.title("Python Cache Cleaner")
app.geometry("300x150")

label = tk.Label(app, text="Clean Python & Streamlit Cache", font=("Arial", 12))
label.pack(pady=10)

btn = tk.Button(app, text="Run Cleanup", command=clean_cache, bg="green", fg="white")
btn.pack(pady=10)

app.mainloop()