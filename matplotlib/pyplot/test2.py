import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

x_ticks_major = np.arange(0, 6, 1)  # Major ticks at every integer
y_ticks_major= np.arange(0,6,1)

# Create the plot
fig, ax = plt.subplots()
ax.plot(x_ticks_major, y_ticks_major, color="red")

# Set major ticks at 20, 40, 60, ...

ax.set_xticks(x_ticks_major)


ax.set_yticks(y_ticks_major)

minor_locator_yaxis=MultipleLocator(0.5)
ax.yaxis.set_minor_locator(minor_locator_yaxis)

# Set minor ticks at 0.2, 0.4, 0.6, ...
minor_locator_xaxis = MultipleLocator(0.2)  # Minor ticks at smaller intervals
ax.xaxis.set_minor_locator(minor_locator_xaxis)

# Optionally, add grid lines for better visualization
ax.grid(which='major', color='blue', linestyle='solid', linewidth=0.8)
ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.5)

# Annotate and mark each data point on the plot
for i in range(len(x_ticks_major)):
    x_point, y_point = x_ticks_major[i], y_ticks_major[i]
    ax.scatter(x_point, y_point, color="blue", zorder=5)  # Mark the point with a blue dot
    ax.text(x_point + 0.1, y_point, f"({x_point}, {y_point})", color="black", fontsize=8)  # Annotate the point

# Title and labels
ax.set_title("Array Data with Markers and Annotations")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Show the plot
plt.show()
