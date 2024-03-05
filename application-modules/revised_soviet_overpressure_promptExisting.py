
import tkinter as tk
from tkinter import ttk
import pandas as pd

# Load CSV data
df = pd.read_csv('nuclear_explosions.csv')

def on_country_select(event):
    # Get the selected country, strip leading/trailing spaces, and ensure case-insensitive matching
    country = country_var.get().strip().lower()

    # Filter the DataFrame for the selected country with case-insensitive comparison
    country_df = df[df['Location.Country'].str.strip().str.lower() == country]

    # Debugging output
    print(f"Selected Country: {country}, Matches Found: {len(country_df)}")

    # Update the treeview with the country-specific data
    for i in tree.get_children():
        tree.delete(i)
    for index, row in country_df.iterrows():
        tree.insert("", tk.END, values=(row['Location.Country'], row['Data.Yeild.Lower'], row['Data.Yeild.Upper'], row['Date.Year']))

# Setting up the GUI
root = tk.Tk()
root.title("Nuclear Explosions Data Viewer")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

country_var = tk.StringVar()
country_combobox = ttk.Combobox(mainframe, textvariable=country_var)
country_combobox['values'] = [country.strip() for country in df['Location.Country'].unique().tolist()]
country_combobox.grid(column=2, row=1)
country_combobox.bind('<<ComboboxSelected>>', on_country_select)

# Setting up the Treeview
tree = ttk.Treeview(mainframe, columns=('Country', 'Yield Lower', 'Yield Upper', 'Year'), show='headings')
tree.heading('Country', text='Country')
tree.heading('Yield Lower', text='Yield Lower')
tree.heading('Yield Upper', text='Yield Upper')
tree.heading('Year', text='Year')
tree.grid(column=0, row=2, columnspan=3)

root.mainloop()
