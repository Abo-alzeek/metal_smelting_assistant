import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def create_popup(**kwargs):
    popup = tk.Toplevel(root)
    popup.title("Enter Values")
    popup.geometry("300x200")
    
    # Add widgets
    tk.Label(popup, text="Enter Dimensions:").pack(pady=10)
    entries = {}

    for label, default_value in kwargs.items():
        tk.Label(popup, text=label.replace('_', ' ').title()).pack()
        entry = ttk.Entry(popup)
        entry.insert(0, default_value)  # Insert default value if provided
        entry.pack()
        entries[label] = entry  # Store reference to the entry widget

    def submit():
        nonlocal entries 
        entries = {label: entry.get() for label, entry in entries.items()}
        popup.destroy()
    
    ttk.Button(popup, text="Submit", command=submit).pack(pady=20)

    # Make the popup modal (optional)
    popup.grab_set()
    root.wait_window(popup)
    return entries  # This will return after popup is destroyed

def on_select(event):
    results = {}

    if event.widget.get() == "Circle":
        results = create_popup(Radius=0)
    elif event.widget.get() == "Square":
        results = create_popup(Side=0)
    elif event.widget.get() == "Rectangle":
        results = create_popup(Width=0, Height=0)
    elif event.widget.get() == "Triangle":
        results = create_popup(Base=0, Height=0)
    elif event.widget.get() == "Parallelogram":
        results = create_popup(Base=0, Height=0)
    
    if event.widget.get() not in faces:
        faces[event.widget.get()] = [results]
    else:
        faces[event.widget.get()].append(results)

    print(faces)

def add_face():
    # Create the Combobox
    options = ["Circle", "Rectangle", "Triangle", "Square", "Parallelogram"]
    combo = ttk.Combobox(root, values=options)
    combo.set("Select the shape of this face")  # Set default text
    combo['state'] = 'readonly'
    combo.pack(pady=10)

    # Bind the selection event
    combo.bind("<<ComboboxSelected>>", on_select)

def calculate_area(face, list) -> int:
    area = 0.0

    if face == "Circle":
        for item in list:
            area = max(area, 3.1415 * float(item['Radius']) * float(item['Radius']))
    elif face == "Rectangle":
        for item in list:
            area = max(area, item['Width'] * item['Height'])
    elif face == "Triangle":
        for item in list:
            area = max(area, item['Base'] * item['Height'] / 2.0)
    elif face == "Square":
        for item in list:
            area = max(area, item['Side'] * item['Side'])
    elif face == "Parallelogram":
        for item in list:
            area = max(area, 3.1415 * item['Base'] * item['Height'])

    return area

def submit():
    # validate the percentage entered

    global maximum_area
    print(maximum_area)
    for face, list in faces.items():
        maximum_area = max(maximum_area, int(calculate_area(face, list)))

    return

# Create the main window
root = tk.Tk()
root.title("Iron Smelting Assistance")
root.geometry("800x600")  # width x height

tk.Label(root, text="Enter Carbon Percentage").pack()
entry = ttk.Entry(root).pack()

tk.Button(root, text="Add Face", command=add_face).pack(pady=10)
tk.Button(root, text="Submit", command=submit).pack(pady=10)

faces = {}
maximum_area = 0

# Run the application
root.mainloop()