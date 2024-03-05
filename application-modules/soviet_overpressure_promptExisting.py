import tkinter as tk
from tkinter import ttk
import pandas as pd
from glasstone.overpressure import soviet_overpressure

# Load CSV data
df = pd.read_csv('nuclear_explosions.csv')

# Mapping from CSV column names to readable descriptions
column_descriptions = {
    "Location.Country": "Country deploying the nuclear device",
    "Location.Region": "Region where nuclear device was deployed",
    "Data.Source": "Source that reported the explosion event",
    "Location.Cordinates.Latitude": "Latitude position",
    "Location.Cordinates.Longitude": "Longitude position",
    "Data.Magnitude.Body": "Body wave magnitude of explosion (mb)",
    "Data.Magnitude.Surface": "Surface wave magnitude of explosion (Ms)",
    "Location.Cordinates.Depth": "Depth at detonation in Km",
    "Data.Yeild.Lower": "Explosion yield lower estimate in kilotons of TNT",
    "Data.Yeild.Upper": "Explosion yield upper estimate in kilotons of TNT",
    "Data.Purpose": "Purpose of detonation",
    "Data.Name": "Name of event or bomb",
    "Data.Type": "Type - method of deployment",
    "Date.Day": "Day of detonation",
    "Date.Month": "Month of detonation",
    "Date.Year": "Year of detonation",
}

def format_bomb_info(selected_bomb):
    info_text = ""
    for key, description in column_descriptions.items():
        #corrected_key = key.replace('.', '_')  # Assuming DataFrame uses underscores instead of periods
        value = selected_bomb.get(key, "N/A")
        info_text += f"{description}: {value}\n"
    return info_text

def on_country_select(event):
    country = country_var.get()
    print(f"Selected Country: {country}")
    unique_bombs = df[df['Location.Country'] == country]['Data.Name'].unique()
    print(f"Unique Bombs: {unique_bombs}")
    bomb_var.set('')
    bomb_dropdown['menu'].delete(0, 'end')
    for bomb in unique_bombs:
        bomb_dropdown['menu'].add_command(label=bomb, command=lambda bomb=bomb: bomb_var.set(bomb))
    if unique_bombs.size > 0:
        bomb_var.set(unique_bombs[0])
    else:
        bomb_var.set('No bombs available')

def calculate_overpressure():
    selected_bomb_name = bomb_var.get()
    if selected_bomb_name and selected_bomb_name != 'No bombs available':
        selected_bomb = df[df['Data.Name'] == selected_bomb_name].iloc[0].to_dict()
        lower_yield_kt = float(selected_bomb['Data.Yeild.Lower'])
        upper_yield_kt = float(selected_bomb['Data.Yeild.Upper'])
        distance_m = float(distance_entry.get())
        burst_height_m = float(burst_height_entry.get())
        if lower_yield_kt == 0: lower_yield_kt += 1
        if upper_yield_kt == 0: upper_yield_kt += 1
        lower_overpressure = soviet_overpressure(lower_yield_kt, distance_m, burst_height_m, thermal_layer=False, yunits='kT', dunits='m', opunits='kg/cm^2')
        upper_overpressure = soviet_overpressure(upper_yield_kt, distance_m, burst_height_m, thermal_layer=False, yunits='kT', dunits='m', opunits='kg/cm^2')
        kgcm2_to_psi = 14.2233
        lower_overpressure_psi = lower_overpressure * kgcm2_to_psi
        upper_overpressure_psi = upper_overpressure * kgcm2_to_psi
        mid_overpressure_psi = (lower_overpressure_psi + upper_overpressure_psi) / 2
        formatted_info = format_bomb_info(selected_bomb)
        result_text = f"Lower Overpressure: {lower_overpressure_psi:.2f} PSI\nUpper Overpressure: {upper_overpressure_psi:.2f} PSI\nMidpoint Overpressure: {mid_overpressure_psi:.2f} PSI\n\nSelected Warhead Info:\n\n{formatted_info}"
        result_label.config(text=result_text)
    else:
        result_label.config(text="Please select a valid bomb.")

root = tk.Tk()
root.title("Nuclear Explosion Overpressure Calculator")
country_var = tk.StringVar(root)
countries = df['Location.Country'].unique()
tk.Label(root, text="Select Country:").grid(row=0, column=0, sticky=tk.W)
country_dropdown = ttk.Combobox(root, textvariable=country_var, values=countries)
country_dropdown['values'] = [country.strip() for country in df['Location.Country'].unique().tolist()]
country_dropdown.grid(row=0, column=1, sticky=tk.W)
country_dropdown.bind('<<ComboboxSelected>>', on_country_select)
bomb_var = tk.StringVar(root)
tk.Label(root, text="Select Warhead:").grid(row=1, column=0, sticky=tk.W)
bomb_dropdown = tk.OptionMenu(root, bomb_var, ())
bomb_dropdown.grid(row=1, column=1, sticky=tk.W)
tk.Label(root, text="Distance (meters):").grid(row=2, column=0, sticky=tk.W)
distance_entry = tk.Entry(root)
distance_entry.grid(row=2, column=1, sticky=tk.W)
tk.Label(root, text="Burst Height (meters):").grid(row=3, column=0, sticky=tk.W)
burst_height_entry = tk.Entry(root)
burst_height_entry.grid(row=3, column=1, sticky=tk.W)
tk.Button(root, text="Calculate", command=calculate_overpressure).grid(row=4, column=0, columnspan=2, pady=10)
result_label = tk.Label(root, text="Overpressure: ")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
