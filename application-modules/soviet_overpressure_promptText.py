# Import necessary modules
from tkinter import *
from glasstone.overpressure import soviet_overpressure

def calculate_overpressure():
    try:
        yield_kt = float(yield_entry.get())
        distance_m = float(distance_entry.get())
        burst_height_m = float(burst_height_entry.get())
        if any(n < 0 for n in [yield_kt, distance_m, burst_height_m]): return result_label.config(text="Negative numbers are not allowed.")
        thermal_layer_input = thermal_layer_var.get()
        thermal_layer = True if thermal_layer_input == 'yes' else False

        # Calculate overpressure
        overpressure = soviet_overpressure(yield_kt, distance_m, burst_height_m, thermal_layer=thermal_layer, yunits='kT', dunits='m', opunits='kg/cm^2')

        # Convert kg/cm^2 to PSI
        kgcm2_to_psi = 14.2233
        overpressure_psi = overpressure * kgcm2_to_psi

        result_label.config(text=f"Overpressure: {overpressure_psi:.2f} PSI")
    except ValueError:
        result_label.config(text="Please enter valid numbers for all inputs.")

# Create main window
root = Tk()
root.title("Nuclear Explosion Overpressure Calculator")

# Create and arrange widgets
Label(root, text="Yield (kilotons):").grid(row=0, column=0, sticky=W)
yield_entry = Entry(root)
yield_entry.grid(row=0, column=1, sticky=W)

Label(root, text="Distance (meters):").grid(row=1, column=0, sticky=W)
distance_entry = Entry(root)
distance_entry.grid(row=1, column=1, sticky=W)

Label(root, text="Burst Height (meters):").grid(row=2, column=0, sticky=W)
burst_height_entry = Entry(root)
burst_height_entry.grid(row=2, column=1, sticky=W)

Label(root, text="Thermal Layer Present? (yes/no):").grid(row=3, column=0, sticky=W)
thermal_layer_var = StringVar(root)
thermal_layer_var.set("no") # default value
thermal_layer_entry = OptionMenu(root, thermal_layer_var, "yes", "no")
thermal_layer_entry.grid(row=3, column=1, sticky=W)

Button(root, text="Calculate", command=calculate_overpressure).grid(row=4, column=0, columnspan=2, pady=10)

result_label = Label(root, text="Overpressure: ")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()

