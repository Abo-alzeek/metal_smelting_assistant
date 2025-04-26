import tkinter as tk
from tkinter import ttk

def create_popup():
    popup = tk.Toplevel(root)
    popup.title("Enter Values")
    popup.geometry("300x200")
    
    # Add widgets
    tk.Label(popup, text="Enter dimensions:").pack(pady=10)
    
    tk.Label(popup, text="Width:").pack()
    width_entry = ttk.Entry(popup)
    width_entry.pack()
    
    tk.Label(popup, text="Height:").pack()
    height_entry = ttk.Entry(popup)
    height_entry.pack()
    
    def submit():
        width = width_entry.get()
        height = height_entry.get()
        print(f"Width: {width}, Height: {height}")
        popup.destroy()
    
    ttk.Button(popup, text="Submit", command=submit).pack(pady=20)

root = tk.Tk()
ttk.Button(root, text="Open Popup", command=create_popup).pack(pady=50)
root.mainloop()