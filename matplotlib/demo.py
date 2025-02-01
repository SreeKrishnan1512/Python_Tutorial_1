import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Generate some sample data
x = np.linspace(0, 100, 100)
y = np.sin(x / 10)

# Create the plot
fig, ax = plt.subplots()
ax.plot(x, y)

# Set major ticks at 20, 40, 60, ...
major_ticks = np.arange(20, 101, 20)
ax.set_xticks(major_ticks)

# Set minor ticks at 5, 10, 15, ...
minor_locator = MultipleLocator(5)
ax.xaxis.set_minor_locator(minor_locator)

# Optionally, add grid lines for better visualization
ax.grid(which='major', color='black', linestyle='-', linewidth=0.8)
ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()
