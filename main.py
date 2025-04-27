import math
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
        entry.insert(0, default_value)  
        entry.pack()
        entries[label] = entry 

    def submit():
        nonlocal entries 
        entries = {label: entry.get() for label, entry in entries.items()}
        popup.destroy()
    
    ttk.Button(popup, text="Submit", command=submit).pack(pady=20)

    popup.grab_set()
    root.wait_window(popup)
    return entries

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
    options = ["Circle", "Rectangle", "Triangle", "Square", "Parallelogram"]
    combo = ttk.Combobox(root, values=options)
    combo.set("Select the shape of this face")  # Set default text
    combo['state'] = 'readonly'
    combo.pack(pady=10)

    combo.bind("<<ComboboxSelected>>", on_select)

def calculate_area(face, list) -> float:
    area = 0.0
    global minimum_dimension, maximum_area
    
    if face == "Circle":
        for item in list:
            area = 3.1415 * float(item['Radius']) * float(item['Radius'])
            if area > maximum_area:
                maximum_area = area
                minimum_dimension = item['Radius']

    elif face == "Rectangle":
        for item in list:
            area = float(item['Width']) * float(item['Height'])
            if area > maximum_area:
                maximum_area = area
                minimum_dimension = min(float(item['Width']), float(item['Height']))

    elif face == "Triangle":
        for item in list:
            area = float(item['Base']) * float(item['Height']) / 2.0
            if area > maximum_area:
                maximum_area = area
                minimum_dimension = min(float(item['Base']), float(item['Height']))

    elif face == "Square":
        for item in list:
            area = float(item['Side']) * float(item['Side'])
            if area > maximum_area:
                maximum_area = area
                minimum_dimension = min(float(item['Side']), float(item['Side']))

    elif face == "Parallelogram":
        for item in list:
            area = float(item['Base']) * float(item['Height'])
            if area > maximum_area:
                maximum_area = area
                minimum_dimension = min(float(item['Base']), float(item['Height']))

    return area

def get_right_temp(carbon) -> float:
    pt1 = (0.8, 723)
    pt2 = (2.0, 1147)
    len = math.sqrt( (pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2 )
    v1 = ( (pt2[0] - pt1[0]) / len, (pt2[1] - pt1[1]) / len)

    diff = (carbon - 0.8) / v1[0]
    temperature = pt1[1] * v1[1] * diff
    
    return temperature

def get_left_temp(carbon) -> float:
    pt1 = (0.8, 723)
    pt2 = (0.0, 910)
    len = math.sqrt( (pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2 )
    v1 = ( (pt2[0] - pt1[0]) / len, (pt2[1] - pt1[1]) / len)

    diff = (float(carbon) - 0.8) / v1[0]
    temperature = pt1[1] * v1[1] * diff
    
    return temperature

def submit():
    # validate the percentage entered
    global temperature, minimum_dimension, maximum_area
    carbon_value = float(carbon_entry.get())

    if float(carbon_value) > 2.0 or float(carbon_value) < 0.0:
        messagebox.showerror("Error", "Invalid carbon percentage (0-2%)")
        return    
    elif float(carbon_value) > 0.8:
        temperature = get_right_temp(carbon_value)
    else:
        temperature = get_left_temp(carbon_value)

    print(maximum_area)
    for face, list in faces.items():
        calculate_area(face, list)

    show_results(temperature, minimum_dimension)
    return

def show_results(temperature, minimum_dimension):
    messagebox.showinfo("Results", f"The temperature is: {temperature}.\n The minimum distance is: {minimum_dimension}.")

# -----------------------------------------------------------------------------

root = tk.Tk()
root.title("Iron Smelting Assistance")
root.geometry("800x600")

tk.Label(root, text="Enter Carbon Percentage").pack()
carbon_entry = ttk.Entry(root)
carbon_entry.pack()

tk.Button(root, text="Add Face", command=add_face).pack(pady=10)
tk.Button(root, text="Submit", command=submit).pack(pady=10)

inf = 1e9
faces = {}
temperature = 0
maximum_area = 0
minimum_dimension = inf

# Run the application
root.mainloop()
