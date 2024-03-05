import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from glasstone.overpressure import soviet_overpressure

# Initialize the figure and axis for plotting
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.4)

# This function will be empty as we are not plotting, but we need it to create sliders
def dummy_plot():
    ax.plot([], [])
    ax.set_title('Nuclear Explosion Overpressure Calculator')

# Initial parameters
yield_kt_initial = 1000  # in kilotons
distance_m_initial = 1000  # in meters
burst_height_m_initial = 1000  # in meters
thermal_layer = False  # Initial value for thermal layer presence

# Draw the initial plot (which is just a placeholder)
dummy_plot()

# Add sliders for interactive control
axcolor = 'lightgoldenrodyellow'
ax_yield = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_distance = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_burst_height = plt.axes([0.1, 0.2, 0.65, 0.03], facecolor=axcolor)

slider_yield = Slider(ax_yield, 'Yield (kilotons)', 0, 10000, valinit=yield_kt_initial)
slider_distance = Slider(ax_distance, 'Distance (meters)', 0, 10000, valinit=distance_m_initial)
slider_burst_height = Slider(ax_burst_height, 'Burst Height (meters)', 0, 10000, valinit=burst_height_m_initial)

# Placeholder for the result text
result_text = ax.text(0.5, 0.5, '', transform=ax.transAxes, ha="center", va="center")

def update(val):
    yield_kt = slider_yield.val
    distance_m = slider_distance.val
    burst_height_m = slider_burst_height.val

    # Calculate overpressure
    overpressure = soviet_overpressure(yield_kt, distance_m, burst_height_m, thermal_layer=thermal_layer, yunits='kT', dunits='m', opunits='kg/cm^2')
    
    # Convert kg/cm^2 to PSI
    kgcm2_to_psi = 14.2233
    overpressure_psi = overpressure * kgcm2_to_psi

    result_text.set_text(f"Overpressure: {overpressure_psi:.2f} PSI")

# Update the plot when sliders are changed
slider_yield.on_changed(update)
slider_distance.on_changed(update)
slider_burst_height.on_changed(update)

plt.show()
