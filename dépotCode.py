
"""
from tkinter import Tk, Entry, StringVar

def is_float(input):
    try:
        float(input)
        return True
    except ValueError:
        return False

def calculate_reste(*args):
    try:
        prix = float(prix_var.get())
        encaiss = float(encaiss_var.get())
        reste = prix - encaiss
        reste_var.set(str(reste))
    except ValueError:
        pass

root = Tk()

# Define the variables
prix_var = StringVar()
encaiss_var = StringVar()
reste_var = StringVar()

# Register the validation function
validate_float = root.register(is_float)

# Create the Entry widgets
prix_entry = Entry(root, textvariable=prix_var, validate="key", validatecommand=(validate_float, '%P'))
encaiss_entry = Entry(root, textvariable=encaiss_var, validate="key", validatecommand=(validate_float, '%P'))
reste_entry = Entry(root, textvariable=reste_var)

# Pack the widgets
prix_entry.pack()
encaiss_entry.pack()
reste_entry.pack()

# Set up the trace
prix_var.trace("w", calculate_reste)
encaiss_var.trace("w", calculate_reste)

root.mainloop()
"""